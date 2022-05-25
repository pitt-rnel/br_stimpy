# Author: Jeff Weiss <jeff.weiss@pitt.edu>
# May 2022

"""stimpy: a python package to interface with Blackrock Cerestim API."""

import _bstimulator
from typing import List, Optional

SUCCESS: _bstimulator.result = _bstimulator.success
MAX_CHANNELS: int = (
    _bstimulator.max_channels - 1
)  # the API constant also includes internal channel 0
MAX_CONFIGURATIONS: int = _bstimulator.max_configurations


class stimulator(object):
    """Simple python interface to Blackrock Cerestim 96"""

    device_vector: Optional[List[int]] = None

    def __init__(self) -> None:
        """Stimulator constructor"""
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
        if not self._is_success:
            # values in range(-24,1) are software errors (or success)
            # values in range(-132,-100) are hardware errors 
            if self.last_result.value > -100:
                err_type = 'software'
            else:
                err_type = 'hardware'
            error_str = f"{context} {err_type} error: {self.last_result.name}"
            raise RuntimeError(error_str)

    @classmethod
    def scan_for_devices(cls) -> List[int]:
        """
        Scan for connected cerestim devices, returns a list of serial numbers.

        If only one Cerestim device is attached to PC, you can skip this step and just call connect().
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

    def connect(self, device_index: int = 0) -> None:
        """
        Connect to Cerestim.

        If multiple devices are attached to PC, first call scan_for_devices to view the list of serial numbers,
        then input the device_index you would like to connect to.
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
        Allows the user to send a single stimulus pulse of one of the stimulation waveforms to a specified electrode.\n\n"

        electrode: The electrode that should be stimulated. Valid values are from 1 - 96
        configID: The stimulation waveform to use. Valid values are from 1 - 15
        """
        self.validate_electrode(electrode)
        self.validate_configID(configID)

        self.last_result = self._bstimulator_obj.manual_stimulus(
            electrode, _bstimulator.config(configID)
        )
        self._raise_if_error("manual_stimulus")

    def begin_sequence(self) -> None:
        """
        This is the first command that must be called when creating a stimulation script. After calling this you are able to call wait,
        auto_stimulus, begin_group, and end_group commands. The stimulation script can have up to 128 commands, excluding begin_sequence and end_sequence
        """
        self.last_result = self._bstimulator_obj.beginning_of_sequence()
        self._raise_if_error("begin_sequence")

    def end_sequence(self) -> None:
        """This is the last command that must be called when creating a stimulation script. It does not count towards the maximum of 128 commands."""
        self.last_result = self._bstimulator_obj.end_of_sequence()
        self._raise_if_error("end_sequence")

    def begin_group(self) -> None:
        """
        This command signifies that the following commands up to the end_group command should all occur simultaneously. The only commands that are valid are the
        "auto_stimulus commands. You can only have as many stimulations as the number of current modules installed. Can't be called on the last of the 128 instructions
        "since it needs to have a closing end_group command.
        """
        self.last_result = self._bstimulator_obj.beginning_of_group()
        self._raise_if_error("begin_group")

    def end_group(self) -> None:
        """
        This command closes off a group of simultaneous stimulations. If begin_group is called during a sequence of commands, then there must be an end_group
        otherwise the user will get a sequence error as a return value.
        """
        self.last_result = self._bstimulator_obj.end_of_group()
        self._raise_if_error("end_group")

    def auto_stimulus(self, electrode: int, configID: int) -> None:
        """
        This command tells the stimulator when to send a stimulus to an electrode in a stimulation script. It can be used as many times as needed so long as the total number
        of commands does not exceed 128. It should also be used within begin_group and end_group commands to allow for simultaneous stimulations.

        electrode: The electrode that will be stimulated. Valid values are from 1 - 96
        configID: One of the fifteen stimulation waveforms that should be used. Valid values are from 1-15
        """
        self.validate_electrode(electrode)
        self.validate_configID(configID)
        self.last_result = self._bstimulator_obj.auto_stimulus(
            electrode, _bstimulator.config(configID)
        )
        self._raise_if_error("auto_stimulus")

    def wait(self, milliseconds: int) -> None:
        """
        This command can only be used within a stimulation script and is capable of adding a wait of up to 65,535 milliseconds.
        
        milliseconds: The number of milliseconds to wait before executing the next command
        """
        if milliseconds < 0 or milliseconds > 65535:
            raise ValueError("milliseconds out of range (0,65535)")
        self.last_result = self._bstimulator_obj.wait(milliseconds)
        self._raise_if_error("wait")

    def play(self, times: int) -> None:
        """
        Tells the stimulator the number of times that it should run the stimulation script. A zero passed in will tell it to run indefinately until it is either stopped or
        paused by the user. Other values include between 1 and 65,535 repetitions. Can not be called during a begin_sequence and end_sequence command call.

        times: Number of times to execute the stimulation script. 0 means indefinitely.
        """
        if times < 0 or 65535:
            raise ValueError("times out of range (0,65535)")
        self.last_result = self._bstimulator_obj.play(times)
        self._raise_if_error("play")
    
    def stop(self) -> None:
        """
        This will stop a currently running stimulation script and reset it so when played again it will begin from the first command. Can only be called while the stimulator
        has a status of stimulating or paused.
        """
        self.last_result = self._bstimulator_obj.stop()
        self._raise_if_error("stop")

    def pause(self) -> None:
        """
        This will pause a currently running stimulation script and keep track of the next command that needs to be executed so if it receives a play command it can pick up where it left off.
        """
        self.last_result = self._bstimulator_obj.pause()
        self._raise_if_error("pause")

    def read_max_output_voltage(self) -> None:
        pass