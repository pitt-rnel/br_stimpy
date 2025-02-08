"""
br_stimpy._bstimulator: CereStim Python SDK. Wrap of BStimulator.h using pybind11.
"""
from __future__ import annotations
import pybind11_stubgen.typing_ext
import typing
__all__ = ['BANK_SIZE', 'CallbackType', 'Config', 'DeviceInfo', 'EEPROM_SIZE', 'ElectrodeChannelMap', 'EventType', 'GroupStimulus', 'InterfaceType', 'MAX_CHANNELS', 'MAX_CONFIGURATIONS', 'MAX_MODULES', 'MaxOutputVoltage', 'MaximumValues', 'ModuleStatus', 'NUMBER_VOLT_MEAS', 'OCVolt', 'OutputMeasurement', 'PN6425', 'PN7008', 'PN7039', 'PN7169', 'PN7655', 'PN7656', 'PN7875', 'PN8543', 'PN8544', 'PN_invalid', 'PartNumbers', 'ReadEEPROMOutput', 'ReadHardwareValuesOutput', 'ResultType', 'SeqType', 'SequenceStatus', 'Stimulator', 'StimulatorType', 'StimulusConfiguration', 'TestElectrodes', 'TestModules', 'TriggerType', 'USBParams', 'Version', 'WFType', 'amp_great_max', 'callback_all', 'callback_count', 'callback_device_attachment', 'callback_reg_failed', 'channel_used_in_group', 'config_0', 'config_1', 'config_10', 'config_11', 'config_12', 'config_13', 'config_14', 'config_15', 'config_2', 'config_3', 'config_4', 'config_5', 'config_6', 'config_7', 'config_8', 'config_9', 'config_count', 'config_not_active', 'connected', 'device_locked', 'device_notify', 'device_registered', 'disconnected', 'echo_error', 'empty_config', 'event_count', 'event_device_attached', 'event_device_detached', 'freq_period_zero', 'frequency_great_max', 'interface_count', 'interface_cpusb', 'interface_default', 'interface_read', 'interface_timeout', 'interface_write', 'interface_wusb', 'invalid', 'invalid_afcf', 'invalid_amplitude', 'invalid_callback_type', 'invalid_channel', 'invalid_command', 'invalid_config', 'invalid_fastdisch', 'invalid_frequency', 'invalid_handle', 'invalid_interface', 'invalid_interphase', 'invalid_interpulse', 'invalid_module', 'invalid_module_enum', 'invalid_number', 'invalid_params', 'invalid_pulses', 'invalid_rwr', 'invalid_stim', 'invalid_trigger', 'invalid_voltage', 'invalid_width', 'library_firmware', 'macro_stim', 'micro_stim', 'module_count', 'module_disabled', 'module_enabled', 'module_ok', 'module_unavailable', 'module_voltagelimitation', 'no_device_selected', 'nok', 'not_implemented', 'null_ptr', 'ocvolt4_7', 'ocvolt5_3', 'ocvolt5_9', 'ocvolt6_5', 'ocvolt7_1', 'ocvolt7_7', 'ocvolt8_3', 'ocvolt8_9', 'ocvolt9_5', 'ocvolt_invalid', 'pause', 'phase_great_max', 'phase_not_balanced', 'playing', 'read_err', 'return_', 'sequence_error', 'stim_attached', 'stim_detached', 'stimuli_modules', 'stop', 'success', 'trigger', 'trigger_change', 'trigger_disabled', 'trigger_falling', 'trigger_invalid', 'trigger_rising', 'unknown', 'vector_UINT32', 'volt_great_max', 'wf_anodic_first', 'wf_cathodic_first', 'wf_invalid', 'width_great_max', 'write_err', 'writing']
class CallbackType:
    """
    Once a connection with the stimulator has been made over the USB and a stimulator object is created, that object needs to be notified of any events that take place. This is handled through a callback function.
    
    Members:
    
      callback_all : Monitor all events.
    
      callback_device_attachment : Monitor device attachment.
    
      callback_count : Number of Callback Types, Always the last value.
    """
    __members__: typing.ClassVar[dict[str, CallbackType]]  # value = {'callback_all': <CallbackType.callback_all: 0>, 'callback_device_attachment': <CallbackType.callback_device_attachment: 1>, 'callback_count': <CallbackType.callback_count: 2>}
    callback_all: typing.ClassVar[CallbackType]  # value = <CallbackType.callback_all: 0>
    callback_count: typing.ClassVar[CallbackType]  # value = <CallbackType.callback_count: 2>
    callback_device_attachment: typing.ClassVar[CallbackType]  # value = <CallbackType.callback_device_attachment: 1>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Config:
    """
    The stimulator is capable of storing up to 16 stimulus waveforms that can then be used in any stimulus. Each waveform is indepently configured by the user. The user can use different stimulus waveforms based on some predetermined signal based on feedback from the neural signals.
    
    Members:
    
      config_0 : Stimulation waveform configuration 0.
    
      config_1 : Stimulation waveform configuration 1.
    
      config_2 : Stimulation waveform configuration 2.
    
      config_3 : Stimulation waveform configuration 3.
    
      config_4 : Stimulation waveform configuration 4.
    
      config_5 : Stimulation waveform configuration 5.
    
      config_6 : Stimulation waveform configuration 6.
    
      config_7 : Stimulation waveform configuration 7.
    
      config_8 : Stimulation waveform configuration 8.
    
      config_9 : Stimulation waveform configuration 9.
    
      config_10 : Stimulation waveform configuration 10.
    
      config_11 : Stimulation waveform configuration 11.
    
      config_12 : Stimulation waveform configuration 12.
    
      config_13 : Stimulation waveform configuration 13.
    
      config_14 : Stimulation waveform configuration 14.
    
      config_15 : Stimulation waveform configuration 15.
    
      config_count : Total Configurations, Always the Last one.
    """
    __members__: typing.ClassVar[dict[str, Config]]  # value = {'config_0': <Config.config_0: 0>, 'config_1': <Config.config_1: 1>, 'config_2': <Config.config_2: 2>, 'config_3': <Config.config_3: 3>, 'config_4': <Config.config_4: 4>, 'config_5': <Config.config_5: 5>, 'config_6': <Config.config_6: 6>, 'config_7': <Config.config_7: 7>, 'config_8': <Config.config_8: 8>, 'config_9': <Config.config_9: 9>, 'config_10': <Config.config_10: 10>, 'config_11': <Config.config_11: 11>, 'config_12': <Config.config_12: 12>, 'config_13': <Config.config_13: 13>, 'config_14': <Config.config_14: 14>, 'config_15': <Config.config_15: 15>, 'config_count': <Config.config_count: 16>}
    config_0: typing.ClassVar[Config]  # value = <Config.config_0: 0>
    config_1: typing.ClassVar[Config]  # value = <Config.config_1: 1>
    config_10: typing.ClassVar[Config]  # value = <Config.config_10: 10>
    config_11: typing.ClassVar[Config]  # value = <Config.config_11: 11>
    config_12: typing.ClassVar[Config]  # value = <Config.config_12: 12>
    config_13: typing.ClassVar[Config]  # value = <Config.config_13: 13>
    config_14: typing.ClassVar[Config]  # value = <Config.config_14: 14>
    config_15: typing.ClassVar[Config]  # value = <Config.config_15: 15>
    config_2: typing.ClassVar[Config]  # value = <Config.config_2: 2>
    config_3: typing.ClassVar[Config]  # value = <Config.config_3: 3>
    config_4: typing.ClassVar[Config]  # value = <Config.config_4: 4>
    config_5: typing.ClassVar[Config]  # value = <Config.config_5: 5>
    config_6: typing.ClassVar[Config]  # value = <Config.config_6: 6>
    config_7: typing.ClassVar[Config]  # value = <Config.config_7: 7>
    config_8: typing.ClassVar[Config]  # value = <Config.config_8: 8>
    config_9: typing.ClassVar[Config]  # value = <Config.config_9: 9>
    config_count: typing.ClassVar[Config]  # value = <Config.config_count: 16>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DeviceInfo:
    """
    The stimulator has several different micro controllers that it uses. These are on the motherboard and current modules. As a result, it is very helpful for troubleshooting and debugging to see what versions of the firmware are stored on the motherboard and current modules as well as what the status of how many current modules are installed and what communication protocol is being used.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
        CereStim 96 Device Specific Information.
        """
    @property
    def mainboard_version(self) -> int:
        """
        MSB = version , LSB = subversion (i.e. 0x020A = version 2.10)
        """
    @mainboard_version.setter
    def mainboard_version(self, arg0: int) -> None:
        ...
    @property
    def module_status(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(16)]:
        """
        0x00 = Not available. 0x01 = Enabled. 0x02 = Disabled
        """
    @property
    def module_version(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(16)]:
        """
        MSB = version , LSB = subversion (i.e. 0x020A = version 2.10)
        """
    @property
    def protocol_version(self) -> int:
        """
        MSB = version , LSB = subversion (i.e. 0x020A = version 2.10)
        """
    @protocol_version.setter
    def protocol_version(self, arg0: int) -> None:
        ...
    @property
    def serial_no(self) -> int:
        """
        Hardware part number, type, and serial number 0xPN TY SN SN.
        """
    @serial_no.setter
    def serial_no(self, arg0: int) -> None:
        ...
class ElectrodeChannelMap:
    """
    The stimulator is capable of sending stimulation up to 96 different electrodes. The layout of where those electrodes are mapped to sometimes are not a straight channel 1 to electrode 1, such as in a Blackrock .CMP file. This struct allows the user to specify a mapping for there electrodes so that they do not need to worry about what channel they need to stimulate if they want electrode 20 to be stimulated.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
        Map Channels to Electrodes.
        """
    @property
    def bankA(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(32)]:
        """
        UINT8 Array, the pin on bank A is the index, and the value is the acutal electrode number.
        """
    @bankA.setter
    def bankA(self, arg1: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(32)]) -> None:
        ...
    @property
    def bankB(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(32)]:
        """
        UINT8 Array, the pin on bank B is the index, and the value is the acutal electrode number.
        """
    @bankB.setter
    def bankB(self, arg1: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(32)]) -> None:
        ...
    @property
    def bankC(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(32)]:
        """
        UINT8 Array, the pin on bank C is the index, and the value is the acutal electrode number.
        """
    @bankC.setter
    def bankC(self, arg1: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(32)]) -> None:
        ...
class EventType:
    """
    Since the stimulator is a HID, it can be plugged in and unplugged from the Host PC at will. The USB events capture the status of whether the device is attached or not.
    
    Members:
    
      event_device_attached : CereStim 96 is Attached to Host PC.
    
      event_device_detached : CereStim 96 is Detached from Host PC.
    
      event_count : Number of Events, Always the last value
    """
    __members__: typing.ClassVar[dict[str, EventType]]  # value = {'event_device_attached': <EventType.event_device_attached: 0>, 'event_device_detached': <EventType.event_device_detached: 1>, 'event_count': <EventType.event_count: 2>}
    event_count: typing.ClassVar[EventType]  # value = <EventType.event_count: 2>
    event_device_attached: typing.ClassVar[EventType]  # value = <EventType.event_device_attached: 0>
    event_device_detached: typing.ClassVar[EventType]  # value = <EventType.event_device_detached: 1>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class GroupStimulus:
    """
    The stimulator allows for a group of simultaneous stimulations to occur. Two methods exist for doing this, first is creating a program script and issueing several different calls. The second method saves on the USB overhead by allowing a single call to set up the simultaneous stimulations.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
        Group Stimulus.
        """
    @property
    def electrode(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(16)]:
        """
        electrodes to stimulate
        """
    @electrode.setter
    def electrode(self, arg1: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(16)]) -> None:
        ...
    @property
    def pattern(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(16)]:
        """
        Configuration Pattern to use with coresponding channel.
        """
    @pattern.setter
    def pattern(self, arg1: typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(16)]) -> None:
        ...
class InterfaceType:
    """
    The Stimulator was originally designed to be communicated via USB or RS232, and will be functional on multiple platforms. The RS232 interface no longer exists. Default type should generally be used.
    
    Members:
    
      interface_default : Default interface (windows USB)
    
      interface_wusb : Windows USB interface.
    
      interface_cpusb : Experimental cross-platform USB interface.
    
      interface_count : Number of Interfaces, always the last one.
    """
    __members__: typing.ClassVar[dict[str, InterfaceType]]  # value = {'interface_default': <InterfaceType.interface_default: 0>, 'interface_wusb': <InterfaceType.interface_wusb: 1>, 'interface_cpusb': <InterfaceType.interface_cpusb: 2>, 'interface_count': <InterfaceType.interface_count: 3>}
    interface_count: typing.ClassVar[InterfaceType]  # value = <InterfaceType.interface_count: 3>
    interface_cpusb: typing.ClassVar[InterfaceType]  # value = <InterfaceType.interface_cpusb: 2>
    interface_default: typing.ClassVar[InterfaceType]  # value = <InterfaceType.interface_default: 0>
    interface_wusb: typing.ClassVar[InterfaceType]  # value = <InterfaceType.interface_wusb: 1>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MaxOutputVoltage:
    """
    The Stimulator is capable of measuring what its current output compliance voltage level is using a known impedance and stimulus parameters.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
        Measured Output Voltage.
        """
    @property
    def milivolts(self) -> int:
        """
        Voltages are returned in millivolts.
        """
    @milivolts.setter
    def milivolts(self, arg0: int) -> None:
        ...
class MaximumValues:
    """
    The stimulator has an administrative interface that allows the primary researcher to set additional safety levels depending on there stimulation protocols and parameters.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
        Admin Max Values.
        """
    @property
    def amplitude(self) -> int:
        """
        Amplitude (uA)
        """
    @amplitude.setter
    def amplitude(self, arg0: int) -> None:
        ...
    @property
    def frequency(self) -> int:
        """
        Frequency (Hz)
        """
    @frequency.setter
    def frequency(self, arg0: int) -> None:
        ...
    @property
    def phase_charge(self) -> int:
        """
        Charge per phase (pC)
        """
    @phase_charge.setter
    def phase_charge(self, arg0: int) -> None:
        ...
    @property
    def voltage(self) -> int:
        """
        Max voltage value.
        """
    @voltage.setter
    def voltage(self, arg0: int) -> None:
        ...
class ModuleStatus:
    """
    The stimulator is capable of housing up to 16 current modules. Each current module can have several states based on how the user has configured the stimulator. The current modules are also capable of returning problem statuses based on the hardware.
    
    Members:
    
      module_unavailable : No current module in the specified position.
    
      module_enabled : Current module in the specified position is enabled.
    
      module_disabled : Current Module in the specified position is disabled.
    
      module_ok : Voltage levels on the current module are normal.
    
      module_voltagelimitation : Voltage levels on the current module are below normal, Module is bad.
    
      module_count : Number of Statuses, Always the Last one.
    """
    __members__: typing.ClassVar[dict[str, ModuleStatus]]  # value = {'module_unavailable': <ModuleStatus.module_unavailable: 0>, 'module_enabled': <ModuleStatus.module_enabled: 1>, 'module_disabled': <ModuleStatus.module_disabled: 2>, 'module_ok': <ModuleStatus.module_ok: 3>, 'module_voltagelimitation': <ModuleStatus.module_voltagelimitation: 4>, 'module_count': <ModuleStatus.module_count: 5>}
    __entries: typing.ClassVar[dict[str, tuple[ModuleStatus, str]]]
    module_count: typing.ClassVar[ModuleStatus]  # value = <ModuleStatus.module_count: 5>
    module_disabled: typing.ClassVar[ModuleStatus]  # value = <ModuleStatus.module_disabled: 2>
    module_enabled: typing.ClassVar[ModuleStatus]  # value = <ModuleStatus.module_enabled: 1>
    module_ok: typing.ClassVar[ModuleStatus]  # value = <ModuleStatus.module_ok: 3>
    module_unavailable: typing.ClassVar[ModuleStatus]  # value = <ModuleStatus.module_unavailable: 0>
    module_voltagelimitation: typing.ClassVar[ModuleStatus]  # value = <ModuleStatus.module_voltagelimitation: 4>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class OCVolt:
    """
    The Stimulator is capable of setting different output compliance voltage levels based on the users needs and safety considerations.
    
    Members:
    
      ocvolt4_7 : Output Voltage Level 4.7V.
    
      ocvolt5_3 : Output Voltage Level 5.3V.
    
      ocvolt5_9 : Output Voltage Level 5.9V.
    
      ocvolt6_5 : Output Voltage Level 6.5V.
    
      ocvolt7_1 : Output Voltage Level 7.1V.
    
      ocvolt7_7 : Output Voltage Level 7.7V.
    
      ocvolt8_3 : Output Voltage Level 8.3V.
    
      ocvolt8_9 : Output Voltage Level 8.9V.
    
      ocvolt9_5 : Output Voltage Level 9.5V.
    
      ocvolt_invalid : Invalid Compliance Voltage, Always the Last One.
    """
    __members__: typing.ClassVar[dict[str, OCVolt]]  # value = {'ocvolt4_7': <OCVolt.ocvolt4_7: 7>, 'ocvolt5_3': <OCVolt.ocvolt5_3: 8>, 'ocvolt5_9': <OCVolt.ocvolt5_9: 9>, 'ocvolt6_5': <OCVolt.ocvolt6_5: 10>, 'ocvolt7_1': <OCVolt.ocvolt7_1: 11>, 'ocvolt7_7': <OCVolt.ocvolt7_7: 12>, 'ocvolt8_3': <OCVolt.ocvolt8_3: 13>, 'ocvolt8_9': <OCVolt.ocvolt8_9: 14>, 'ocvolt9_5': <OCVolt.ocvolt9_5: 15>, 'ocvolt_invalid': <OCVolt.ocvolt_invalid: 16>}
    __entries: typing.ClassVar[dict[str, tuple[OCVolt, str]]]
    ocvolt4_7: typing.ClassVar[OCVolt]  # value = <OCVolt.ocvolt4_7: 7>
    ocvolt5_3: typing.ClassVar[OCVolt]  # value = <OCVolt.ocvolt5_3: 8>
    ocvolt5_9: typing.ClassVar[OCVolt]  # value = <OCVolt.ocvolt5_9: 9>
    ocvolt6_5: typing.ClassVar[OCVolt]  # value = <OCVolt.ocvolt6_5: 10>
    ocvolt7_1: typing.ClassVar[OCVolt]  # value = <OCVolt.ocvolt7_1: 11>
    ocvolt7_7: typing.ClassVar[OCVolt]  # value = <OCVolt.ocvolt7_7: 12>
    ocvolt8_3: typing.ClassVar[OCVolt]  # value = <OCVolt.ocvolt8_3: 13>
    ocvolt8_9: typing.ClassVar[OCVolt]  # value = <OCVolt.ocvolt8_9: 14>
    ocvolt9_5: typing.ClassVar[OCVolt]  # value = <OCVolt.ocvolt9_5: 15>
    ocvolt_invalid: typing.ClassVar[OCVolt]  # value = <OCVolt.ocvolt_invalid: 16>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class OutputMeasurement:
    """
    The stimulator is capable of sending out a stimulus using known values and measure the voltage that is returned at five locations during the course of that stimulation. The five values in order are as follows: Just before the first phase, during the first phase, in between phases, during the second phase, and just after the second phase.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
        Measured Stimulus Voltage.
        """
    @property
    def measurement(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(5)]:
        """
        Voltages are returned in millivolts.
        """
class PartNumbers:
    """
    There are many versions of the stimulator. There are research versions of micro and macro stimulators, each with varying number of installed current modules; and there is a clinical version of the macro stimulator with a single current module. The part number of the device sets internal safety levels of what stimulation parameters are allowed.
    
    Members:
    
      PN6425 : CereStim R96 Micro Stimulator Beta Unit, May be either a 3 or 16 current module unit.
    
      PN7008 : CereStim R96 Micro Stimulator 3 current module unit.
    
      PN7039 : CereStim R96 Micro Stimulator 16 current module unit.
    
      PN7169 : CereStim R96 Micro Stimulator 1 current module unit.
    
      PN8543 : CereStim R96 Micro Stimulator Customer Specified Configuration.
    
      PN7655 : CereStim R96 Macro Stimulator 3 current module unit.
    
      PN7656 : CereStim M96 Macro Stimulator Clinical 1 current module unit.
    
      PN7875 : CereStim R96 Macro Stimulator 16 current module unit.
    
      PN8544 : CereStim R96 Macro Stimulator Customer Specified Configuration.
    
      PN_invalid : Invalid part number.
    """
    PN6425: typing.ClassVar[PartNumbers]  # value = <PartNumbers.PN6425: 0>
    PN7008: typing.ClassVar[PartNumbers]  # value = <PartNumbers.PN7008: 1>
    PN7039: typing.ClassVar[PartNumbers]  # value = <PartNumbers.PN7039: 2>
    PN7169: typing.ClassVar[PartNumbers]  # value = <PartNumbers.PN7169: 3>
    PN7655: typing.ClassVar[PartNumbers]  # value = <PartNumbers.PN7655: 5>
    PN7656: typing.ClassVar[PartNumbers]  # value = <PartNumbers.PN7656: 6>
    PN7875: typing.ClassVar[PartNumbers]  # value = <PartNumbers.PN7875: 7>
    PN8543: typing.ClassVar[PartNumbers]  # value = <PartNumbers.PN8543: 4>
    PN8544: typing.ClassVar[PartNumbers]  # value = <PartNumbers.PN8544: 8>
    PN_invalid: typing.ClassVar[PartNumbers]  # value = <PartNumbers.PN_invalid: 9>
    __members__: typing.ClassVar[dict[str, PartNumbers]]  # value = {'PN6425': <PartNumbers.PN6425: 0>, 'PN7008': <PartNumbers.PN7008: 1>, 'PN7039': <PartNumbers.PN7039: 2>, 'PN7169': <PartNumbers.PN7169: 3>, 'PN8543': <PartNumbers.PN8543: 4>, 'PN7655': <PartNumbers.PN7655: 5>, 'PN7656': <PartNumbers.PN7656: 6>, 'PN7875': <PartNumbers.PN7875: 7>, 'PN8544': <PartNumbers.PN8544: 8>, 'PN_invalid': <PartNumbers.PN_invalid: 9>}
    __entries: typing.ClassVar[dict[str, tuple[PartNumbers, str]]]
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ReadEEPROMOutput:
    """
    The EEprom on the microcontroller stores the information that should be preserved over time even when the device is off or unplugged. These values can be read in order to debug or know the status of different components within the device.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
        CereStim 96 Motherboard EEprom.
        """
    @property
    def eeprom(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(256)]:
        """
        eeprom values
        """
class ReadHardwareValuesOutput:
    """
    The stimulators various models have some different hardware configurations, so it is beneficial to get those hardware values of that particuliar CereStim 96.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
        Hardware Values of the CereStim 96.
        """
    @property
    def amp(self) -> int:
        """
        Max phase amplitude based on hardware in uA.
        """
    @amp.setter
    def amp(self, arg0: int) -> None:
        ...
    @property
    def charge(self) -> int:
        """
        Max charge based on hardware in pC.
        """
    @charge.setter
    def charge(self, arg0: int) -> None:
        ...
    @property
    def interphase(self) -> int:
        """
        Max Interphase width based on hardware in uS.
        """
    @interphase.setter
    def interphase(self, arg0: int) -> None:
        ...
    @property
    def max_comp_voltage(self) -> int:
        """
        Max output compliance voltage.
        """
    @max_comp_voltage.setter
    def max_comp_voltage(self, arg0: int) -> None:
        ...
    @property
    def max_freq(self) -> int:
        """
        Max Frequency based on hardware in Hz.
        """
    @max_freq.setter
    def max_freq(self, arg0: int) -> None:
        ...
    @property
    def min_comp_voltage(self) -> int:
        """
        Min output compliance voltage.
        """
    @min_comp_voltage.setter
    def min_comp_voltage(self, arg0: int) -> None:
        ...
    @property
    def min_freq(self) -> int:
        """
        Min Frequency based on hardware in Hz.
        """
    @min_freq.setter
    def min_freq(self, arg0: int) -> None:
        ...
    @property
    def modules(self) -> int:
        """
        Number of modules installed in device.
        """
    @modules.setter
    def modules(self, arg0: int) -> None:
        ...
    @property
    def width(self) -> int:
        """
        Max Width for each phase based on hardware in uS.
        """
    @width.setter
    def width(self, arg0: int) -> None:
        ...
class ResultType:
    """
    A stimulator object creates a USB connection with the actual CereStim 96 and calls are made to it through the stimulator object. The stimulator object can return an error message (Software Error) or the CereStim 96 can return an error message (Hardware Error).
    
    Members:
    
      return_ : Software Error: Early returned warning.
    
      success : Successful operation.
    
      not_implemented : Software Error: Not implemented.
    
      unknown : Software Error: Unknown error.
    
      invalid_handle : Software Error: Invalid handle.
    
      null_ptr : Software Error: Null pointer.
    
      invalid_interface : Software Error: Invalid interface specified or interface not supported.
    
      interface_timeout : Software Error: Timeout in creating the interface.
    
      device_registered : Software Error: Device with that address already connected.
    
      invalid_params : Software Error: Invalid parameters.
    
      disconnected : Software Error: Stim is disconnected, invalid operation.
    
      connected : Software Error: Stim is connected, invalid operation.
    
      stim_attached : Software Error: Stim is attached, invalid operation.
    
      stim_detached : Software Error: Stim is detached, invalid operation.
    
      device_notify : Software Error: Cannot register for device change notification.
    
      invalid_command : Software Error: Invalid command.
    
      interface_write : Software Error: Cannot open interface for write.
    
      interface_read : Software Error: Cannot open interface for read.
    
      write_err : Software Error: Cannot write command to the interface.
    
      read_err : Software Error: Cannot read command from the interface.
    
      invalid_module_enum : Software Error: Invalid module number specified.
    
      invalid_callback_type : Software Error: Invalid callback type.
    
      callback_reg_failed : Software Error: Callback register/unregister failed.
    
      library_firmware : Software Error: CereStim Firmware version not supported by SDK Library Version.
    
      freq_period_zero : Software Error: Frequency or Period is zero and unable to be converted.
    
      no_device_selected : Software Error: No physical device has been set. See setDevice() for help.
    
      nok : Hardware Error: Comamnd result not OK.
    
      sequence_error : Hardware Error: Sequence Error.
    
      invalid_trigger : Hardware Error: Invalid Trigger.
    
      invalid_channel : Hardware Error: Invalid Channel.
    
      invalid_config : Hardware Error: Invalid Configuration.
    
      invalid_number : Hardware Error: Invalid Number.
    
      invalid_rwr : Hardware Error: Invalid Read/Write.
    
      invalid_voltage : Hardware Error: Invalid Voltage.
    
      invalid_amplitude : Hardware Error: Invalid Amplitude.
    
      invalid_afcf : Hardware Error: Invalid AF/CF.
    
      invalid_pulses : Hardware Error: Invalid Pulses.
    
      invalid_width : Hardware Error: Invalid Width.
    
      invalid_interpulse : Hardware Error: Invalid Interpulse.
    
      invalid_interphase : Hardware Error: Invalid Interphase.
    
      invalid_fastdisch : Hardware Error: Invalid Fast Discharge.
    
      invalid_module : Hardware Error: Invalid Module.
    
      stimuli_modules : Hardware Error: More Stimuli than Modules.
    
      module_unavailable : Hardware Error: Module not Available.
    
      channel_used_in_group : Hardware Error: Channel already used in Group.
    
      config_not_active : Hardware Error: Configuration not Active.
    
      empty_config : Hardware Error: Empty Config.
    
      phase_not_balanced : Hardware Error: Phases not Balanced.
    
      phase_great_max : Hardware Error: Phase Charge Greater than Max.
    
      amp_great_max : Hardware Error: Amplitude Greater than Max.
    
      width_great_max : Hardware Error: Width Greater than Max.
    
      volt_great_max : Hardware Error: Voltage Greater than Max.
    
      module_disabled : Hardware Error: Module already disabled can't disable it.
    
      module_enabled : Hardware Error: Module already enabled can't reenable it.
    
      invalid_frequency : Hardware Error: Invalid Frequency.
    
      frequency_great_max : Hardware Error: The frequency is greater than the max value allowed.
    
      device_locked : Hardware Error: Device locked due to hardware mismatch or not being configured.
    
      echo_error : Hardware Error: Command returned was not the same command sent.
    """
    __members__: typing.ClassVar[dict[str, ResultType]]  # value = {'return_': <ResultType.return_: 1>, 'success': <ResultType.success: 0>, 'not_implemented': <ResultType.not_implemented: -1>, 'unknown': <ResultType.unknown: -2>, 'invalid_handle': <ResultType.invalid_handle: -3>, 'null_ptr': <ResultType.null_ptr: -4>, 'invalid_interface': <ResultType.invalid_interface: -5>, 'interface_timeout': <ResultType.interface_timeout: -6>, 'device_registered': <ResultType.device_registered: -7>, 'invalid_params': <ResultType.invalid_params: -8>, 'disconnected': <ResultType.disconnected: -9>, 'connected': <ResultType.connected: -10>, 'stim_attached': <ResultType.stim_attached: -11>, 'stim_detached': <ResultType.stim_detached: -12>, 'device_notify': <ResultType.device_notify: -13>, 'invalid_command': <ResultType.invalid_command: -14>, 'interface_write': <ResultType.interface_write: -15>, 'interface_read': <ResultType.interface_read: -16>, 'write_err': <ResultType.write_err: -17>, 'read_err': <ResultType.read_err: -18>, 'invalid_module_enum': <ResultType.invalid_module_enum: -19>, 'invalid_callback_type': <ResultType.invalid_callback_type: -20>, 'callback_reg_failed': <ResultType.callback_reg_failed: -21>, 'library_firmware': <ResultType.library_firmware: -22>, 'freq_period_zero': <ResultType.freq_period_zero: -23>, 'no_device_selected': <ResultType.no_device_selected: -24>, 'nok': <ResultType.nok: -100>, 'sequence_error': <ResultType.sequence_error: -102>, 'invalid_trigger': <ResultType.invalid_trigger: -103>, 'invalid_channel': <ResultType.invalid_channel: -104>, 'invalid_config': <ResultType.invalid_config: -105>, 'invalid_number': <ResultType.invalid_number: -106>, 'invalid_rwr': <ResultType.invalid_rwr: -107>, 'invalid_voltage': <ResultType.invalid_voltage: -108>, 'invalid_amplitude': <ResultType.invalid_amplitude: -109>, 'invalid_afcf': <ResultType.invalid_afcf: -110>, 'invalid_pulses': <ResultType.invalid_pulses: -111>, 'invalid_width': <ResultType.invalid_width: -112>, 'invalid_interpulse': <ResultType.invalid_interpulse: -113>, 'invalid_interphase': <ResultType.invalid_interphase: -114>, 'invalid_fastdisch': <ResultType.invalid_fastdisch: -115>, 'invalid_module': <ResultType.invalid_module: -116>, 'stimuli_modules': <ResultType.stimuli_modules: -117>, 'module_unavailable': <ResultType.module_unavailable: -118>, 'channel_used_in_group': <ResultType.channel_used_in_group: -119>, 'config_not_active': <ResultType.config_not_active: -120>, 'empty_config': <ResultType.empty_config: -121>, 'phase_not_balanced': <ResultType.phase_not_balanced: -122>, 'phase_great_max': <ResultType.phase_great_max: -123>, 'amp_great_max': <ResultType.amp_great_max: -124>, 'width_great_max': <ResultType.width_great_max: -125>, 'volt_great_max': <ResultType.volt_great_max: -126>, 'module_disabled': <ResultType.module_disabled: -127>, 'module_enabled': <ResultType.module_enabled: -128>, 'invalid_frequency': <ResultType.invalid_frequency: -129>, 'frequency_great_max': <ResultType.frequency_great_max: -130>, 'device_locked': <ResultType.device_locked: -131>, 'echo_error': <ResultType.echo_error: -132>}
    __entries: typing.ClassVar[dict[str, tuple[ResultType, str]]]
    amp_great_max: typing.ClassVar[ResultType]  # value = <ResultType.amp_great_max: -124>
    callback_reg_failed: typing.ClassVar[ResultType]  # value = <ResultType.callback_reg_failed: -21>
    channel_used_in_group: typing.ClassVar[ResultType]  # value = <ResultType.channel_used_in_group: -119>
    config_not_active: typing.ClassVar[ResultType]  # value = <ResultType.config_not_active: -120>
    connected: typing.ClassVar[ResultType]  # value = <ResultType.connected: -10>
    device_locked: typing.ClassVar[ResultType]  # value = <ResultType.device_locked: -131>
    device_notify: typing.ClassVar[ResultType]  # value = <ResultType.device_notify: -13>
    device_registered: typing.ClassVar[ResultType]  # value = <ResultType.device_registered: -7>
    disconnected: typing.ClassVar[ResultType]  # value = <ResultType.disconnected: -9>
    echo_error: typing.ClassVar[ResultType]  # value = <ResultType.echo_error: -132>
    empty_config: typing.ClassVar[ResultType]  # value = <ResultType.empty_config: -121>
    freq_period_zero: typing.ClassVar[ResultType]  # value = <ResultType.freq_period_zero: -23>
    frequency_great_max: typing.ClassVar[ResultType]  # value = <ResultType.frequency_great_max: -130>
    interface_read: typing.ClassVar[ResultType]  # value = <ResultType.interface_read: -16>
    interface_timeout: typing.ClassVar[ResultType]  # value = <ResultType.interface_timeout: -6>
    interface_write: typing.ClassVar[ResultType]  # value = <ResultType.interface_write: -15>
    invalid_afcf: typing.ClassVar[ResultType]  # value = <ResultType.invalid_afcf: -110>
    invalid_amplitude: typing.ClassVar[ResultType]  # value = <ResultType.invalid_amplitude: -109>
    invalid_callback_type: typing.ClassVar[ResultType]  # value = <ResultType.invalid_callback_type: -20>
    invalid_channel: typing.ClassVar[ResultType]  # value = <ResultType.invalid_channel: -104>
    invalid_command: typing.ClassVar[ResultType]  # value = <ResultType.invalid_command: -14>
    invalid_config: typing.ClassVar[ResultType]  # value = <ResultType.invalid_config: -105>
    invalid_fastdisch: typing.ClassVar[ResultType]  # value = <ResultType.invalid_fastdisch: -115>
    invalid_frequency: typing.ClassVar[ResultType]  # value = <ResultType.invalid_frequency: -129>
    invalid_handle: typing.ClassVar[ResultType]  # value = <ResultType.invalid_handle: -3>
    invalid_interface: typing.ClassVar[ResultType]  # value = <ResultType.invalid_interface: -5>
    invalid_interphase: typing.ClassVar[ResultType]  # value = <ResultType.invalid_interphase: -114>
    invalid_interpulse: typing.ClassVar[ResultType]  # value = <ResultType.invalid_interpulse: -113>
    invalid_module: typing.ClassVar[ResultType]  # value = <ResultType.invalid_module: -116>
    invalid_module_enum: typing.ClassVar[ResultType]  # value = <ResultType.invalid_module_enum: -19>
    invalid_number: typing.ClassVar[ResultType]  # value = <ResultType.invalid_number: -106>
    invalid_params: typing.ClassVar[ResultType]  # value = <ResultType.invalid_params: -8>
    invalid_pulses: typing.ClassVar[ResultType]  # value = <ResultType.invalid_pulses: -111>
    invalid_rwr: typing.ClassVar[ResultType]  # value = <ResultType.invalid_rwr: -107>
    invalid_trigger: typing.ClassVar[ResultType]  # value = <ResultType.invalid_trigger: -103>
    invalid_voltage: typing.ClassVar[ResultType]  # value = <ResultType.invalid_voltage: -108>
    invalid_width: typing.ClassVar[ResultType]  # value = <ResultType.invalid_width: -112>
    library_firmware: typing.ClassVar[ResultType]  # value = <ResultType.library_firmware: -22>
    module_disabled: typing.ClassVar[ResultType]  # value = <ResultType.module_disabled: -127>
    module_enabled: typing.ClassVar[ResultType]  # value = <ResultType.module_enabled: -128>
    module_unavailable: typing.ClassVar[ResultType]  # value = <ResultType.module_unavailable: -118>
    no_device_selected: typing.ClassVar[ResultType]  # value = <ResultType.no_device_selected: -24>
    nok: typing.ClassVar[ResultType]  # value = <ResultType.nok: -100>
    not_implemented: typing.ClassVar[ResultType]  # value = <ResultType.not_implemented: -1>
    null_ptr: typing.ClassVar[ResultType]  # value = <ResultType.null_ptr: -4>
    phase_great_max: typing.ClassVar[ResultType]  # value = <ResultType.phase_great_max: -123>
    phase_not_balanced: typing.ClassVar[ResultType]  # value = <ResultType.phase_not_balanced: -122>
    read_err: typing.ClassVar[ResultType]  # value = <ResultType.read_err: -18>
    return_: typing.ClassVar[ResultType]  # value = <ResultType.return_: 1>
    sequence_error: typing.ClassVar[ResultType]  # value = <ResultType.sequence_error: -102>
    stim_attached: typing.ClassVar[ResultType]  # value = <ResultType.stim_attached: -11>
    stim_detached: typing.ClassVar[ResultType]  # value = <ResultType.stim_detached: -12>
    stimuli_modules: typing.ClassVar[ResultType]  # value = <ResultType.stimuli_modules: -117>
    success: typing.ClassVar[ResultType]  # value = <ResultType.success: 0>
    unknown: typing.ClassVar[ResultType]  # value = <ResultType.unknown: -2>
    volt_great_max: typing.ClassVar[ResultType]  # value = <ResultType.volt_great_max: -126>
    width_great_max: typing.ClassVar[ResultType]  # value = <ResultType.width_great_max: -125>
    write_err: typing.ClassVar[ResultType]  # value = <ResultType.write_err: -17>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SeqType:
    """
    The Stimulator has internal states, and based on those states the stimulator is allowed to perform different functions. The SeqType enumerator lists all the valid states.
    
    Members:
    
      stop : The stimulator is stopped.
    
      pause : The stimulator is paused.
    
      playing : The stimulator is actively delivering a stimulus.
    
      writing : A stimulus sequence is being written to the stimulator.
    
      trigger : The stimulator is waiting for a trigger on its trigger line.
    
      invalid : Invalid Sequence, Always the last value.
    """
    __members__: typing.ClassVar[dict[str, SeqType]]  # value = {'stop': <SeqType.stop: 0>, 'pause': <SeqType.pause: 1>, 'playing': <SeqType.playing: 2>, 'writing': <SeqType.writing: 3>, 'trigger': <SeqType.trigger: 4>, 'invalid': <SeqType.invalid: 5>}
    __entries: typing.ClassVar[dict[str, tuple[SeqType, str]]]
    invalid: typing.ClassVar[SeqType]  # value = <SeqType.invalid: 5>
    pause: typing.ClassVar[SeqType]  # value = <SeqType.pause: 1>
    playing: typing.ClassVar[SeqType]  # value = <SeqType.playing: 2>
    stop: typing.ClassVar[SeqType]  # value = <SeqType.stop: 0>
    trigger: typing.ClassVar[SeqType]  # value = <SeqType.trigger: 4>
    writing: typing.ClassVar[SeqType]  # value = <SeqType.writing: 3>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SequenceStatus:
    """
    The stimulator can always be queried to determine what state it is in.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
        Status of the Stimulator.
        """
    @property
    def status(self) -> int:
        """
        Contains status of the stimulator.
        """
    @status.setter
    def status(self, arg0: int) -> None:
        ...
class Stimulator:
    """
    The stimulator class encapsulates all the functionallity of the stimulator and allows the user the ability to interface directly with Blackrock Microsystems CereStim 96 device. By encapsulating it in an object, multiple stimulators can be connected to a single Host PC and be used simultaneously.
    """
    class MaxStimulatorError:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __init__(self) -> None:
            """
            Error If there are more stimulator objects created than allowed which is MAX_STIMULATORS
            """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def scan_for_devices() -> vector_UINT32:
        """
        Scans all USB devices and builds up a list of serial numbers of the devices connected to the computer. In order to connect to a device, this function has to be invoked first, then a device needs to be selected through setDevice() and only then connect()
        """
    def __init__(self) -> None:
        """
        Creates a stimulator object that is able to bind to an actual CereStim 96 that is connected to the host PC.
        """
    def auto_stimulus(self, electrode: int, configID: Config) -> ResultType:
        """
        This command tells the stimulator when to send a stimulus to an electrode in a stimulation script. It can be used as many times as needed so long as the total number of commands does not exceed 128. It should also be used within beginningOfGroup and endOfGroup commands to allow for simultaneous stimulations.
        
        electrode: The electrode that will be stimulated Valid values are from 1 - 96
        configID: One of the fifteen stimulation waveforms that should be used
        """
    def beginning_of_group(self) -> ResultType:
        """
        This command signifies that the following commands up to the endOfGroup command should all occur simultaneously. The only commands that are valid are the autoStimulus commands. You can only have as many stimulations as the number of current modules installed. Cant be called on the last of the 128 instructions since it needs to have a closing endOfGroup command.
        """
    def beginning_of_sequence(self) -> ResultType:
        """
        This is the first command that must be called when creating a stimulation script. After calling this you are able to call wait, autoStimulus, beginningOfGroup, and endOfGroup commands. The stimulation script can have up to 128 commands, excluding beginningOfSequence and endOfSequence
        """
    def configure_stimulus_pattern(self, configID: Config, afcf: WFType, pulses: int, amp1: int, amp2: int, width1: int, width2: int, frequency: int, interphase: int) -> ResultType:
        """
        Takes all of the parameters needed in order to create a custom biphasic stimulation waveform. The device is capable of handling 16 differnt waveforms, but waveform 0 is reserved and used for testing in getting measurements from electrodes and current modules. Micro and Macro stimulators have different ranges of valid values. Especially for the amplitude where micro stimulators are in the uA range with uA precision, Macro stimulators go from 100 uA to 10 mA with 100 uA precision. While the widths and interphases have quite a range, the user needs to somewhat understand how they interact with the frequency chosen. You dont want a stimulus waveform that is longer than the time between repeats.
        
        configID: The stimulation waveform that is being configured 1 - 15
        afcf: What polarity should the first phase be, Anodic or Cathodic first
        pulses: The number of stimulation pulses in waveform from 1 - 255
        amp1: The amplitude of the first phase, for Micro it is 1 - 215 uA, and for Macro it is 100 uA - 10 mA
        amp2: The amplitude of the first phase, for Micro it is 1 - 215 uA, and for Macro it is 100 uA - 10 mA
        width1: The width of the first phase in the stimulation 1 - 65,535 uS
        width2: The width of the second phase in the stimulation 1 - 65,535 uS
        frequency1: The stimulating frequency at which the biphasic pulses should repeat 4 - 5000 Hz
        interphase: The period of time between the first and second phases 53 - 65,535 uS
        """
    def connect(self, stim_interface: InterfaceType, params: typing.Any) -> ResultType:
        """
        Tries to establish a connection with a CereStim 96 device that has been selected using setDevice().
        
        stim_interface: The type of interface that the object should try and connect over
        params: A void pointer to either an initialized BUsbParams structure or initialized BRs232Params structure
        """
    def disable_module(self, module: int) -> ResultType:
        """
        Allows the user to disable different current modules that are installed in the CereStim. This is useful for testing and making sure that multiple current modules are all giving the same output values. The current module has to exist to be disabled.
        
        module: The current module to be disabled from 0 to 15
        """
    def disable_stimulus_configuration(self, config_id: int) -> ResultType:
        """
        Disables a stimulation waveform so that it is able to be reset
        
        config_id: The configuration to disable
        """
    def disconnect(self) -> ResultType:
        """
        Disconnects from a connected CereStim 96 device.
        """
    def enable_module(self, module: int) -> ResultType:
        """
        Allows the user to enable different current modules that have been disabled. This is useful for testing and making sure that multiple current modules are all giving the same output values.
        
        module: The current module to be enabled from 0 to 15
        """
    def end_of_group(self) -> ResultType:
        """
        This command closes off a group of simultaneous stimulations. If beginningOfGroup is called during a sequence of commands, then there must be an endOfGroup otherwise the user will get a sequence error as a return value.
        """
    def end_of_sequence(self) -> ResultType:
        """
        This is the last command that must be called when creating a stimulation script. It does not count towards the maximum of 128 commands.
        """
    def erase_eeprom(self) -> ResultType:
        """
        Erases the complete EEProm on the the CereStim 96 motherboard, setting all values to 0xFF
        """
    def get_interface(self) -> InterfaceType:
        """
        Checks to see what interface is being used for the connection between the stimulator object and the physical CereStim 96 Device.
        
        Returns: The interface being used for the stimulator object
        """
    def get_max_hard_charge(self) -> int:
        """
        This value is based on the hardware of the particuliar model of the CereStim 96. Again the micro and macro versions of the stimulator have different values
        """
    def get_max_hard_frequency(self) -> int:
        """
        This value is based on the hardware of the particuliar model of the CereStim 96. Again the micro and macro versions of the stimulator have different values
        
        Returns: Maximum Stimulating Frequency in Hz
        """
    def get_max_hard_interphase(self) -> int:
        """
        This value is based on the hardware of the particuliar model of the CereStim 96
        
        Maximum interphase width in uS
        """
    def get_max_hard_width(self) -> int:
        """
        This value is based on the hardware of the particuliar model of the CereStim 96.
        
        Returns: Maximum width of each phase in uS
        """
    def get_min_hard_frequency(self) -> int:
        """
        This value is based on the hardware of the particuliar model of the CereStim 96. Again the micro and macro versions of the stimulator have different values
        
        Returns: Minimum Stimulating Frequency in Hz
        """
    def get_min_max_amplitude(self) -> int:
        """
        Since there are different models and version of the stimulator, such as the micro and macro versions, this will allow the user to get the min and max amplitudes that are allowed for stimulation. The upper two MSB are the maximum amplitude while the lower two LSB are the minimum amplitude.
        
        Returns: Min and Max Amplitude.
        """
    def get_module_firmware_version(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(16)]:
        """
        Each current module has its own microcontroller and has a firmware version. All current modules in a single stimulator should have the same firmware version. The MSB is the Major revision number and the LSB is the minor revision number. I.e. 0x0105 would be version 1.5
        """
    def get_module_status(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(16)]:
        """
        This tells the status of each current module, whether it is enabled, disabled, or not available.
        """
    def get_motherboard_firmware_version(self) -> int:
        """
        Retrieves the firmware revision of the microcontroller on the motherboard. The MSB is the Major revision number and the LSB is the minor revision number. I.e. 0x0500 would be version 5.0
        
        Returns: Firmware Version of the Motherboard
        """
    def get_number_modules(self) -> int:
        """
        This value is based on the hardware of the particuliar model of the CereStim 96. Again the micro and macro versions of the stimulator have different values
        
        Returns: Number of Modules installed
        """
    def get_protocol_version(self) -> int:
        """
        The protocol version that the motherboard uses to send and receive data from the current modules. The MSB is the Major revision number and the LSB is the minor revision number. I.e. 0x0105 would be version 1.5
        
        Returns: Protocol Version of the Motherboard
        """
    def get_serial_number(self) -> int:
        """
        Retrieves the serial number that is programmed into the CereStim 96 device that is attached. The format of the 32 bit serial number is as follows 0xPPXXSSSS, where PP is the part number, XX is ignored, and SSSS is the serial number. The part number is a BPartNumbers enumeration.
        
        Returns: Part Number and Serial number of the CereStim 96
        """
    def get_usb_address(self) -> int:
        ...
    def group_stimulus(self, begin_seq: int, play: int, times: int, number: int, input: GroupStimulus) -> ResultType:
        """
        There is a lot of overhead in sending commands over the USB to the CereStim 96. each function call averages 2mS. This function allows the user to create the stimulation parameters beforehand and in a single function call perform simultaneous stimulations based on different electrodes and configured waveforms.
        
        begin_seq: Boolean expression to tell the function that it is the beginning of a sequence
        play: Boolean expression to tell if the stimulator should begin stimulating immedieatly after this call
        times: The number of times to play the stimulation, is ignored if play = false
        number: The number of stimulus that will occur simultaneously.
        input: Pointer to an instantiated BGroupStimulus structure which has a pair of arrays with electrodes and waveforms
        """
    def is_connected(self) -> int:
        """
        Lets the user know that the stimulator object is connected to a physical CereStim 96 device.
        
        Returns: a boolean result, 1 = TRUE, 0 = FALSE
        """
    def is_device_locked(self) -> int:
        """
        If the detected number of current modules doesn't match the hardware configuration or if the hardware configuration is not setup, the device will be locked down preventing any stimulation from occuring.
        
        Returns: true if locked false otherwise
        """
    def is_safety_disabled(self) -> int:
        """
        For Internal validation and testing it is required to disable the safety limits in the firmware and API so that hardware limits can be observed and tested.
        
        Returns: true if disabled false otherwise
        """
    def lib_version(self, output: Version) -> ResultType:
        """
        Takes a pointer to a BVersion structure and writes the libarary version to the structure.
        """
    def manual_stimulus(self, electrode: int, configID: Config) -> ResultType:
        """
        Allows the user to send a single stimulus pulse of one of the stimulation waveforms to a specified electrode.
        
        electrode: The electrode that should be stimulated Valid values are from 1 - 96
        configID: The stimulation waveform to use Valid values are from 1 - 15
        """
    def max_output_voltage(self, output: MaxOutputVoltage, rw: int, voltage: OCVolt) -> ResultType:
        """
        This will set the values of +VDD and -VSS on the stimulator which allows it to effectively limit the maximum output voltage that can be delivered during a stimulation. If the output current times the impedance of the electrode is greater than the max compliance voltage then it means the full current is not being deliverd to the electrode because it can not drive any more current.
        
        output: Pointer to a BMaxOutputVoltage structure that will contain the read value
        rw: Boolean expression for determining if you just want to read the output compliance voltage or update it with a new value Read = 0 and Write = 1
        voltage: The voltage level that is being set if writing, otherwise it is ignored
        """
    def measure_output_voltage(self, output: OutputMeasurement, module: int, electrode: int) -> ResultType:
        """
        Sends a known stimulation configuration, 45 uA for micro and 9 mA for Macro, from a selected current module to a specific module. It is helpful for determining the impedance of the electrode.
        
        output: A pointer to a BOutpuMeasurment structure to store the returned measurement values
        module: The specific current module (0 - 15) that should send the stimulus The module must be enabled.
        electrode: The electrode to send the stimulation to Valid values are from 1 - 96
        """
    def pause(self) -> ResultType:
        """
        This will pause a currently running stimulation script and keep track of the next command that needs to be executed so if it receives a play command it can pick up where it left off.
        """
    def play(self, times: int) -> ResultType:
        """
        Tells the stimulator the number of times that it should run the stimulation script. A zero passed in will tell it to run indefinately until it is either stopped or paused by the user. Other values include between 1 and 65,535 repetitions. Can not be called during a beginningOfSequence and endOfSequence command call.
        
        times: Number of times to execute the stimulation script 0 means indefinately
        """
    def read_device_info(self, output: DeviceInfo) -> ResultType:
        """
        This returns all the information about the CereStim 96 that is connected to. It will tell its part number, serial number, firmware versions for both the motherboard and for the current modules. It will also tell you the protocol that the motherboard is using with the current modules and the number of installed current modules.
        
        output: Pointer to a BDeviceInfo structure, the structure will be populated with the CereStim's information
        """
    def read_eeprom(self, output: ReadEEPROMOutput) -> ResultType:
        """
        Reads the CereStim 96 motherboards EEprom and returns all values
        
        output: Pointer to array of UINT8[256]
        """
    def read_hardware_values(self, output: ReadHardwareValuesOutput) -> ResultType:
        """
        Reads the hardware values that are set based on the part number
        
        output: Structure containing the hardware values
        """
    def read_sequence_status(self, output: SequenceStatus) -> ResultType:
        """
        Can be called anytime as it does not interrupt other functions from executing, but simply reads what state the stimulator is in.
        
        output: Pointer to a BSequenceStatus that gets populate with the value from the CereStim 96
        """
    def read_stimulus_pattern(self, output: StimulusConfiguration, configID: Config) -> ResultType:
        """
        Reads back all of the parameters associated with a specific stimulation waveform and stores it in the structure supplied by the user
        
        output: Pointer to a BStimulusConfiguration structure which contains all the parameters that consist in a stimulation waveform
        configID: The stimulation waveform that is being read back
        """
    def reset_stimulator(self) -> ResultType:
        """
        Administrative command that will call the reset interrupt vector on the uController User will need to call Connect after calling this.
        """
    def set_device(self, device_index: int) -> ResultType:
        """
        Using the index of the device in the serial number list obtained from scanForDevices(), set the device you want to connect.
        """
    def stimulus_max_values(self, output: MaximumValues, rw: int, voltage: OCVolt, amplitude: int, phase_charge: int, frequency: int) -> ResultType:
        """
        Intended to be an administrative interface that can be password protected and only allow the lead researcher to make changes. It allows the user to set other determined upper limits for the stimulation parameters for whatever safety protocol they are requireing. Again micro and macro stimulators will have some different bounds for setting max values due to the different ranges each are able to achieve.
        
        output: Pointer to a BMaximumValues structure that will contain the current max values that are set
        rw: Boolean to determine if updating new max values or just reading the old Read = 0 and Write = 1
        voltage: The Max Compliance Voltage that can be set
        amplitude: The Max amplitude that can be used in a stimulation
        phase_charge: The Max charge per phase that will be allowed (Charge = Amplitude * Width)
        frequency: The Max frequency at which the stimulations can take place
        """
    def stop(self) -> ResultType:
        """
        This will stop a currently running stimulation script and reset it so when played again it will begin from the first command. Can only be called while the stimulator has a status of stimulating or paused.
        """
    def stop_trigger_stimulus(self) -> ResultType:
        """
        Changes the state of the stimulator so that it is no longer waiting for a trigger. Frees up the stimulator for other commands to be called.
        """
    def test_electrodes(self, output: TestElectrodes) -> ResultType:
        """
        This is a diagnostic tool that can be used to help determine which electrodes are good and which ones are bad. The stimulator will send out a known stimulus configuration, (Config_0), and measure the voltage it returns. Off of these values the relative impedance calculated and returned.
        
        output: Pointer to a BTestElectrodes Structure which will contain all the information from all the channels.
        """
    def test_modules(self, output: TestModules) -> ResultType:
        """
        Used as a way to diagnose the current modules that reside in the stimulator to determine if there output voltage levels are okay and ensure that they continue to function at the right levels over time. A known stimulus is applied to a known load and the voltage is compared to what it should be.
        
        output: Pointer to a BTestModules structure which will contain the status of all the current modules
        """
    def trigger_stimulus(self, edge: TriggerType) -> ResultType:
        """
        Allows the stimulator to wait for a trigger event before executing a stimulation script. The stimulator has an external TTL Trigger input port that uses TTL logic levels to determine wheather the input is high or low. The stimulator can be set to fire on a rising edge, falling edge, or any edge transition. Once in trigger mode the stimulator is locked down from other function calls except for stopTriggerStimulus
        
        edge: The type of digital event to trigger the stimulation on
        """
    def update_electrode_channel_map(self, input: ElectrodeChannelMap) -> ResultType:
        """
        Since not all electrodes are found on channel 1 this function allows the user to create a map key pair where the channel is an index into an array which holds the value of the electrode at that channel.
        """
    def wait(self, milliseconds: int) -> ResultType:
        """
        This command can only be used within a stimulation script and is capable of adding a wait of up to 65,535 milliseconds.
        
        milliseconds: The number of milliseconds to wait before executing the next command
        """
    def write_eeprom(self, addr: int, val: int) -> ResultType:
        ...
class StimulatorType:
    """
    Members:
    
      micro_stim : Micro Stimulator
    
      macro_stim : Macro Stimulator
    
      invalid_stim : Invalid.
    """
    __members__: typing.ClassVar[dict[str, StimulatorType]]  # value = {'micro_stim': <StimulatorType.micro_stim: 0>, 'macro_stim': <StimulatorType.macro_stim: 1>, 'invalid_stim': <StimulatorType.invalid_stim: 2>}
    invalid_stim: typing.ClassVar[StimulatorType]  # value = <StimulatorType.invalid_stim: 2>
    macro_stim: typing.ClassVar[StimulatorType]  # value = <StimulatorType.macro_stim: 1>
    micro_stim: typing.ClassVar[StimulatorType]  # value = <StimulatorType.micro_stim: 0>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class StimulusConfiguration:
    """
    The stimulator is capable of custom configuring a biphasic stimulus. The amplitudes and widths and frequency are all a part of the components that can be configured. The main restriction is that the two phases are balanced, i.e. width * amp of phase 1 is equal to width * amp of phase 2.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
        Components of the Stimulus Configurations.
        """
    @property
    def amp1(self) -> int:
        """
        Amplitude first phase (uA)
        """
    @amp1.setter
    def amp1(self, arg0: int) -> None:
        ...
    @property
    def amp2(self) -> int:
        """
        Amplitude second phase (uA)
        """
    @amp2.setter
    def amp2(self, arg0: int) -> None:
        ...
    @property
    def anodicFirst(self) -> int:
        """
        0x01 = anodic first, 0x00 = cathodic first
        """
    @anodicFirst.setter
    def anodicFirst(self, arg0: int) -> None:
        ...
    @property
    def frequency(self) -> int:
        """
        Frequency of stimulation pulses (Hz)
        """
    @frequency.setter
    def frequency(self, arg0: int) -> None:
        ...
    @property
    def interphase(self) -> int:
        """
        Time between phases (us)
        """
    @interphase.setter
    def interphase(self, arg0: int) -> None:
        ...
    @property
    def pulses(self) -> int:
        """
        Number of biphasic pulses (from 1 to 255)
        """
    @pulses.setter
    def pulses(self, arg0: int) -> None:
        ...
    @property
    def width1(self) -> int:
        """
        Width first phase (us)
        """
    @width1.setter
    def width1(self, arg0: int) -> None:
        ...
    @property
    def width2(self) -> int:
        """
        Width second phase (us)
        """
    @width2.setter
    def width2(self, arg0: int) -> None:
        ...
class TestElectrodes:
    """
    The stimulator allows for diagnosising the status of the electrodes attached to it. A known stimulus is sent to each electrode and the voltage is recorded for the five data points during a stimulation, i.e. before the first phase, during the first phase, between the two phases, during the second phase and after the second phase. These voltage levels are then used along with the known stimulation to calculate the impedance of each electrode. A 1 kHz frequency is used for the stimulation.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
        Electrode Diagnostics.
        """
    @property
    def electrodes(self) -> typing.Annotated[list[typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(5)]], pybind11_stubgen.typing_ext.FixedSize(97)]:
        """
        5 voltage measurements for all 96 channels reported in millivolts
        """
    @property
    def impedance(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(97)]:
        """
        Real part of Impedance of each electrode reported in Ohms.
        """
class TestModules:
    """
    The stimulator uses current modules to deliver stimulus through electrodes. These modules may become damaged and so the stimulator uses a known load and stimulus parameter to determine if the voltage levels on the current module are as they should be.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
        Module Diagnostics.
        """
    @property
    def modules_mv(self) -> typing.Annotated[list[typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(5)]], pybind11_stubgen.typing_ext.FixedSize(16)]:
        """
        5 voltage measurements for all current modules reported in millivolts
        """
    @property
    def modules_status(self) -> typing.Annotated[list[ModuleStatus], pybind11_stubgen.typing_ext.FixedSize(16)]:
        """
        Status of each current module.
        """
class TriggerType:
    """
    The stimulator is able to begin stimulating based on an external TTL logic. The Trigger type defines the possible trigger methods. It can be set to trigger on a low to high transistion, a high to low transistion, or any transistion.
    
    Members:
    
      trigger_disabled : Trigger mode is currently turned off.
    
      trigger_rising : Trigger on a low to high transistion.
    
      trigger_falling : Trigger on a high to low transistion
    
      trigger_change : Trigger on any transistion.
    
      trigger_invalid : Invalid Trigger, Always the last value
    """
    __members__: typing.ClassVar[dict[str, TriggerType]]  # value = {'trigger_disabled': <TriggerType.trigger_disabled: 0>, 'trigger_rising': <TriggerType.trigger_rising: 1>, 'trigger_falling': <TriggerType.trigger_falling: 2>, 'trigger_change': <TriggerType.trigger_change: 3>, 'trigger_invalid': <TriggerType.trigger_invalid: 4>}
    __entries: typing.ClassVar[dict[str, tuple[TriggerType, str]]]
    trigger_change: typing.ClassVar[TriggerType]  # value = <TriggerType.trigger_change: 3>
    trigger_disabled: typing.ClassVar[TriggerType]  # value = <TriggerType.trigger_disabled: 0>
    trigger_falling: typing.ClassVar[TriggerType]  # value = <TriggerType.trigger_falling: 2>
    trigger_invalid: typing.ClassVar[TriggerType]  # value = <TriggerType.trigger_invalid: 4>
    trigger_rising: typing.ClassVar[TriggerType]  # value = <TriggerType.trigger_rising: 1>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class USBParams:
    """
    The USB parameters that need to be configured in order to have the stimulator object actually connect with the CereStim 96 over usb.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
        USB Parameters
        """
    @property
    def pid(self) -> int:
        """
        product ID
        """
    @pid.setter
    def pid(self, arg0: int) -> None:
        ...
    @property
    def size(self) -> int:
        """
        sizeof(BStimUsbParams)
        """
    @size.setter
    def size(self, arg0: int) -> None:
        ...
    @property
    def timeout(self) -> int:
        """
        How long to try before timeout (ms)
        """
    @timeout.setter
    def timeout(self, arg0: int) -> None:
        ...
    @property
    def vid(self) -> int:
        """
        vendor ID
        """
    @vid.setter
    def vid(self, arg0: int) -> None:
        ...
class Version:
    """
    Gives the current version of the API that is being used.
    """
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
        API Version.
        """
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    @property
    def beta(self) -> int:
        """
        Whether the Version is Beta.
        """
    @beta.setter
    def beta(self, arg0: int) -> None:
        ...
    @property
    def major(self) -> int:
        """
        Major Version.
        """
    @major.setter
    def major(self, arg0: int) -> None:
        ...
    @property
    def minor(self) -> int:
        """
        Minor Version.
        """
    @minor.setter
    def minor(self, arg0: int) -> None:
        ...
    @property
    def release(self) -> int:
        """
        Wether the Version is Released.
        """
    @release.setter
    def release(self, arg0: int) -> None:
        ...
class WFType:
    """
    The Stimulator is capable of outputting a biphasic current pulse. the BWFType enumerator allows the user to determine what the polarity is of the first phase of the biphasic pulse.
    
    Members:
    
      wf_anodic_first : The first phase is anodic.
    
      wf_cathodic_first : The first phase is cathodic.
    
      wf_invalid : Invalid Selection, always the last one.
    """
    __members__: typing.ClassVar[dict[str, WFType]]  # value = {'wf_anodic_first': <WFType.wf_anodic_first: 0>, 'wf_cathodic_first': <WFType.wf_cathodic_first: 1>, 'wf_invalid': <WFType.wf_invalid: 2>}
    __entries: typing.ClassVar[dict[str, tuple[WFType, str]]]
    wf_anodic_first: typing.ClassVar[WFType]  # value = <WFType.wf_anodic_first: 0>
    wf_cathodic_first: typing.ClassVar[WFType]  # value = <WFType.wf_cathodic_first: 1>
    wf_invalid: typing.ClassVar[WFType]  # value = <WFType.wf_invalid: 2>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class vector_UINT32:
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: int) -> bool:
        """
        Return true the container contains ``x``
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None:
        """
        Delete list elements using a slice object
        """
    def __eq__(self, arg0: vector_UINT32) -> bool:
        ...
    @typing.overload
    def __getitem__(self, s: slice) -> vector_UINT32:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, arg0: int) -> int:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: vector_UINT32) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None:
        ...
    def __iter__(self) -> typing.Iterator[int]:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: vector_UINT32) -> bool:
        ...
    def __repr__(self) -> str:
        """
        Return the canonical string representation of this list.
        """
    @typing.overload
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: vector_UINT32) -> None:
        """
        Assign list elements using a slice object
        """
    def append(self, x: int) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: int) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: vector_UINT32) -> None:
        """
        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None:
        """
        Extend the list by appending all the items in the given list
        """
    def insert(self, i: int, x: int) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> int:
        """
        Remove and return the last item
        """
    @typing.overload
    def pop(self, i: int) -> int:
        """
        Remove and return the item at index ``i``
        """
    def remove(self, x: int) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
BANK_SIZE: int = 32
EEPROM_SIZE: int = 256
MAX_CHANNELS: int = 97
MAX_CONFIGURATIONS: int = 16
MAX_MODULES: int = 16
NUMBER_VOLT_MEAS: int = 5
PN6425: PartNumbers  # value = <PartNumbers.PN6425: 0>
PN7008: PartNumbers  # value = <PartNumbers.PN7008: 1>
PN7039: PartNumbers  # value = <PartNumbers.PN7039: 2>
PN7169: PartNumbers  # value = <PartNumbers.PN7169: 3>
PN7655: PartNumbers  # value = <PartNumbers.PN7655: 5>
PN7656: PartNumbers  # value = <PartNumbers.PN7656: 6>
PN7875: PartNumbers  # value = <PartNumbers.PN7875: 7>
PN8543: PartNumbers  # value = <PartNumbers.PN8543: 4>
PN8544: PartNumbers  # value = <PartNumbers.PN8544: 8>
PN_invalid: PartNumbers  # value = <PartNumbers.PN_invalid: 9>
amp_great_max: ResultType  # value = <ResultType.amp_great_max: -124>
callback_all: CallbackType  # value = <CallbackType.callback_all: 0>
callback_count: CallbackType  # value = <CallbackType.callback_count: 2>
callback_device_attachment: CallbackType  # value = <CallbackType.callback_device_attachment: 1>
callback_reg_failed: ResultType  # value = <ResultType.callback_reg_failed: -21>
channel_used_in_group: ResultType  # value = <ResultType.channel_used_in_group: -119>
config_0: Config  # value = <Config.config_0: 0>
config_1: Config  # value = <Config.config_1: 1>
config_10: Config  # value = <Config.config_10: 10>
config_11: Config  # value = <Config.config_11: 11>
config_12: Config  # value = <Config.config_12: 12>
config_13: Config  # value = <Config.config_13: 13>
config_14: Config  # value = <Config.config_14: 14>
config_15: Config  # value = <Config.config_15: 15>
config_2: Config  # value = <Config.config_2: 2>
config_3: Config  # value = <Config.config_3: 3>
config_4: Config  # value = <Config.config_4: 4>
config_5: Config  # value = <Config.config_5: 5>
config_6: Config  # value = <Config.config_6: 6>
config_7: Config  # value = <Config.config_7: 7>
config_8: Config  # value = <Config.config_8: 8>
config_9: Config  # value = <Config.config_9: 9>
config_count: Config  # value = <Config.config_count: 16>
config_not_active: ResultType  # value = <ResultType.config_not_active: -120>
connected: ResultType  # value = <ResultType.connected: -10>
device_locked: ResultType  # value = <ResultType.device_locked: -131>
device_notify: ResultType  # value = <ResultType.device_notify: -13>
device_registered: ResultType  # value = <ResultType.device_registered: -7>
disconnected: ResultType  # value = <ResultType.disconnected: -9>
echo_error: ResultType  # value = <ResultType.echo_error: -132>
empty_config: ResultType  # value = <ResultType.empty_config: -121>
event_count: EventType  # value = <EventType.event_count: 2>
event_device_attached: EventType  # value = <EventType.event_device_attached: 0>
event_device_detached: EventType  # value = <EventType.event_device_detached: 1>
freq_period_zero: ResultType  # value = <ResultType.freq_period_zero: -23>
frequency_great_max: ResultType  # value = <ResultType.frequency_great_max: -130>
interface_count: InterfaceType  # value = <InterfaceType.interface_count: 3>
interface_cpusb: InterfaceType  # value = <InterfaceType.interface_cpusb: 2>
interface_default: InterfaceType  # value = <InterfaceType.interface_default: 0>
interface_read: ResultType  # value = <ResultType.interface_read: -16>
interface_timeout: ResultType  # value = <ResultType.interface_timeout: -6>
interface_write: ResultType  # value = <ResultType.interface_write: -15>
interface_wusb: InterfaceType  # value = <InterfaceType.interface_wusb: 1>
invalid: SeqType  # value = <SeqType.invalid: 5>
invalid_afcf: ResultType  # value = <ResultType.invalid_afcf: -110>
invalid_amplitude: ResultType  # value = <ResultType.invalid_amplitude: -109>
invalid_callback_type: ResultType  # value = <ResultType.invalid_callback_type: -20>
invalid_channel: ResultType  # value = <ResultType.invalid_channel: -104>
invalid_command: ResultType  # value = <ResultType.invalid_command: -14>
invalid_config: ResultType  # value = <ResultType.invalid_config: -105>
invalid_fastdisch: ResultType  # value = <ResultType.invalid_fastdisch: -115>
invalid_frequency: ResultType  # value = <ResultType.invalid_frequency: -129>
invalid_handle: ResultType  # value = <ResultType.invalid_handle: -3>
invalid_interface: ResultType  # value = <ResultType.invalid_interface: -5>
invalid_interphase: ResultType  # value = <ResultType.invalid_interphase: -114>
invalid_interpulse: ResultType  # value = <ResultType.invalid_interpulse: -113>
invalid_module: ResultType  # value = <ResultType.invalid_module: -116>
invalid_module_enum: ResultType  # value = <ResultType.invalid_module_enum: -19>
invalid_number: ResultType  # value = <ResultType.invalid_number: -106>
invalid_params: ResultType  # value = <ResultType.invalid_params: -8>
invalid_pulses: ResultType  # value = <ResultType.invalid_pulses: -111>
invalid_rwr: ResultType  # value = <ResultType.invalid_rwr: -107>
invalid_stim: StimulatorType  # value = <StimulatorType.invalid_stim: 2>
invalid_trigger: ResultType  # value = <ResultType.invalid_trigger: -103>
invalid_voltage: ResultType  # value = <ResultType.invalid_voltage: -108>
invalid_width: ResultType  # value = <ResultType.invalid_width: -112>
library_firmware: ResultType  # value = <ResultType.library_firmware: -22>
macro_stim: StimulatorType  # value = <StimulatorType.macro_stim: 1>
micro_stim: StimulatorType  # value = <StimulatorType.micro_stim: 0>
module_count: ModuleStatus  # value = <ModuleStatus.module_count: 5>
module_disabled: ResultType  # value = <ResultType.module_disabled: -127>
module_enabled: ResultType  # value = <ResultType.module_enabled: -128>
module_ok: ModuleStatus  # value = <ModuleStatus.module_ok: 3>
module_unavailable: ResultType  # value = <ResultType.module_unavailable: -118>
module_voltagelimitation: ModuleStatus  # value = <ModuleStatus.module_voltagelimitation: 4>
no_device_selected: ResultType  # value = <ResultType.no_device_selected: -24>
nok: ResultType  # value = <ResultType.nok: -100>
not_implemented: ResultType  # value = <ResultType.not_implemented: -1>
null_ptr: ResultType  # value = <ResultType.null_ptr: -4>
ocvolt4_7: OCVolt  # value = <OCVolt.ocvolt4_7: 7>
ocvolt5_3: OCVolt  # value = <OCVolt.ocvolt5_3: 8>
ocvolt5_9: OCVolt  # value = <OCVolt.ocvolt5_9: 9>
ocvolt6_5: OCVolt  # value = <OCVolt.ocvolt6_5: 10>
ocvolt7_1: OCVolt  # value = <OCVolt.ocvolt7_1: 11>
ocvolt7_7: OCVolt  # value = <OCVolt.ocvolt7_7: 12>
ocvolt8_3: OCVolt  # value = <OCVolt.ocvolt8_3: 13>
ocvolt8_9: OCVolt  # value = <OCVolt.ocvolt8_9: 14>
ocvolt9_5: OCVolt  # value = <OCVolt.ocvolt9_5: 15>
ocvolt_invalid: OCVolt  # value = <OCVolt.ocvolt_invalid: 16>
pause: SeqType  # value = <SeqType.pause: 1>
phase_great_max: ResultType  # value = <ResultType.phase_great_max: -123>
phase_not_balanced: ResultType  # value = <ResultType.phase_not_balanced: -122>
playing: SeqType  # value = <SeqType.playing: 2>
read_err: ResultType  # value = <ResultType.read_err: -18>
return_: ResultType  # value = <ResultType.return_: 1>
sequence_error: ResultType  # value = <ResultType.sequence_error: -102>
stim_attached: ResultType  # value = <ResultType.stim_attached: -11>
stim_detached: ResultType  # value = <ResultType.stim_detached: -12>
stimuli_modules: ResultType  # value = <ResultType.stimuli_modules: -117>
stop: SeqType  # value = <SeqType.stop: 0>
success: ResultType  # value = <ResultType.success: 0>
trigger: SeqType  # value = <SeqType.trigger: 4>
trigger_change: TriggerType  # value = <TriggerType.trigger_change: 3>
trigger_disabled: TriggerType  # value = <TriggerType.trigger_disabled: 0>
trigger_falling: TriggerType  # value = <TriggerType.trigger_falling: 2>
trigger_invalid: TriggerType  # value = <TriggerType.trigger_invalid: 4>
trigger_rising: TriggerType  # value = <TriggerType.trigger_rising: 1>
unknown: ResultType  # value = <ResultType.unknown: -2>
volt_great_max: ResultType  # value = <ResultType.volt_great_max: -126>
wf_anodic_first: WFType  # value = <WFType.wf_anodic_first: 0>
wf_cathodic_first: WFType  # value = <WFType.wf_cathodic_first: 1>
wf_invalid: WFType  # value = <WFType.wf_invalid: 2>
width_great_max: ResultType  # value = <ResultType.width_great_max: -125>
write_err: ResultType  # value = <ResultType.write_err: -17>
writing: SeqType  # value = <SeqType.writing: 3>
