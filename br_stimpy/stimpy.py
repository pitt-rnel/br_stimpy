"""br_stimpy: a python package to interface with Blackrock Cerestim API."""

# br_stimpy.stimpy
# Author: Jeff Weiss <jeff.weiss@pitt.edu>
# May 2022

from __future__ import annotations  # ensure forward compatibility
from br_stimpy import _bstimulator
from br_stimpy.constants import *
from br_stimpy.enums import *
from br_stimpy._validation import _ValidationFcns
from br_stimpy.group_stim_struct import GroupStimulusStruct
from typing import List, Optional, Any


def get_enum_docstr(enum_val: Any) -> str:
    """Lookup docstr for a pybind11 enum value and output as string

    Args:
        enum_val: an enumeration value from the _bstimulator module

    Returns:
        docstr for the enum_val
    """
    enum_entries = enum_val.__entries
    doc_str = enum_entries[enum_val.name][1]
    return doc_str


def get_api_version() -> _bstimulator.Version:
    """Get Cerestim API library version

    Returns:
        structure containing version info
    """
    version_struct = _bstimulator.Version()
    result = _bstimulator.Stimulator().lib_version(version_struct)
    if result != _bstimulator.success:
        err_doc = get_enum_docstr(result)
        error_str = f"{result.name.upper()} error in get_api_version():\n {err_doc}"
        raise RuntimeError(error_str)
    return version_struct


class Stimulator(object):
    """Simple python interface to Blackrock Cerestim 96
    
    Raises:
            RuntimeError: Only 12 stimulator objects can be created at a time
    """

    device_vector: Optional[List[int]] = None
    _stimulator_count: int = 0

    # repeat _bstimulator references here (user can access from either module or class)
    OCVolt = OCVolt  # enum class for compliance voltage
    WFType = WFType  # enum class for anodal or cathodal first
    TriggerType = TriggerType
    ElectrodeChannelMap = ElectrodeChannelMap
    PartNumbers = PartNumbers
    ModuleStatus = ModuleStatus
    SeqType = SeqType

    def __init__(self) -> None:
        Stimulator._stimulator_count += 1
        if Stimulator._stimulator_count > MAX_STIMULATORS:
            raise RuntimeError("Max stimulator error")

        self._bstimulator_obj: _bstimulator.Stimulator = (
            _bstimulator.Stimulator()
        )  # raw stimulator object
        self.device_index: Optional[List[int]] = None
        self.last_result: ResultType = _bstimulator.success
        self._pattern_cache = {key: None for key in range(1, MAX_CONFIGURATIONS)}

    # Properties

    @property
    def api_version(self) -> _bstimulator.Version:
        """Get Cerestim API library version

        Returns:
            structure containing version info
        """
        version_struct = _bstimulator.Version()
        self.last_result = self._bstimulator_obj.lib_version(version_struct)
        self._raise_if_error("api_lib_version")
        return version_struct

    @property
    def stimulus_patterns_cached(self) -> dict:
        """Get cached list of configured stimulus patterns

        Returns:
            15 cached _bstimulator.StimulusConfiguration
            structures,  None if configuration is inactive.
        """
        return self._pattern_cache

    @property
    def device_info(self) -> dict:
        """Read device hardware and firmware info

        This returns all the information about the CereStim 96 that is
        connected to. It will tell its part number, serial number,
        firmware versions for both the motherboard and for the current
        modules. It will also tell you the protocol that the motherboard
        is using with the current modules and the number of installed
        current modules.
        """
        dev_info = _bstimulator.DeviceInfo()
        self.last_result = self._bstimulator_obj.read_device_info(dev_info)
        self._raise_if_error("read_device_info")

        output = dict = {
            "serial_no": self._convert_raw_serial_num(dev_info.serial_no),
            "mainboard_version": self._convert_raw_version(dev_info.mainboard_version),
            "protocol_version": self._convert_raw_version(dev_info.protocol_version),
            "module_status": [ModuleStatus(x) for x in dev_info.module_status],
            "module_version": [
                self._convert_raw_version(x) for x in dev_info.module_version
            ],
        }
        return output

    @property
    def sequence_status(self) -> SeqType:
        """Get stim sequence status

        Can be read anytime as it does not interrupt other functions
        from executing, but simply reads what state the stimulator is in.
        """
        output = _bstimulator.SequenceStatus()
        self.last_result = self._bstimulator_obj.read_sequence_status(output)
        self._raise_if_error("read_sequence_status")
        return SeqType(output.status)

    @property
    def is_stim_sequence_playing(self) -> bool:
        """Check if a stim sequence is actively playing"""
        return self.sequence_status == self.SeqType.playing

    @property
    def is_connected(self) -> bool:
        """Check if stimulator is connected

        Lets the user know that the Stimulator object is connected to a
        physical CereStim 96 device.
        """
        return bool(self._bstimulator_obj.is_connected())

    @property
    def serial_number(self) -> dict:
        """Get device serial number

        Retrieves the serial number that is programmed into the
        CereStim 96 device that is attached.
        """
        return self._convert_raw_serial_num(self._bstimulator_obj.get_serial_number())

    @property
    def motherboard_firmware_version(self) -> dict:
        """Get main firmware version

        Retrieves the firmware revision of the microcontroller on the
        motherboard.
        """
        return self._convert_raw_version(
            self._bstimulator_obj.get_motherboard_firmware_version()
        )

    @property
    def protocol_version(self) -> dict:
        """Get motherboard protocol version

        The protocol version that the motherboard uses to send and
        receive data from the current modules.
        """
        return self._convert_raw_version(self._bstimulator_obj.get_protocol_version())

    @property
    def min_max_amplitude(self) -> dict:
        """Get hardware min and max amplitudes

        Since there are different models and version of the stimulator,
        such as the micro and macro versions, this will allow the user
        to get the min and max amplitudes that are allowed for
        stimulation.
        """
        return self._convert_raw_min_max_amp(
            self._bstimulator_obj.get_min_max_amplitude()
        )

    @property
    def module_firmware_version(self) -> List[dict]:
        """Get firmware versions of current modules

        Each current module has its own microcontroller and has a
        firmware version. All current modules in a single stimulator
        should have the same firmware version. The MSB is the Major
        revision number and the LSB is the minor revision number. I.e.
        0x0105 would be version 1.5
        """
        fv = self._bstimulator_obj.get_module_firmware_version()
        output = [self._convert_raw_version(x) for x in fv]
        return output[: self.get_number_modules()]

    @property
    def module_status(self) -> List[ModuleStatus]:
        """Get status of each current module

        This tells the status of each current module, whether it is
        enabled, disabled, or not available.
        """
        ms = self._bstimulator_obj.get_module_status()
        output = [ModuleStatus(x) for x in ms]
        return output[: self.get_number_modules()]

    @property
    def usb_address(self) -> int:
        """Gets the USB address of the connected stimulator"""
        return self._bstimulator_obj.get_usb_address()

    @property
    def max_hard_charge(self) -> int:
        """Get hardware max charge per phase

        This value is based on the hardware of the particular model of
        the CereStim 96. Again the micro and macro versions of the
        stimulator have different values
        """
        return self._bstimulator_obj.get_max_hard_charge()

    @property
    def min_hard_frequency(self) -> int:
        """Get hardware minimum frequency in Hz

        This value is based on the hardware of the particular model of
        the CereStim 96. Again the micro and macro versions of the
        stimulator have different values
        """
        return self._bstimulator_obj.get_min_hard_frequency()

    @property
    def max_hard_frequency(self) -> int:
        """Get hardware maximum frequency in Hz

        This value is based on the hardware of the particular model of
        the CereStim 96. Again the micro and macro versions of the
        stimulator have different values
        """
        return self._bstimulator_obj.get_max_hard_frequency()

    @property
    def number_modules(self) -> int:
        """Get number of current modules installed

        This value is based on the hardware of the particular model of
        the CereStim 96. Again the micro and macro versions of the
        stimulator have different values
        """
        return self._bstimulator_obj.get_number_modules()

    @property
    def max_hard_width(self) -> int:
        """Get hardware maximum pulse width in us

        This value is based on the hardware of the particuliar model of
        the CereStim 96.
        """
        return self._bstimulator_obj.get_max_hard_width()

    @property
    def max_hard_interphase(self) -> int:
        """Get hardware maximum interphase width in us

        This value is based on the hardware of the particuliar model of
        the CereStim 96
        """
        return self._bstimulator_obj.get_max_hard_interphase()

    @property
    def is_safety_disabled(self) -> bool:
        """Check if safety limits are disabled

        For Internal validation and testing it is required to disable
        the safety limits in the firmware and API so that hardware
        limits can be observed and tested.
        """
        return bool(self._bstimulator_obj.is_safety_disabled())

    @property
    def is_device_locked(self) -> bool:
        """Check if stimulator is locked

        If the detected number of current modules doesn't match the
        hardware configuration or if the hardware configuration is not
        setup, the device will be locked down preventing any stimulation
        from occuring.
        """
        return bool(self._bstimulator_obj.is_device_locked())

    # public class method
    @classmethod
    def scan_for_devices(cls) -> List[int]:
        """Scan for connected Cerestim devices

        If only one Cerestim device is attached to PC, you can skip this step
        and just call connect().

        Returns:
            list of serial numbers of the connected Cerestims
        """
        cls.device_vector = list(_bstimulator.Stimulator.scan_for_devices())
        return cls.device_vector

    # public instance methods
    def connect(self, device_index: int = 0) -> None:
        """Connect to Cerestim.

        If multiple devices are attached to PC, first call scan_for_devices
        to view the list of serial numbers, then input the device_index you
        would like to connect to.

        Args:
            device_index (optional): Index of device from scan_for_devices.
                Defaults to 0.

        Raises:
            IndexError: Invalid device_index
            RuntimeError: No Cerestim devices found
        """
        if not self.device_vector:
            # assume scan_for_devices has not been called yet if attribute is empty
            self.scan_for_devices()
        if len(self.device_vector) >= (device_index + 1):
            self.last_result = self._bstimulator_obj.set_device(device_index)
            self._raise_if_error("set_device")
            self.last_result = self._bstimulator_obj.connect(
                _bstimulator.interface_default, None
            )
            self._raise_if_error("connect")
        else:
            if self.device_vector:
                raise IndexError("Invalid device_index")
            else:
                raise RuntimeError("No Cerestim devices found")
        # if successfully connected, initialize stimulus_patterns_cached
        self.read_all_stimulus_patterns()

    def disconnect(self) -> None:
        """Disconnect from Cerestim"""
        self.last_result = self._bstimulator_obj.disconnect()
        self._raise_if_error("disconnect")

    def simple_stimulus(
        self,
        electrode: int,
        afcf: WFType,
        pulses: int,
        amp1: int,
        amp2: int,
        width1: int,
        width2: int,
        frequency: int,
        interphase: int,
    ) -> None:
        """Simplest method to manually command a stimulus pulse

        Combines configure_stimulus_pattern() and manual_stimulus()
        into a single call. Note that the overhead of
        configure_stimulus_pattern() limits how quickly this can run.
        This method is simple, but inefficient.

        Args:
            electrode: The electrode that should be stimulated.
                Valid values are from 1 - 96.
            afcf: What polarity should the first
                phase be, Anodic or Cathodic first
            pulses: The number of stimulation pulses in waveform
                from 1 - 255
            amp1: The amplitude of the first phase, for Micro it
                is 1 - 215 uA, and for Macro it is 100 uA - 10 mA
            amp2: The amplitude of the first phase, for Micro it
                is 1 - 215 uA, and for Macro it is 100 uA - 10 mA
            width1: The width of the first phase in the stimulation
                1 - 65,535 uS
            width2: The width of the second phase in the stimulation
                1 - 65,535 uS
            frequency: The stimulating frequency at which the
                biphasic pulses should repeat 4 - 5000 Hz
            interphase: The period of time between the first and
                second phases 53 - 65,535 uS
        """
        self.configure_stimulus_pattern(
            1, afcf, pulses, amp1, amp2, width1, width2, frequency, interphase
        )
        self.manual_stimulus(electrode, 1)

    def simple_stimulus_group(
        self,
        electrodes: List[int],
        afcf: WFType,
        pulses: int,
        amp1: int,
        amp2: int,
        width1: int,
        width2: int,
        frequency: int,
        interphase: int,
    ) -> None:
        """Simplest method to manually command a group stimulus pulse
        with identical parameters on all electrodes

        Combines configure_stimulus_pattern() and group_stimulus()
        into a single call. Note that the overhead of
        configure_stimulus_pattern() limits how quickly this can run.
        This method is simple, but inefficient.

        Args:
            electrodes: The electrodes that should be stimulated.
                Valid values are from 1 - 96.
            afcf: What polarity should the first
                phase be, Anodic or Cathodic first
            pulses: The number of stimulation pulses in waveform
                from 1 - 255
            amp1: The amplitude of the first phase, for Micro it
                is 1 - 215 uA, and for Macro it is 100 uA - 10 mA
            amp2: The amplitude of the first phase, for Micro it
                is 1 - 215 uA, and for Macro it is 100 uA - 10 mA
            width1: The width of the first phase in the stimulation
                1 - 65,535 uS
            width2: The width of the second phase in the stimulation
                1 - 65,535 uS
            frequency: The stimulating frequency at which the
                biphasic pulses should repeat 4 - 5000 Hz
            interphase: The period of time between the first and
                second phases 53 - 65,535 uS
        """
        self.configure_stimulus_pattern(
            1, afcf, pulses, amp1, amp2, width1, width2, frequency, interphase
        )
        patterns = [1] * len(electrodes)
        gc = GroupStimulusStruct(electrodes, patterns)
        self.group_stimulus(begin_seq=True, play=True, times=1, group_stim_struct=gc)

    def manual_stimulus(self, electrode: int, configID: int) -> None:
        """Manually stimulate on one electrode

        Allows the user to send a single stimulus pulse of one of the
        stimulation waveforms to a specified electrode.

        Args:
            electrode: The electrode that should be stimulated.
                Valid values are from 1 - 96.
            configID: The stimulation waveform to use.
                Valid values are from 1 - 15.
        """
        _ValidationFcns.validate_electrode(electrode)
        _ValidationFcns.validate_configID(configID)

        self.last_result = self._bstimulator_obj.manual_stimulus(
            electrode, _bstimulator.Config(configID)
        )
        self._raise_if_error("manual_stimulus")

    def begin_sequence(self) -> None:
        """Begin stim script

        This is the first command that must be called when creating a
        stimulation script. After calling this you are able to call wait(),
        auto_stimulus(), begin_group(), and end_group() commands. The
        stimulation script can have up to 128 commands, excluding
        begin_sequence() and end_sequence()
        """
        self.last_result = self._bstimulator_obj.beginning_of_sequence()
        self._raise_if_error("begin_sequence")

    def end_sequence(self) -> None:
        """End stim script

        This is the last command that must be called when creating a
        stimulation script. It does not count towards the maximum of 128
        commands.
        """
        self.last_result = self._bstimulator_obj.end_of_sequence()
        self._raise_if_error("end_sequence")

    def begin_group(self) -> None:
        """Begin group stim

        This command signifies that the following commands up to the
        end_group() command should all occur simultaneously. The only
        commands that are valid are the auto_stimulus() commands. You
        can only have as many stimulations as the number of current
        modules installed. Can't be called on the last of the 128
        instructions since it needs to have a closing end_group command.
        """
        self.last_result = self._bstimulator_obj.beginning_of_group()
        self._raise_if_error("begin_group")

    def end_group(self) -> None:
        """End group stim

        This command closes off a group of simultaneous stimulations.
        If begin_group() is called during a sequence of commands, then
        there must be an end_group() otherwise the user will get a
        sequence error as a return value.
        """
        self.last_result = self._bstimulator_obj.end_of_group()
        self._raise_if_error("end_group")

    def auto_stimulus(self, electrode: int, configID: int) -> None:
        """Stimulate in stim script

        This command tells the stimulator when to send a stimulus to an
        electrode in a stimulation script. It can be used as many times
        as needed so long as the total number of commands does not exceed
        128. It should also be used within begin_group() and end_group()
        commands to allow for simultaneous stimulations.

        Args:
            electrode: The electrode that will be stimulated.
                Valid values are from 1 - 96
            configID: One of the fifteen stimulation waveforms that should be used.
                Valid values are from 1-15
        """
        _ValidationFcns.validate_electrode(electrode)
        _ValidationFcns.validate_configID(configID)
        self.last_result = self._bstimulator_obj.auto_stimulus(
            electrode, _bstimulator.Config(configID)
        )
        self._raise_if_error("auto_stimulus")

    def wait(self, milliseconds: int) -> None:
        """Wait between stim pulses

        This command can only be used within a stimulation script and
        is capable of adding a wait of up to 65,535 milliseconds.

        Args:
            milliseconds: The number of milliseconds to wait before
                executing the next command

        Raises:
            ValueError: milliseconds must be between 0 and 65535.
        """
        if milliseconds < 0 or milliseconds > 65535:
            raise ValueError("milliseconds out of range (0,65535)")
        self.last_result = self._bstimulator_obj.wait(milliseconds)
        self._raise_if_error("wait")

    def play(self, times: int) -> None:
        """Play stim script

        Tells the stimulator the number of times that it should run the
        stimulation script. A zero passed in will tell it to run
        indefinitely until it is either stopped or paused by the user.
        Other values include between 1 and 65,535 repetitions. Cannot
        be called during a begin_sequence() and end_sequence() command call.
        Args:
            times: Number of times to execute the stimulation script.
            0 means indefinitely.

        Raises:
            ValueError: times must be between 0 and 65535.
        """
        if times < 0 or times > 65535:
            raise ValueError("times out of range (0,65535)")
        self.last_result = self._bstimulator_obj.play(times)
        self._raise_if_error("play")

    def stop(self) -> None:
        """Stop stim script execution

        This will stop a currently running stimulation script and reset
        it so when played again it will begin from the first command.
        Can only be called while the stimulator has a status of
        stimulating or paused.
        """
        self.last_result = self._bstimulator_obj.stop()
        self._raise_if_error("stop")

    def pause(self) -> None:
        """Pause stim script execution

        This will pause a currently running stimulation script and keep
        track of the next command that needs to be executed so if it
        receives a play command it can pick up where it left off.
        """
        self.last_result = self._bstimulator_obj.pause()
        self._raise_if_error("pause")

    def read_max_output_voltage(self) -> int:
        """Read compliance voltage

        This will read the values of +VDD and -VSS on the stimulator
        which allows it to effectively limit the maximum output voltage
        that can be delivered during a stimulation. If the output current
        times the impedance of the electrode is greater than the max
        compliance voltage then it means the full current is not being
        delivered to the electrode because it can not drive any more current.

        Returns:
            the max output voltage in millivolts
        """
        output = _bstimulator.MaxOutputVoltage()
        rw = 0  # read
        v = _bstimulator.ocvolt_invalid
        self.last_result = self._bstimulator_obj.max_output_voltage(output, rw, v)
        self._raise_if_error("max_output_voltage")
        return output.milivolts

    def set_max_output_voltage(self, oc_voltage: OCVolt) -> int:
        """Set compliance voltage

        This will set the values of +VDD and -VSS on the stimulator
        which allows it to effectively limit the maximum output voltage
        that can be delivered during a stimulation. If the output
        current times the impedance of the electrode is greater than the
        max compliance voltage then it means the full current is not
        being delivered to the electrode because it can not drive any
        more current.

        Args:
            oc_voltage: The voltage level that is
                being set. Must be an oc_volt enum value.

        Returns:
            the max output voltage in millivolts.
        """
        output = _bstimulator.MaxOutputVoltage()
        rw = 1  # write
        self.last_result = self._bstimulator_obj.max_output_voltage(
            output, rw, oc_voltage
        )
        self._raise_if_error("max_output_voltage")
        return output.milivolts

    def enable_module(self, module: int) -> None:
        """Enable current module

        Allows the user to enable different current modules that have
        been disabled. This is useful for testing and making sure that
        multiple current modules are all giving the same output values.

        Args:
            module: The current module to be enabled from 0 to 15
        """
        _ValidationFcns.validate_module(module)
        self.last_result = self._bstimulator_obj.enable_module(module)
        self._raise_if_error("enable_module")

    def disable_module(self, module: int) -> None:
        """Disable current module

        Allows the user to disable different current modules that are
        installed in the CereStim. This is useful for testing and making
        sure that multiple current modules are all giving the same output
        values. The current module has to exist to be disabled.

        Args:
            module:The current module to be disabled from 0 to 15
        """
        _ValidationFcns.validate_module(module)
        self.last_result = self._bstimulator_obj.disable_module(module)
        self._raise_if_error("enable_module")

    def configure_stimulus_pattern(
        self,
        configID: int,
        afcf: WFType,
        pulses: int,
        amp1: int,
        amp2: int,
        width1: int,
        width2: int,
        frequency: int,
        interphase: int,
    ) -> None:
        """Set stim pattern configs

        Takes all of the parameters needed in order to create a custom
        biphasic stimulation waveform. The device is capable of handling
        16 differnt waveforms, but waveform 0 is reserved and used for
        testing in getting measurements from electrodes and current
        modules. Micro and Macro stimulators have different ranges of
        valid values. Especially for the amplitude where micro
        stimulators are in the uA range with uA precision, Macro
        stimulators go from 100 uA to 10 mA with 100 uA precision.
        While the widths and interphases have quite a range, the user
        needs to somewhat understand how they interact with the frequency
        chosen. You dont want a stimulus waveform that is longer than
        the time between repeats.

        Args:
            configID: The stimulation waveform that is being
                configured 1 - 15
            afcf: What polarity should the first
                phase be, Anodic or Cathodic first
            pulses: The number of stimulation pulses in waveform
                from 1 - 255
            amp1: The amplitude of the first phase, for Micro it
                is 1 - 215 uA, and for Macro it is 100 uA - 10 mA
            amp2: The amplitude of the first phase, for Micro it
                is 1 - 215 uA, and for Macro it is 100 uA - 10 mA
            width1: The width of the first phase in the stimulation
                1 - 65,535 uS
            width2: The width of the second phase in the stimulation
                1 - 65,535 uS
            frequency: The stimulating frequency at which the
                biphasic pulses should repeat 4 - 5000 Hz
            interphase: The period of time between the first and
                second phases 53 - 65,535 uS
        """
        _ValidationFcns.validate_configID(configID)
        _ValidationFcns.validate_pulses(pulses)
        _ValidationFcns.validate_amp(amp1)
        _ValidationFcns.validate_amp(amp2)
        _ValidationFcns.validate_width(width1)
        _ValidationFcns.validate_width(width2)
        _ValidationFcns.validate_frequency(frequency)
        _ValidationFcns.validate_interphase(interphase)
        self.last_result = self._bstimulator_obj.configure_stimulus_pattern(
            _bstimulator.Config(configID),
            afcf,
            pulses,
            amp1,
            amp2,
            width1,
            width2,
            frequency,
            interphase,
        )
        self._raise_if_error("configure_stimulus_pattern")
        pat = _bstimulator.StimulusConfiguration()
        pat.anodicFirst = afcf
        pat.pulses = pulses
        pat.amp1 = amp1
        pat.amp2 = amp2
        pat.width1 = width1
        pat.width2 = width2
        pat.frequency = frequency
        pat.interphase = interphase
        self._pattern_cache[configID] = pat

    def read_stimulus_pattern(
        self, configID: int
    ) -> _bstimulator.StimulusConfiguration:
        """Read stim config pattern

        Reads back all of the parameters associated with a specific
        stimulation waveform and stores it in the structure supplied by
        the user.

        Args:
            configID: The stimulation waveform that is being read back

        Returns:
            structure which contains all the parameters that consist in
            a stimulation waveform
        """
        _ValidationFcns.validate_configID(configID)
        output = _bstimulator.StimulusConfiguration()
        self.last_result = self._bstimulator_obj.read_stimulus_pattern(
            output, _bstimulator.Config(configID)
        )
        self._raise_if_error("read_stimulus_pattern")
        self._pattern_cache[configID] = output
        return output

    def read_all_stimulus_patterns(self) -> dict:
        """Read back all stim config patterns from stimulator

        Returns:
            15 _bstimulator.StimulusConfiguration structures
            Values are None if configuration is inactive
        """
        patterns = {}
        for configID in range(1, MAX_CONFIGURATIONS):
            try:
                pat = self.read_stimulus_pattern(configID)
            except:  # TODO: check specifically for RuntimeError: CONFIG_NOT_ACTIVE
                pat = None
            patterns[configID] = pat
        self._pattern_cache = patterns
        return self._pattern_cache

    def read_stimulus_max_values(self) -> _bstimulator.MaximumValues:
        """Read maximum stimulus values set using set_stimulus_max_values()

        Returns:
            structure that will contain the current max values that are set
        """
        output = _bstimulator.MaximumValues()
        rw = 0
        v = _bstimulator.ocvolt_invalid
        amp = 0
        charge = 0
        freq = 0
        self.last_result = self._bstimulator_obj.stimulus_max_values(
            output, rw, v, amp, charge, freq
        )
        self._raise_if_error("stimulus_max_values")
        return output

    def set_stimulus_max_values(
        self, voltage: OCVolt, amplitude: int, phaseCharge: int, frequency: int
    ) -> _bstimulator.MaximumValues:
        """Set max limits

        Intended to be an administrative interface that can be password
        protected and only allow the lead researcher to make changes.
        It allows the user to set other determined upper limits for the
        stimulation parameters for whatever safety protocol they are
        requiring. Again micro and macro stimulators will have some
        different bounds for setting max values due to the different
        ranges each are able to achieve.

        Args:
            voltage: The Max Compliance Voltage that can be set
            amplitude: The Max amplitude that can be used in a stimulation
            phaseCharge: The Max charge per phase that will be allowed (Charge = Amplitude * Width)
            frequency: The Max frequency at which the stimulations can take place

        Returns:
            structure that will contain the current max values that are set
        """
        output = _bstimulator.MaximumValues()
        rw = 1
        self.last_result = self._bstimulator_obj.stimulus_max_values(
            output, rw, voltage, amplitude, phaseCharge, frequency
        )
        self._raise_if_error("stimulus_max_values")
        return output

    def group_stimulus(
        self,
        begin_seq: bool,
        play: bool,
        times: int,
        group_stim_struct: GroupStimulusStruct,
    ) -> None:
        """Send group stimulus command

        There is a lot of overhead in sending commands over the USB to
        the CereStim 96. each function call averages 2mS. This function
        allows the user to create the stimulation parameters beforehand
        and in a single function call perform simultaneous stimulations
        based on different electrodes and configured waveforms.

        Args:
            begin_seq: Boolean expression to tell the function
                that it is the beginning of a sequence
            play: Boolean expression to tell if the stimulator
                should begin stimulating immedieatly after this call
            times: The number of times to play the stimulation,
                is ignored if play = false
            group_stim_struct: structure which has a pair of arrays
                with electrodes and waveforms
        """
        bgroup_stim_struct = _bstimulator.GroupStimulus()
        bgroup_stim_struct.electrode = group_stim_struct.electrode
        bgroup_stim_struct.pattern = group_stim_struct.pattern
        number = group_stim_struct.number
        self.last_result = self._bstimulator_obj.group_stimulus(
            int(begin_seq), int(play), times, number, bgroup_stim_struct
        )
        self._raise_if_error("group_stimulus")

    def trigger_stimulus(self, edge: TriggerType) -> None:
        """Start trigger mode

        Allows the stimulator to wait for a trigger event before
        executing a stimulation script. The stimulator has an external
        TTL Trigger input port that uses TTL logic levels to determine
        whether the input is high or low. The stimulator can be set to
        fire on a rising edge, falling edge, or any edge transition.
        Once in trigger mode the stimulator is locked down from other
        function calls except for stop_trigger_stimulus()

        Args:
            edge: The type of digital event to trigger the stimulation on
        """
        self.last_result = self._bstimulator_obj.trigger_stimulus(edge)
        self._raise_if_error("trigger_stimulus")

    def stop_trigger_stimulus(self) -> None:
        """Stop trigger mode

        Changes the state of the stimulator so that it is no longer
        waiting for a trigger. Frees up the stimulator for other
        commands to be called.
        """
        self.last_result = self._bstimulator_obj.stop_trigger_stimulus()
        self._raise_if_error("stop_trigger_stimulus")

    def update_electrode_channel_map(self, map: ElectrodeChannelMap) -> None:
        """Set electrode map

        Since not all electrodes are found on channel 1 this function
        allows the user to create a map key pair where the channel is
        an index into an array which holds the value of the electrode
        at that channel.

        Args:
            map:channel map structure
        """
        self.last_result = self._bstimulator_obj.update_electrode_channel_map(map)
        self._raise_if_error("update_electrode_channel_map")

    def read_hardware_values(self) -> _bstimulator.ReadHardwareValuesOutput:
        """Reads the hardware values that are set based on the part number

        Returns:
            Structure containing the hardware values
        """
        output = _bstimulator.ReadHardwareValuesOutput()
        self.last_result = self._bstimulator_obj.read_hardware_values(output)
        self._raise_if_error("read_hardware_values")
        return output

    def disable_stimulus_configuration(self, configID: int) -> None:
        """Disables a stimulation waveform so that it is able to be reset

        Args:
            configID: The configuration to disable
        """
        _ValidationFcns.validate_configID(configID)
        self.last_result = self._bstimulator_obj.disable_stimulus_configuration(
            configID
        )
        self._raise_if_error("disable_stimulus_configuration")

    def reset_stimulator(self) -> None:
        """Stimulator Reset

        Administrative command that will call the reset interrupt
        vector on the uController. User will need to call connect()
        after calling this.
        """
        self.last_result = self._bstimulator_obj.reset_stimulator()
        self._raise_if_error("reset_stimulator")

    # protected methods
    def _raise_if_error(self, context: str) -> None:
        """Raise last error, if any"""
        if self.last_result != _bstimulator.success:
            last_err = self.last_result
            err_doc = get_enum_docstr(last_err)
            error_str = f"{last_err.name.upper()} error in {context}():\n {err_doc}"
            # TODO create more specific error types
            raise RuntimeError(error_str)

    @staticmethod
    def _convert_raw_version(raw_version: int) -> dict:
        version = {"major": (raw_version >> 8) & 0xFF, "minor": raw_version & 0xFF}
        return version

    @staticmethod
    def _convert_raw_serial_num(raw_serial: int) -> dict:
        serial = {
            "part": PartNumbers((raw_serial >> 24) & 0xFF),
            "serial_no": raw_serial & 0xFFFF,
        }
        return serial

    @staticmethod
    def _convert_raw_min_max_amp(raw_amp: int) -> dict:
        amp_limits = {"min_amp": raw_amp & 0xFFFF, "max_amp": (raw_amp >> 16) & 0xFFFF}
        return amp_limits

    def __del__(self) -> None:
        """Stimulator destructor

        Decrements _stimulator_count
        """
        Stimulator._stimulator_count -= 1


# end class Stimulator
