# Author: Jeff Weiss <jeff.weiss@pitt.edu>
# May 2022

"""stimpy: a python package to interface with Blackrock Cerestim API."""

from code import interact
import _bstimulator
from typing import List, Optional, Any

SUCCESS: _bstimulator.result = _bstimulator.success
MAX_CHANNELS: int = (
    _bstimulator.max_channels - 1
)  # the API constant also includes internal channel 0
MAX_CONFIGURATIONS: int = _bstimulator.max_configurations
MAX_MODULES: int = _bstimulator.max_modules
BANK_SIZE: int = _bstimulator.bank_size
MAX_STIMULATORS: int = 12 # subject to change, this is not from public BStimulator.h header


def get_enum_docstr(enum_val: Any) -> str:
    """Lookup docstr for a pybind11 enum value and output as string"""
    enum_entries = enum_val.__entries
    doc_str = enum_entries[enum_val.name][1]
    return doc_str


class stimulator(object):
    """Simple python interface to Blackrock Cerestim 96"""

    device_vector: Optional[List[int]] = None
    oc_volt = _bstimulator.oc_volt  # enum class for compliance voltage
    wf_types = _bstimulator.wf_type  # enum class for anodal or cathodal first
    _stimulator_count: int = 0

    def __init__(self) -> None:
        """Stimulator constructor"""
        stimulator._stimulator_count += 1
        if stimulator._stimulator_count > MAX_STIMULATORS:
            raise RuntimeError("Max stimulator error")

        self._bstimulator_obj: _bstimulator.stimulator = (
            _bstimulator.stimulator()
        )  # raw stimulator object
        self.device_index: Optional[List[int]] = None
        self.last_result: _bstimulator.result = SUCCESS

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
        """
        Scan for connected cerestim devices, returns a list of serial numbers.

        If only one Cerestim device is attached to PC, you can skip this step
        and just call connect().
        """
        cls.device_vector = list(_bstimulator.stimulator.scan_for_devices())
        return cls.device_vector

    @staticmethod
    def validate_electrode(electrode: int) -> None:
        if electrode < 1 or electrode > MAX_CHANNELS:
            raise ValueError("Invalid electrode")

    @staticmethod
    def validate_configID(configID: int) -> None:
        if configID < 1 or configID > MAX_CONFIGURATIONS:
            raise ValueError("Invalid pattern config ID")

    @staticmethod
    def validate_module(module: int) -> None:
        if module < 0 or module > MAX_MODULES:
            raise ValueError("Invalid module index")

    @staticmethod
    def validate_pulses(pulses: int) -> None:
        if pulses < 1 or pulses > 255:
            raise ValueError("Invalid pulse number")

    @staticmethod
    def validate_amp(amp: int) -> None:
        # TODO determine if micro or macro, for now assume micro
        if amp < 1 or amp > 215:  # micro
            # if amp < 100 or amp > 10000:
            raise ValueError("Invalid pulse amplitude")

    @staticmethod
    def validate_width(width: int) -> None:
        if width < 1 or width > 65535:
            raise ValueError("Invalid pulse width")

    @staticmethod
    def validate_frequency(freq: int) -> None:
        if freq < 4 or freq > 5000:
            raise ValueError("Invalid frequency")

    @staticmethod
    def validate_interphase(interphase: int) -> None:
        if interphase < 53 or interphase > 65535:
            raise ValueError("Invalid interphase")

    def connect(self, device_index: int = 0) -> None:
        """
        Connect to Cerestim.

        If multiple devices are attached to PC, first call scan_for_devices
        to view the list of serial numbers, then input the device_index you
        would like to connect to.
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
        """Disconnect from cerestim"""
        self.last_result = self._bstimulator_obj.disconnect()
        self._raise_if_error("disconnect")

    def lib_version(self) -> _bstimulator.version:
        """Get API library version"""
        version_struct = _bstimulator.version()
        self.last_result = self._bstimulator_obj.lib_version(version_struct)
        self._raise_if_error("lib_version")
        return version_struct

    def manual_stimulus(self, electrode: int, configID: int) -> None:
        """
        Allows the user to send a single stimulus pulse of one of the
        stimulation waveforms to a specified electrode."

        electrode: The electrode that should be stimulated.
            Valid values are from 1 - 96.
        configID: The stimulation waveform to use.
            Valid values are from 1 - 15.
        """
        self.validate_electrode(electrode)
        self.validate_configID(configID)

        self.last_result = self._bstimulator_obj.manual_stimulus(
            electrode, _bstimulator.config(configID)
        )
        self._raise_if_error("manual_stimulus")

    def begin_sequence(self) -> None:
        """
        This is the first command that must be called when creating a
        stimulation script. After calling this you are able to call wait(),
        auto_stimulus(), begin_group(), and end_group() commands. The
        stimulation script can have up to 128 commands, excluding
        begin_sequence() and end_sequence()
        """
        self.last_result = self._bstimulator_obj.beginning_of_sequence()
        self._raise_if_error("begin_sequence")

    def end_sequence(self) -> None:
        """
        This is the last command that must be called when creating a
        stimulation script. It does not count towards the maximum of 128
        commands.
        """
        self.last_result = self._bstimulator_obj.end_of_sequence()
        self._raise_if_error("end_sequence")

    def begin_group(self) -> None:
        """
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
        """
        This command closes off a group of simultaneous stimulations.
        If begin_group() is called during a sequence of commands, then
        there must be an end_group() otherwise the user will get a
        sequence error as a return value.
        """
        self.last_result = self._bstimulator_obj.end_of_group()
        self._raise_if_error("end_group")

    def auto_stimulus(self, electrode: int, configID: int) -> None:
        """
        This command tells the stimulator when to send a stimulus to an
        electrode in a stimulation script. It can be used as many times
        as needed so long as the total number of commands does not exceed
        128. It should also be used within begin_group() and end_group()
        commands to allow for simultaneous stimulations.

        electrode: The electrode that will be stimulated.
            Valid values are from 1 - 96
        configID: One of the fifteen stimulation waveforms that should be used.
            Valid values are from 1-15
        """
        self.validate_electrode(electrode)
        self.validate_configID(configID)
        self.last_result = self._bstimulator_obj.auto_stimulus(
            electrode, _bstimulator.config(configID)
        )
        self._raise_if_error("auto_stimulus")

    def wait(self, milliseconds: int) -> None:
        """
        This command can only be used within a stimulation script and
        is capable of adding a wait of up to 65,535 milliseconds.

        milliseconds: The number of milliseconds to wait before
            executing the next command
        """
        if milliseconds < 0 or milliseconds > 65535:
            raise ValueError("milliseconds out of range (0,65535)")
        self.last_result = self._bstimulator_obj.wait(milliseconds)
        self._raise_if_error("wait")

    def play(self, times: int) -> None:
        """
        Tells the stimulator the number of times that it should run the
        stimulation script. A zero passed in will tell it to run
        indefinitely until it is either stopped or paused by the user.
        Other values include between 1 and 65,535 repetitions. Cannot
        be called during a begin_sequence() and end_sequence() command call.

        times: Number of times to execute the stimulation script. 0 means indefinitely.
        """
        if times < 0 or 65535:
            raise ValueError("times out of range (0,65535)")
        self.last_result = self._bstimulator_obj.play(times)
        self._raise_if_error("play")

    def stop(self) -> None:
        """
        This will stop a currently running stimulation script and reset
        it so when played again it will begin from the first command.
        Can only be called while the stimulator has a status of
        stimulating or paused.
        """
        self.last_result = self._bstimulator_obj.stop()
        self._raise_if_error("stop")

    def pause(self) -> None:
        """
        This will pause a currently running stimulation script and keep
        track of the next command that needs to be executed so if it
        receives a play command it can pick up where it left off.
        """
        self.last_result = self._bstimulator_obj.pause()
        self._raise_if_error("pause")

    def read_max_output_voltage(self) -> int:
        """
        This will read the values of +VDD and -VSS on the stimulator
        which allows it to effectively limit the maximum output voltage
        that can be delivered during a stimulation. If the output current
        times the impedance of the electrode is greater than the max
        compliance voltage then it means the full current is not being
        delivered to the electrode because it can not drive any more current.

        returns the max output voltage in millivolts
        """
        output = _bstimulator.max_output_voltage
        rw = 0  # read
        v = _bstimulator.ocvolt_invalid
        self.last_result = self._bstimulator_obj.max_output_voltage(output, rw, v)
        self._raise_if_error("max_output_voltage")
        return output.miliVolts

    def set_max_output_voltage(self, oc_voltage: oc_volt) -> int:
        """
        This will set the values of +VDD and -VSS on the stimulator
        which allows it to effectively limit the maximum output voltage
        that can be delivered during a stimulation. If the output
        current times the impedance of the electrode is greater than the
        max compliance voltage then it means the full current is not
        being delivered to the electrode because it can not drive any
        more current.

        oc_voltage: The voltage level that is being set.
            Must be an oc_volt enum value.
        returns the max output voltage in millivolts.

        """
        output = _bstimulator.max_output_voltage
        rw = 1  # write
        self.last_result = self._bstimulator_obj.max_output_voltage(
            output, rw, oc_voltage
        )
        self._raise_if_error("max_output_voltage")
        return output.miliVolts

    def read_device_info(self) -> _bstimulator.device_info:
        """
        This returns all the information about the CereStim 96 that is
        connected to. It will tell its part number, serial number,
        firmware versions for both the motherboard and for the current
        modules. It will also tell you the protocol that the motherboard
        is using with the current modules and the number of installed
        current modules.

        "Returns a device_info structure, the structure will be populated
            with the CereStim's information
        """
        # TODO parse this structure so everything is human readable
        output = _bstimulator.device_info()
        self.last_result = self._bstimulator_obj.read_device_info(output)
        self.raise_if_error("read_device_info")
        return output

    def enable_module(self, module: int) -> None:
        """
        Allows the user to enable different current modules that have
        been disabled. This is useful for testing and making sure that
        multiple current modules are all giving the same output values.

        module: The current module to be enabled from 0 to 15
        """
        self.validate_module(module)
        self.last_result = self._bstimulator_obj.enable_module(module)
        self.raise_if_error("enable_module")

    def disable_module(self, module: int) -> None:
        """
        Allows the user to disable different current modules that are
        installed in the CereStim. This is useful for testing and making
        sure that multiple current modules are all giving the same output
        values. The current module has to exist to be disabled.

        module: The current module to be disabled from 0 to 15
        """
        self.validate_module(module)
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
        """
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

        configID: The stimulation waveform that is being configured
            1 - 15
        afcf: What polarity should the first phase be,
            Anodic or Cathodic first
        pulses: The number of stimulation pulses in waveform from
            1 - 255
        amp1: The amplitude of the first phase, for Micro it is
            1 - 215 uA, and for Macro it is 100 uA - 10 mA
        amp2: The amplitude of the first phase, for Micro it is
            1 - 215 uA, and for Macro it is 100 uA - 10 mA
        width1: The width of the first phase in the stimulation
            1 - 65,535 uS
        width2: The width of the second phase in the stimulation
            1 - 65,535 uS
        frequency: The stimulating frequency at which the biphasic
            pulses should repeat 4 - 5000 Hz
        interphase: The period of time between the first and second
            phases 53 - 65,535 uS
        """
        self.validate_configID(configID)
        self.validate_pulses(pulses)
        self.validate_amp(amp1)
        self.validate_amp(amp2)
        self.validate_width(width1)
        self.validate_width(width2)
        self.validate_frequency(frequency)
        self.validate_interphase(interphase)
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

    def read_stimulus_pattern():
        pass

    def read_sequence_status():
        pass

    def read_stimulus_max_values():
        pass

    def set_stimulus_max_values():
        pass

    def group_stimulus():
        pass

    def trigger_stimulus():
        pass

    def stop_trigger_stimulus():
        pass

    def update_electrode_channel_map():
        pass

    def read_hardware_values():
        pass

    def disable_stimulus_configuration():
        pass

    def reset_stimulator():
        pass

    def is_conected():
        pass

    def get_serial_number():
        pass

    def get_motherboard_firmware_version():
        pass

    def get_protocol_version():
        pass

    def git_min_max_amplitude():
        pass

    def get_module_firmware_version():
        pass

    def get_module_status():
        pass

    def get_usb_address():
        pass

    def get_max_hard_charge():
        pass

    def get_min_hard_frequency():
        pass

    def get_max_hard_frequency():
        pass

    def get_number_modules():
        pass

    def get_max_hard_width():
        pass

    def get_max_hard_interphase():
        pass

    def is_safety_disabled():
        pass

    def is_device_locked():
        pass