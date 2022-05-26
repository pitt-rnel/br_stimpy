# Author: Jeff Weiss <jeff.weiss@pitt.edu>
# May 2022

"""stimpy: a python package to interface with Blackrock Cerestim API."""

from __future__ import annotations  # ensure forward compatibility
import _bstimulator
from typing import List, Optional, Any

SUCCESS: _bstimulator.result = _bstimulator.success
MAX_CHANNELS: int = (
    _bstimulator.max_channels - 1
)  # the API constant also includes internal channel 0
MAX_CONFIGURATIONS: int = _bstimulator.max_configurations
MAX_MODULES: int = _bstimulator.max_modules
BANK_SIZE: int = _bstimulator.bank_size
MAX_STIMULATORS: int = (
    12  # subject to change, this is not from public BStimulator.h header
)

# add references to enums and other classes from _bstimulator
oc_volt = _bstimulator.oc_volt  # enum class for compliance voltage
wf_types = _bstimulator.wf_type  # enum class for anodal or cathodal first
trigger_type = _bstimulator.trigger_type
electrode_channel_map = _bstimulator.electrode_channel_map
part_numbers = _bstimulator.part_numbers
module_status = _bstimulator.module_status
seq_type = _bstimulator.seq_type
module_status = _bstimulator.module_status
result_types = _bstimulator.result


def get_enum_docstr(enum_val: Any) -> str:
    """Lookup docstr for a pybind11 enum value and output as string

    Args:
        enum_val: an enumeration value from the _bstimulator module

    Returns:
        str: docstr for the enum_val
    """
    enum_entries = enum_val.__entries
    doc_str = enum_entries[enum_val.name][1]
    return doc_str


class validation_fcns:
    """Validation functions for internal use within this module"""

    @staticmethod
    def _validate_electrode(electrode: int) -> None:
        if electrode < 1 or electrode > MAX_CHANNELS:
            raise ValueError("Invalid electrode")

    @staticmethod
    def _validate_configID(configID: int) -> None:
        if configID < 1 or configID > MAX_CONFIGURATIONS:
            raise ValueError("Invalid pattern config ID")

    @staticmethod
    def _validate_module(module: int) -> None:
        if module < 0 or module > MAX_MODULES:
            raise ValueError("Invalid module index")

    @staticmethod
    def _validate_pulses(pulses: int) -> None:
        if pulses < 1 or pulses > 255:
            raise ValueError("Invalid pulse number")

    @staticmethod
    def _validate_amp(amp: int) -> None:
        # TODO determine if micro or macro, for now assume micro
        if amp < 1 or amp > 215:  # micro
            # if amp < 100 or amp > 10000:
            raise ValueError("Invalid pulse amplitude")

    @staticmethod
    def _validate_width(width: int) -> None:
        if width < 1 or width > 65535:
            raise ValueError("Invalid pulse width")

    @staticmethod
    def _validate_frequency(freq: int) -> None:
        if freq < 4 or freq > 5000:
            raise ValueError("Invalid frequency")

    @staticmethod
    def _validate_interphase(interphase: int) -> None:
        if interphase < 53 or interphase > 65535:
            raise ValueError("Invalid interphase")


class group_stimlus_struct(object):
    """Group Stimulus Structure

    Structure to input to stimulator.group_stimulus() function.

    Optionally accepts electrode and pattern ID lists as input.
    Constructor will check that electrode and pattern IDs are valid and
    not longer than MAX_MODULES. Will zero-pad lists to length
    MAX_MODULES. User must not modify these lengths before calling
    stimulator.group_stimulus()
    """

    def __init__(
        self, electrode: Optional[List[int]] = None, pattern: Optional[List[int]] = None
    ) -> None:
        """
        group_stimulus_struct constructor

        Args:
            electrode (Optional[List[int]], optional):
                List of electrodes to stimulate on, up to length
                MAX_MODULES. Defaults to None.
            pattern (Optional[List[int]], optional):
                List of pattern config IDs to match to electrodes above.
                Must be same length as electrode list. Defaults to None.

        Raises:
            ValueError: Electrode and Pattern lists must be the same length and cannot be longer than MAX_MODULES.
        """
        if electrode:
            num_elec = len(electrode)
        else:
            num_elec = 0

        if pattern:
            num_pat = len(pattern)
        else:
            num_pat = 0

        if num_elec > MAX_MODULES or num_pat > MAX_MODULES:
            raise ValueError(
                f"Cannot simultaneously stimulate on more than {MAX_MODULES} electrodes."
            )

        if num_elec != num_pat:
            raise ValueError(f"Electrode and Pattern lists must be the same length")

        for idx in range(0, num_elec):
            self.validate_electrode(electrode[idx])
            self.validate_pattern(pattern[idx])

        if num_elec:
            self.electrode = electrode
            self.pattern = pattern
            if num_elec < MAX_MODULES:
                ext_len = MAX_MODULES - num_elec
                self.electrode.extend([0] * ext_len)
                self.pattern.extend([0] * num_elec)
        else:
            self.electrode = [0] * MAX_MODULES
            self.pattern = [0] * MAX_MODULES


class stimulator(object):
    """Simple python interface to Blackrock Cerestim 96"""

    device_vector: Optional[List[int]] = None
    _stimulator_count: int = 0

    # repeat _bstimulator references here (user can access from either module or class)
    oc_volt = oc_volt  # enum class for compliance voltage
    wf_types = wf_types  # enum class for anodal or cathodal first
    trigger_type = trigger_type
    electrode_channel_map = electrode_channel_map
    part_numbers = part_numbers
    module_status = module_status
    seq_type = seq_type

    def __init__(self) -> None:
        """Stimulator constructor

        Raises:
            RuntimeError: Only 12 stimulator objects can be created at a time
        """
        stimulator._stimulator_count += 1
        if stimulator._stimulator_count > MAX_STIMULATORS:
            raise RuntimeError("Max stimulator error")

        self._bstimulator_obj: _bstimulator.stimulator = (
            _bstimulator.stimulator()
        )  # raw stimulator object
        self.device_index: Optional[List[int]] = None
        self.last_result: result_types = SUCCESS

    def __del__(self) -> None:
        """Stimulator destructor

        Decrements _stimulator_count
        """
        stimulator._stimulator_count -= 1

    def _is_success(self) -> bool:
        """Evaluate if last stim API result was successful"""
        return self.last_result == SUCCESS

    def _raise_if_error(self, context: str) -> None:
        """Raise last error, if any"""
        if not self._is_success():
            last_err = self.last_result
            err_doc = get_enum_docstr(last_err)
            error_str = f"{last_err.name.upper()} error in {context}():\n {err_doc}"
            raise RuntimeError(error_str)

    @classmethod
    def scan_for_devices(cls) -> List[int]:
        """Scan for connected Cerestim devices

        If only one Cerestim device is attached to PC, you can skip this step
        and just call connect().

        Returns:
            List[int]: list of serial numbers of the connected Cerestims
        """
        cls.device_vector = list(_bstimulator.stimulator.scan_for_devices())
        return cls.device_vector

    def connect(self, device_index: int = 0) -> None:
        """Connect to Cerestim.

        If multiple devices are attached to PC, first call scan_for_devices
        to view the list of serial numbers, then input the device_index you
        would like to connect to.

        Args:
            device_index (int, optional): Index of device from scan_for_devices.
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

    def disconnect(self) -> None:
        """Disconnect from Cerestim"""
        self.last_result = self._bstimulator_obj.disconnect()
        self._raise_if_error("disconnect")

    def lib_version(self) -> _bstimulator.version:
        """Get API library version

        Returns:
            _bstimulator.version: structure containing version
        """
        version_struct = _bstimulator.version()
        self.last_result = self._bstimulator_obj.lib_version(version_struct)
        self._raise_if_error("lib_version")
        return version_struct

    def manual_stimulus(self, electrode: int, configID: int) -> None:
        """Manually stimulate on one electrode

        Allows the user to send a single stimulus pulse of one of the
        stimulation waveforms to a specified electrode.

        Args:
            electrode (int): The electrode that should be stimulated.
                Valid values are from 1 - 96.
            configID (int): The stimulation waveform to use.
                Valid values are from 1 - 15.
        """
        validation_fcns._validate_electrode(electrode)
        validation_fcns._validate_configID(configID)

        self.last_result = self._bstimulator_obj.manual_stimulus(
            electrode, _bstimulator.config(configID)
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
            electrode (int): The electrode that will be stimulated.
                Valid values are from 1 - 96
            configID (int): One of the fifteen stimulation waveforms that should be used.
                Valid values are from 1-15
        """
        validation_fcns._validate_electrode(electrode)
        validation_fcns._validate_configID(configID)
        self.last_result = self._bstimulator_obj.auto_stimulus(
            electrode, _bstimulator.config(configID)
        )
        self._raise_if_error("auto_stimulus")

    def wait(self, milliseconds: int) -> None:
        """Wait between stim pulses

        This command can only be used within a stimulation script and
        is capable of adding a wait of up to 65,535 milliseconds.

        Args:
            milliseconds (int): The number of milliseconds to wait before
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
            times (int): Number of times to execute the stimulation script.
            0 means indefinitely.

        Raises:
            ValueError: times must be between 0 and 65535.
        """
        if times < 0 or 65535:
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
            int: the max output voltage in millivolts
        """
        output = _bstimulator.max_output_voltage()
        rw = 0  # read
        v = _bstimulator.ocvolt_invalid
        self.last_result = self._bstimulator_obj.max_output_voltage(output, rw, v)
        self._raise_if_error("max_output_voltage")
        return output.miliVolts

    def set_max_output_voltage(self, oc_voltage: oc_volt) -> int:
        """Set compliance voltage

        This will set the values of +VDD and -VSS on the stimulator
        which allows it to effectively limit the maximum output voltage
        that can be delivered during a stimulation. If the output
        current times the impedance of the electrode is greater than the
        max compliance voltage then it means the full current is not
        being delivered to the electrode because it can not drive any
        more current.

        Args:
            oc_voltage (stimulator.oc_volt): The voltage level that is
                being set. Must be an oc_volt enum value.

        Returns:
            int: the max output voltage in millivolts.
        """
        output = _bstimulator.max_output_voltage()
        rw = 1  # write
        self.last_result = self._bstimulator_obj.max_output_voltage(
            output, rw, oc_voltage
        )
        self._raise_if_error("max_output_voltage")
        return output.miliVolts

    def read_device_info(self) -> dict:
        """Read device hardware and firmware info

        This returns all the information about the CereStim 96 that is
        connected to. It will tell its part number, serial number,
        firmware versions for both the motherboard and for the current
        modules. It will also tell you the protocol that the motherboard
        is using with the current modules and the number of installed
        current modules.

        Returns:
            dict: a dictionary populated with the CereStim's information
        """
        dev_info = _bstimulator.device_info()
        self.last_result = self._bstimulator_obj.read_device_info(dev_info)
        self.raise_if_error("read_device_info")
        output = dict = {
            "serial_no": hex(dev_info.serialNo),
            "mainboard_version": hex(dev_info.mainboardVersion),
            "protcol_version": hex(dev_info.protocol_version),
            "module_status": [module_status(x) for x in dev_info.moduleStatus],
            "module_version": [hex(x) for x in dev_info.moduleVersion],
        }
        return output

    def enable_module(self, module: int) -> None:
        """Enable current module

        Allows the user to enable different current modules that have
        been disabled. This is useful for testing and making sure that
        multiple current modules are all giving the same output values.

        Args:
            module (int): The current module to be enabled from 0 to 15
        """
        validation_fcns._validate_module(module)
        self.last_result = self._bstimulator_obj.enable_module(module)
        self.raise_if_error("enable_module")

    def disable_module(self, module: int) -> None:
        """Disable current module

        Allows the user to disable different current modules that are
        installed in the CereStim. This is useful for testing and making
        sure that multiple current modules are all giving the same output
        values. The current module has to exist to be disabled.

        Args:
            module (int):The current module to be disabled from 0 to 15
        """
        validation_fcns._validate_module(module)
        self.last_result = self._bstimulator_obj.disable_module(module)
        self.raise_if_error("enable_module")

    def configure_stimulus_pattern(
        self,
        configID: int,
        afcf: wf_types,
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
            configID (int): The stimulation waveform that is being
                configured 1 - 15
            afcf (stimulator.wf_types): What polarity should the first
                phase be, Anodic or Cathodic first
            pulses (int): The number of stimulation pulses in waveform
                from 1 - 255
            amp1 (int): The amplitude of the first phase, for Micro it
                is 1 - 215 uA, and for Macro it is 100 uA - 10 mA
            amp2 (int): The amplitude of the first phase, for Micro it
                is 1 - 215 uA, and for Macro it is 100 uA - 10 mA
            width1 (int): The width of the first phase in the stimulation
                1 - 65,535 uS
            width2 (int): The width of the second phase in the stimulation
                1 - 65,535 uS
            frequency (int): The stimulating frequency at which the
                biphasic pulses should repeat 4 - 5000 Hz
            interphase (int): The period of time between the first and
                second phases 53 - 65,535 uS
        """
        validation_fcns._validate_configID(configID)
        validation_fcns._validate_pulses(pulses)
        validation_fcns._validate_amp(amp1)
        validation_fcns._validate_amp(amp2)
        validation_fcns._validate_width(width1)
        validation_fcns._validate_width(width2)
        validation_fcns._validate_frequency(frequency)
        validation_fcns._validate_interphase(interphase)
        self.last_result = self._bstimulator_obj.configure_stimulus_pattern(
            _bstimulator.config(configID),
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

    def read_stimulus_pattern(
        self, configID: int
    ) -> _bstimulator.stimulus_configuration:
        """Read stim config pattern

        Reads back all of the parameters associated with a specific
        stimulation waveform and stores it in the structure supplied by
        the user.

        Args:
            configID (int): The stimulation waveform that is being read back

        Returns:
            _bstimulator.stimulus_configuration: structure which contains
                all the parameters that consist in a stimulation waveform
        """
        validation_fcns._validate_configID(configID)
        output = _bstimulator.stimulus_configuration()
        self.last_result = self._bstimulator_obj.read_stimulus_pattern(output, configID)
        self._raise_if_error("read_stimulus_pattern")
        return output

    def read_sequence_status(self) -> seq_type:
        """Get stim sequence status

        Can be called anytime as it does not interrupt other functions
        from executing, but simply reads what state the stimulator is in.

        Returns:
            seq_type: Enum containing the sequence state
        """
        output = _bstimulator.sequence_status()
        self.last_result = self._bstimulator_obj.read_sequence_status(output)
        self._raise_if_error("read_sequence_status")
        return seq_type(output.status)

    def read_stimulus_max_values(self) -> _bstimulator.maximum_values:
        """Read maximum stimulus values set using set_stimulus_max_values()

        Returns:
            _bstimulator.maximum_values: structure that will contain the current max values that are set
        """
        output = _bstimulator.maximum_values()
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
        self, voltage: oc_volt, amplitude: int, phaseCharge: int, frequency: int
    ) -> _bstimulator.maximum_values:
        """Set max limits

        Intended to be an administrative interface that can be password
        protected and only allow the lead researcher to make changes.
        It allows the user to set other determined upper limits for the
        stimulation parameters for whatever safety protocol they are
        requiring. Again micro and macro stimulators will have some
        different bounds for setting max values due to the different
        ranges each are able to achieve.

        Args:
            voltage (oc_volt): The Max Compliance Voltage that can be set
            amplitude (int): The Max amplitude that can be used in a stimulation
            phaseCharge (int): The Max charge per phase that will be allowed (Charge = Amplitude * Width)
            frequency (int): The Max frequency at which the stimulations can take place

        Returns:
            _bstimulator.maximum_values: structure that will contain the current max values that are set
        """
        output = _bstimulator.maximum_values()
        rw = 1
        self.last_result = self._bstimulator_obj.stimulus_max_values(
            output, rw, voltage, amplitude, phaseCharge, frequency
        )
        self._raise_if_error("stimulus_max_values")
        return output

    def group_stimulus(
        self,
        begin_seq: int,
        play: int,
        times: int,
        number: int,
        group_stim_struct: group_stimlus_struct,
    ) -> None:
        """Send group stimulus command

        There is a lot of overhead in sending commands over the USB to
        the CereStim 96. each function call averages 2mS. This function
        allows the user to create the stimulation parameters beforehand
        and in a single function call perform simultaneous stimulations
        based on different electrodes and configured waveforms.

        Args:
            begin_seq (int): Boolean expression to tell the function
                that it is the beginning of a sequence
            play (int): Boolean expression to tell if the stimulator
                should begin stimulating immedieatly after this call
            times (int): The number of times to play the stimulation,
                is ignored if play = false
            number (int): The number of stimulus that will occur
                simultaneously.
            group_stim_struct (group_stimlus_struct): structure which
                has a pair of arrays with electrodes and waveforms
        """
        self.last_result = self._bstimulator_obj.group_stimulus(
            begin_seq, play, times, number, group_stim_struct
        )
        self._raise_if_error("group_stimulus")

    def trigger_stimulus(self, edge: trigger_type) -> None:
        """Start trigger mode

        Allows the stimulator to wait for a trigger event before
        executing a stimulation script. The stimulator has an external
        TTL Trigger input port that uses TTL logic levels to determine
        whether the input is high or low. The stimulator can be set to
        fire on a rising edge, falling edge, or any edge transition.
        Once in trigger mode the stimulator is locked down from other
        function calls except for stop_trigger_stimulus()

        Args:
            edge (trigger_type): The type of digital event to trigger the stimulation on
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

    def update_electrode_channel_map(self, map: electrode_channel_map) -> None:
        """Set electrode map

        Since not all electrodes are found on channel 1 this function
        allows the user to create a map key pair where the channel is
        an index into an array which holds the value of the electrode
        at that channel.

        Args:
            map (electrode_channel_map):channel map structure
        """
        self.last_result = self._bstimulator_obj.update_electrode_channel_map(map)
        self._raise_if_error("update_electrode_channel_map")

    def read_hardware_values(self) -> _bstimulator.read_hardware_values_output:
        """Reads the hardware values that are set based on the part number

        Returns:
            _bstimulator.read_hardware_values_output: Structure containing the hardware values
        """
        output = _bstimulator.read_hardware_values_output()
        self.last_result = self._bstimulator_obj.read_hardware_values(output)
        self._raise_if_error("read_hardware_values")
        return output

    def disable_stimulus_configuration(self, configID: int) -> None:
        """Disables a stimulation waveform so that it is able to be reset

        Args:
            configID (int): The configuration to disable
        """
        validation_fcns._validate_configID(configID)
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

    def is_conected(self) -> bool:
        """Check if stimulator is connected

        Lets the user know that the stimulator object is connected to a
        physical CereStim 96 device.

        Returns:
            bool: True if stimulator is connected
        """
        return bool(self._bstimulator_obj.is_connected())

    def get_serial_number(self) -> str:
        """Get device serial number

        Retrieves the serial number that is programmed into the
        CereStim 96 device that is attached. The format of the 32 bit
        serial number is as follows 0xPPXXSSSS, where PP is the part
        number, XX is ignored, and SSSS is the serial number. The part
        number is a part_numbers enumeration.

        Returns:
            str: Part Number and Serial number of the CereStim 96 as hex string
        """
        # hex string from serial number TODO do something better to handle part number and serial number
        return hex(self._bstimulator_obj.get_serial_number())

    def get_motherboard_firmware_version(self) -> str:
        """Get main firmware version

        Retrieves the firmware revision of the microcontroller on the
        motherboard. The MSB is the Major revision number and the LSB
        is the minor revision number. I.e. 0x0500 would be version 5.0

        Returns:
            str: Firmware Version of the Motherboard as a hex string
        """
        return hex(self._bstimulator_obj.get_motherboard_firmware_version())

    def get_protocol_version(self) -> str:
        """Get motherboard protocol version

        The protocol version that the motherboard uses to send and
        receive data from the current modules. The MSB is the Major
        revision number and the LSB is the minor revision number. I.e.
        0x0105 would be version 1.5

        Returns:
            str: Protocol Version of the Motherboard as a hex string
        """
        return hex(self._bstimulator_obj.get_protocol_version())

    def get_min_max_amplitude(self) -> str:
        """Get hardware min and max amplitudes

        Since there are different models and version of the stimulator,
        such as the micro and macro versions, this will allow the user
        to get the min and max amplitudes that are allowed for
        stimulation. The upper two MSB are the maximum amplitude while
        the lower two LSB are the minimum amplitude.

        Returns:
            str: Min and Max Amplitude in hex string
        """
        return hex(self._bstimulator_obj.get_min_max_amplitude())

    def get_module_firmware_version(self) -> List[str]:
        """Get firmware versions of current modules

        Each current module has its own microcontroller and has a
        firmware version. All current modules in a single stimulator
        should have the same firmware version. The MSB is the Major
        revision number and the LSB is the minor revision number. I.e.
        0x0105 would be version 1.5

        Returns:
            List[str]: List of module firmware versions as hex strings
        """
        # TODO this will certainly require testing
        output = _bstimulator.vector_UINT16([])
        self.last_result = self._bstimulator_obj.get_module_firmware_version(output)
        self._raise_if_error("get_module_firmware_version")
        return [hex(x) for x in output]

    def get_module_status(self) -> List[module_status]:
        """Get status of each current module

        This tells the status of each current module, whether it is
        enabled, disabled, or not available.

        Returns:
            List[module_status]: List of the possible 16 current modules status
        """
        output = _bstimulator.vector_UINT8([])
        self.last_result = self._bstimulator_obj.get_module_status(output)
        self._raise_if_error("get_module_status")
        return [module_status(x) for x in output]

    def get_usb_address(self) -> int:
        """Gets the USB address of the connected stimulator

        Returns:
            int: USB address
        """
        return self._bstimulator_obj.get_usb_address()

    def get_max_hard_charge(self) -> int:
        """Get hardware max charge per phase

        This value is based on the hardware of the particuliar model of
        the CereStim 96. Again the micro and macro versions of the
        stimulator have different values

        Returns:
            int: Max charge per phase
        """
        return self._bstimulator_obj.get_max_hard_charge()

    def get_min_hard_frequency(self) -> int:
        """Get hardware minimum frequency

        This value is based on the hardware of the particuliar model of
        the CereStim 96. Again the micro and macro versions of the
        stimulator have different values

        Returns:
            int: Minimum Stimulating Frequency in Hz
        """
        return self._bstimulator_obj.get_max_hard_charge()

    def get_max_hard_frequency(self) -> int:
        """Get hardware maximum frequency

        This value is based on the hardware of the particuliar model of
        the CereStim 96. Again the micro and macro versions of the
        stimulator have different values

        Returns:
            int: Maximum Stimulating Frequency in Hz
        """
        return self._bstimulator_obj.get_max_hard_charge()

    def get_number_modules(self) -> int:
        """Get number of current modules installed

        This value is based on the hardware of the particuliar model of
        the CereStim 96. Again the micro and macro versions of the
        stimulator have different values

        Returns:
            int: Number of Modules installed
        """
        return self._bstimulator_obj.get_max_hard_charge()

    def get_max_hard_width(self) -> int:
        """Get hardware maximum pulse width

        This value is based on the hardware of the particuliar model of
        the CereStim 96.

        Returns:
            int: Maximum width of each phase in us
        """
        return self._bstimulator_obj.get_max_hard_charge()

    def get_max_hard_interphase(self) -> int:
        """Get hardware maximum interphase width

        This value is based on the hardware of the particuliar model of
        the CereStim 96

        Returns:
            int: Maximum interphase width in us
        """
        return self._bstimulator_obj.get_max_hard_charge()

    def is_safety_disabled(self) -> bool:
        """Check if safety limits are disabled

        For Internal validation and testing it is required to disable
        the safety limits in the firmware and API so that hardware
        limits can be observed and tested.

        Returns:
            bool: True if disabled False otherwise
        """
        return bool(self._bstimulator_obj.get_max_hard_charge())

    def is_device_locked(self) -> bool:
        """Check if stimulator is locked

        If the detected number of current modules doesn't match the
        hardware configuration or if the hardware configuration is not
        setup, the device will be locked down preventing any stimulation
        from occuring.

        Returns:
            bool: True if locked False otherwise
        """
        return bool(self._bstimulator_obj.get_max_hard_charge())
