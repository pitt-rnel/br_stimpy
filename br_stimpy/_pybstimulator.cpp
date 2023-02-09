#include "_pybstimulator.h"

PYBIND11_MAKE_OPAQUE(std::vector<UINT32>);
//PYBIND11_MAKE_OPAQUE(std::vector<UINT16>);
//PYBIND11_MAKE_OPAQUE(std::vector<UINT8>);

namespace py = pybind11;
using namespace pybind11::literals;

std::vector<UINT32> scan_for_devices_wrap() { // wrap this static method to return vector instead of passing in by reference
    std::vector<UINT32> device_serial_nums;
    BResult res;
    res = BStimulator::scanForDevices(device_serial_nums);
    if (res)
        std::cerr << "Error from BStimulator::scanForDevices: " << res << std::endl;   
    //py::list dev_list = py::cast(device_serial_nums);
    //py::dict rdict("result"_a=res, "device_serial_nums"_a=dev_list);
    return device_serial_nums;
}

std::array<UINT16, MAXMODULES> get_module_firmware_version_wrap(BStimulator *stimulator) {
    UINT16 versions[MAXMODULES];
    BResult res = stimulator->getModuleFirmwareVersion(versions);
    if (res)
        std::cerr << "Error from BStimulator::getModuleFirmwareVersion: " << res << std::endl;
    std::array<UINT16, MAXMODULES> output;
    std::copy(std::begin(versions), std::end(versions), output.begin());
    return output;
}

std::array<UINT8, MAXMODULES> get_module_status_wrap(BStimulator *stimulator) {
    UINT8 status[MAXMODULES];
    BResult res = stimulator->getModuleStatus(status);
    if (res)
        std::cerr << "Error from BStimulator::getModuleStatus: " << res << std::endl;
    std::array<UINT8, MAXMODULES> output;
    std::copy(std::begin(status), std::end(status), output.begin());
    return output;
}

std::array<INT16, NUMBER_VOLT_MEAS> get_output_measurement(BOutputMeasurement *output_measurement){ //getter to convert int16 array to vector
    std::array<INT16, NUMBER_VOLT_MEAS>  out;
    std::copy(std::begin(output_measurement->measurement), std::end(output_measurement->measurement), out.begin());
    return out;
}

std::array<UINT8, MAXMODULES> get_module_status(BDeviceInfo *device_info){ //getter to convert array to vector
    std::array<UINT8, MAXMODULES> out;
    std::copy(std::begin(device_info->moduleStatus), std::end(device_info->moduleStatus), out.begin());
    return out;
}

std::array<UINT16, MAXMODULES> get_module_version(BDeviceInfo *device_info){ //getter to convert array to vector
    std::array<UINT16, MAXMODULES> out;
    std::copy(std::begin(device_info->moduleVersion), std::end(device_info->moduleVersion), out.begin());
    return out;
}

Matrix<INT16, MAXCHANNELS, NUMBER_VOLT_MEAS> get_test_electrodes_meas(BTestElectrodes *test_electrodes){
    Matrix<INT16, MAXCHANNELS, NUMBER_VOLT_MEAS> out;
    for (int i=0; i< MAXCHANNELS; i++){
        for (int j=0; j< NUMBER_VOLT_MEAS; j++){
            out[i][j] = test_electrodes->electrodes[i][j];
        }
    }
    return out;
}

std::array<UINT32, MAXCHANNELS> get_test_electrodes_imp(BTestElectrodes *test_electrodes){ //getter to convert array to vector
    std::array<UINT32, MAXCHANNELS> out;
    std::copy(std::begin(test_electrodes->impedance), std::end(test_electrodes->impedance), out.begin());
    return out;
}

Matrix<INT16, MAXMODULES, NUMBER_VOLT_MEAS> get_modules_mv(BTestModules *testModules){
    Matrix<INT16, MAXMODULES, NUMBER_VOLT_MEAS> out;
    for (int i=0; i< MAXMODULES; i++){
        for (int j=0; j< NUMBER_VOLT_MEAS; j++){
            out[i][j] = testModules->modulesMV[i][j];
        }
    }
    return out;
}

std::array<BModuleStatus, MAXMODULES> get_test_modules_status(BTestModules *testModules){
    std::array<BModuleStatus, MAXMODULES> out;
    std::copy(std::begin(testModules->modulesStatus), std::end(testModules->modulesStatus), out.begin());
    return out;
}

std::array<UINT8, MAXMODULES> get_group_electrodes(BGroupStimulus *group){
    std::array<UINT8, MAXMODULES> out;
    std::copy(std::begin(group->electrode), std::end(group->electrode), out.begin());
    return out;
}

void set_group_electrodes(BGroupStimulus *group, std::array<UINT8, MAXMODULES> electrode){
    std::copy(electrode.begin(), electrode.end(), std::begin(group->electrode));
}
    

std::array<UINT8, MAXMODULES> get_group_pattern(BGroupStimulus *group){
    std::array<UINT8, MAXMODULES> out;
    std::copy(std::begin(group->pattern), std::end(group->pattern), out.begin());
    return out;
}

void set_group_pattern(BGroupStimulus *group, std::array<UINT8, MAXMODULES> pattern){
    std::copy(pattern.begin(), pattern.end(), std::begin(group->pattern));
}

std::array<UINT8, EEPROM_SIZE> get_eeprom(BReadEEpromOutput* eeprom_output){
    std::array<UINT8, EEPROM_SIZE> out;
    std::copy(std::begin(eeprom_output->eeprom), std::end(eeprom_output->eeprom), out.begin());
    return out;
}

std::array<UINT8, BANKSIZE> get_bankA(BElectrodeChannelMap *map){
    std::array<UINT8, BANKSIZE> out;
    std::copy(std::begin(map->bankA), std::end(map->bankA), out.begin());
    return out;
}

std::array<UINT8, BANKSIZE> get_bankB(BElectrodeChannelMap *map){
    std::array<UINT8, BANKSIZE> out;
    std::copy(std::begin(map->bankB), std::end(map->bankB), out.begin());
    return out;
}

std::array<UINT8, BANKSIZE> get_bankC(BElectrodeChannelMap *map){
    std::array<UINT8, BANKSIZE> out;
    std::copy(std::begin(map->bankC), std::end(map->bankC), out.begin());
    return out;
}

void set_bankA(BElectrodeChannelMap *map, std::array<UINT8, BANKSIZE> bank){
    std::copy(bank.begin(), bank.end(), std::begin(map->bankA));
}

void set_bankB(BElectrodeChannelMap *map, std::array<UINT8, BANKSIZE> bank){
    std::copy(bank.begin(), bank.end(), std::begin(map->bankB));
}

void set_bankC(BElectrodeChannelMap *map, std::array<UINT8, BANKSIZE> bank){
    std::copy(bank.begin(), bank.end(), std::begin(map->bankC));
}

PYBIND11_MODULE(_bstimulator, m) {
    m.attr("__name__") = "br_stimpy._bstimulator";
    m.doc() = "br_stimpy._bstimulator: CereStim Python SDK. Wrap of BStimulator.h using pybind11.";

    m.attr("MAX_MODULES") = MAXMODULES;
    m.attr("MAX_CHANNELS") = MAXCHANNELS;
    m.attr("BANK_SIZE") = BANKSIZE;
    m.attr("EEPROM_SIZE") = EEPROM_SIZE;
    m.attr("NUMBER_VOLT_MEAS") = NUMBER_VOLT_MEAS;
    m.attr("MAX_CONFIGURATIONS") = MAXCONFIGURATIONS;

    py::bind_vector<std::vector<UINT32>>(m, "vector_UINT32");
    //py::bind_vector<std::vector<UINT16>>(m, "vector_UINT16");
    //py::bind_vector<std::vector<UINT8>>(m, "vector_UINT8");
    
    py::enum_<BInterfaceType> interface_type(m, "interface_type",
        "The Stimulator was originally designed to be communicated via USB or RS232, and will be functional on multiple platforms. "
        "The RS232 interface no longer exists. Default type should generally be used.");
    interface_type.value("interface_default", BInterfaceType::BINTERFACE_DEFAULT, "Default interface (windows USB)")
        .value("interface_wusb",  BInterfaceType::BINTERFACE_WUSB, "Windows USB interface.");
#ifdef _WIN32 // __if_exists keyword is in windows but is not standard c++, not in gcc
    __if_exists(BInterfaceType::BINTERFACE_CPUSB) { // experimental cross-platform USB interface, not in standard header
        interface_type.value("interface_cpusb",  BInterfaceType::BINTERFACE_CPUSB, "Experimental cross-platform USB interface."); 
    };
#else
    interface_type.value("interface_cpusb",  BInterfaceType::BINTERFACE_CPUSB, "Experimental cross-platform USB interface.");
#endif    
    interface_type.value("interface_count",  BInterfaceType::BINTERFACE_COUNT, "Number of Interfaces, always the last one.")
        .export_values();

    py::enum_<BWFType> wf_type(m, "WFType", 
        "The Stimulator is capable of outputting a biphasic current pulse. the BWFType enumerator allows the user to determine what the polarity is of the first phase of the biphasic pulse.");
    wf_type.value("wf_anodic_first", BWFType::BWF_ANODIC_FIRST, "The first phase is anodic.")
        .value("wf_cathodic_first", BWFType::BWF_CATHODIC_FIRST, "The first phase is cathodic.")
        .value("wf_invalid", BWFType::BWF_INVALID, "Invalid Selection, always the last one.")
        .export_values();

    py::enum_<BSeqType> seq_type(m, "SeqType", 
        "The Stimulator has internal states, and based on those states the stimulator is allowed to perform different functions. The SeqType enumerator lists all the valid states.");
    seq_type.value("stop", BSeqType::BSEQ_STOP, "The stimulator is stopped.")
        .value("pause"  , BSeqType::BSEQ_PAUSE, "The stimulator is paused.")
        .value("playing", BSeqType::BSEQ_PLAYING, "The stimulator is actively delivering a stimulus.")
        .value("writing", BSeqType::BSEQ_WRITING, "A stimulus sequence is being written to the stimulator.")
        .value("trigger", BSeqType::BSEQ_TRIGGER, "The stimulator is waiting for a trigger on its trigger line.")
        .value("invalid", BSeqType::BSEQ_INVALID, "Invalid Sequence, Always the last value.")
        .export_values();

    py::enum_<BTriggerType>(m, "TriggerType", 
        "The stimulator is able to begin stimulating based on an external TTL logic. The Trigger type defines the possible trigger methods. It can be set to trigger on a "
        "low to high transistion, a high to low transistion, or any transistion.")
        .value("trigger_disabled", BTriggerType::BTRIGGER_DISABLED, "Trigger mode is currently turned off.")
        .value("trigger_rising", BTriggerType::BTRIGGER_RISING, "Trigger on a low to high transistion.")
        .value("trigger_falling", BTriggerType::BTRIGGER_FALLING, "Trigger on a high to low transistion")
        .value("trigger_change", BTriggerType::BTRIGGER_CHANGE, "Trigger on any transistion.")
        .value("trigger_invalid", BTriggerType::BTRIGGER_INVALID, "Invalid Trigger, Always the last value")
        .export_values();

    py::enum_<BModuleStatus>(m, "ModuleStatus",
        "The stimulator is capable of housing up to 16 current modules. Each current module can have several states based on how the user has configured the stimulator. "
        "The current modules are also capable of returning problem statuses based on the hardware.")
        .value("module_unavailable", BModuleStatus::BMODULE_UNAVAILABLE, "No current module in the specified position.")
        .value("module_enabled", BModuleStatus::BMODULE_ENABLED, "Current module in the specified position is enabled.")
        .value("module_disabled", BModuleStatus::BMODULE_DISABLED, "Current Module in the specified position is disabled.")
        .value("module_ok", BModuleStatus::BMODULE_OK, "Voltage levels on the current module are normal.")
        .value("module_voltagelimitation", BModuleStatus::BMODULE_VOLTAGELIMITATION, "Voltage levels on the current module are below normal, Module is bad.")
        .value("module_count", BModuleStatus::BMODULE_COUNT, "Number of Statuses, Always the Last one.")
        .export_values();

    py::enum_<BConfig>(m, "Config",
        "The stimulator is capable of storing up to 16 stimulus waveforms that can then be used in any stimulus. Each waveform is indepently configured by the user. "
        "The user can use different stimulus waveforms based on some predetermined signal based on feedback from the neural signals.")
        .value("config_0", BConfig::BCONFIG_0,   "Stimulation waveform configuration 0.")
        .value("config_1", BConfig::BCONFIG_1,   "Stimulation waveform configuration 1.")
        .value("config_2", BConfig::BCONFIG_2,   "Stimulation waveform configuration 2.")
        .value("config_3", BConfig::BCONFIG_3,   "Stimulation waveform configuration 3.")
        .value("config_4", BConfig::BCONFIG_4,   "Stimulation waveform configuration 4.")
        .value("config_5", BConfig::BCONFIG_5,   "Stimulation waveform configuration 5.")
        .value("config_6", BConfig::BCONFIG_6,   "Stimulation waveform configuration 6.")
        .value("config_7", BConfig::BCONFIG_7,   "Stimulation waveform configuration 7.")
        .value("config_8", BConfig::BCONFIG_8,   "Stimulation waveform configuration 8.")
        .value("config_9", BConfig::BCONFIG_9,   "Stimulation waveform configuration 9.")
        .value("config_10", BConfig::BCONFIG_10, "Stimulation waveform configuration 10.")
        .value("config_11", BConfig::BCONFIG_11, "Stimulation waveform configuration 11.")
        .value("config_12", BConfig::BCONFIG_12, "Stimulation waveform configuration 12.")
        .value("config_13", BConfig::BCONFIG_13, "Stimulation waveform configuration 13.")
        .value("config_14", BConfig::BCONFIG_14, "Stimulation waveform configuration 14.")
        .value("config_15", BConfig::BCONFIG_15, "Stimulation waveform configuration 15.")
        .value("config_count", BConfig::BCONFIG_COUNT, "Total Configurations, Always the Last one.")
        .export_values();

    py::enum_<BOCVolt>(m, "OCVolt",
        "The Stimulator is capable of setting different output compliance voltage levels based on the users needs and safety considerations.")
        .value("ocvolt4_7", BOCVolt::BOCVOLT4_7, "Output Voltage Level 4.7V.")
        .value("ocvolt5_3", BOCVolt::BOCVOLT5_3, "Output Voltage Level 5.3V.")
        .value("ocvolt5_9", BOCVolt::BOCVOLT5_9, "Output Voltage Level 5.9V.")
        .value("ocvolt6_5", BOCVolt::BOCVOLT6_5, "Output Voltage Level 6.5V.")
        .value("ocvolt7_1", BOCVolt::BOCVOLT7_1, "Output Voltage Level 7.1V.")
        .value("ocvolt7_7", BOCVolt::BOCVOLT7_7, "Output Voltage Level 7.7V.")
        .value("ocvolt8_3", BOCVolt::BOCVOLT8_3, "Output Voltage Level 8.3V.")
        .value("ocvolt8_9", BOCVolt::BOCVOLT8_9, "Output Voltage Level 8.9V.")
        .value("ocvolt9_5", BOCVolt::BOCVOLT9_5, "Output Voltage Level 9.5V.")
        .value("ocvolt_invalid", BOCVolt::BOCVOLT_INVALID, "Invalid Compliance Voltage, Always the Last One.")
        .export_values();

    py::enum_<BPartNumbers>(m, "PartNumbers",
        "There are many versions of the stimulator. There are research versions of micro and macro stimulators, each with varying number of installed current modules; "
        "and there is a clinical version of the macro stimulator with a single current module. The part number of the device sets internal safety levels of what "
        "stimulation parameters are allowed.")
        .value("PN6425", BPartNumbers::PN6425, "CereStim R96 Micro Stimulator Beta Unit, May be either a 3 or 16 current module unit.")
        .value("PN7008", BPartNumbers::PN7008, "CereStim R96 Micro Stimulator 3 current module unit.")
        .value("PN7039", BPartNumbers::PN7039, "CereStim R96 Micro Stimulator 16 current module unit.")
        .value("PN7169", BPartNumbers::PN7169, "CereStim R96 Micro Stimulator 1 current module unit.")
        .value("PN8543", BPartNumbers::PN8543, "CereStim R96 Micro Stimulator Customer Specified Configuration.")
        .value("PN7655", BPartNumbers::PN7655, "CereStim R96 Macro Stimulator 3 current module unit.")
        .value("PN7656", BPartNumbers::PN7656, "CereStim M96 Macro Stimulator Clinical 1 current module unit.")
        .value("PN7875", BPartNumbers::PN7875, "CereStim R96 Macro Stimulator 16 current module unit.")
        .value("PN8544", BPartNumbers::PN8544, "CereStim R96 Macro Stimulator Customer Specified Configuration.")
        .value("PN_invalid", BPartNumbers::PN_INVALID, "Invalid part number.")
        .export_values();

    py::enum_<BStimulatorType>(m, "StimulatorType")
        .value("micro_stim", BStimulatorType::MICRO_STIM, "Micro Stimulator")
        .value("macro_stim", BStimulatorType::MACRO_STIM, "Macro Stimulator")
        .value("invalid_stim", BStimulatorType::INVALID_STIM, "Invalid.")
        .export_values();

    py::enum_<BEventType>(m, "EventType", 
        "Since the stimulator is a HID, it can be plugged in and unplugged from the Host PC at will. The USB events capture the status of whether the device is attached or not.")
        .value("event_device_attached", BEventType::BEVENT_DEVICE_ATTACHED, "CereStim 96 is Attached to Host PC.")
        .value("event_device_detached", BEventType::BEVENT_DEVICE_DETACHED, "CereStim 96 is Detached from Host PC.")
        .value("event_count", BEventType::BEVENT_COUNT, "Number of Events, Always the last value")
        .export_values();

    py::enum_<BCallbackType>(m, "CallbackType", 
        "Once a connection with the stimulator has been made over the USB and a stimulator object is created, that object needs to be notified of any events that take place. "
        "This is handled through a callback function.")
        .value("callback_all", BCallbackType::BCALLBACK_ALL, "Monitor all events.")
        .value("callback_device_attachment", BCallbackType::BCALLBACK_DEVICE_ATTACHMENT, "Monitor device attachment.")
        .value("callback_count", BCallbackType::BCALLBACK_COUNT, "Number of Callback Types, Always the last value.")
        .export_values();

    // include callback function??
    // typedef void (* BCallback)(BEventType type, void* pCallbackData);

    py::enum_<BResult>(m, "Result",
        "A stimulator object creates a USB connection with the actual CereStim 96 and calls are made to it through the stimulator object. The stimulator object can return an "
        "error message (Software Error) or the CereStim 96 can return an error message (Hardware Error).")
        .value("return", BResult::BRETURN, "Software Error: Early returned warning.")
        .value("success", BResult::BSUCCESS, "Successful operation.")
        .value("not_implemented", BResult::BNOTIMPLEMENTED, "Software Error: Not implemented.")
        .value("unknown", BResult::BUNKNOWN, "Software Error: Unknown error.")
        .value("invalid_handle", BResult::BINVALIDHANDLE, "Software Error: Invalid handle.")
        .value("null_ptr", BResult::BNULLPTR, "Software Error: Null pointer.")
        .value("invalid_interface", BResult::BINVALIDINTERFACE, "Software Error: Invalid interface specified or interface not supported.")
        .value("interface_timeout", BResult::BINTERFACETIMEOUT, "Software Error: Timeout in creating the interface.")
        .value("device_registered", BResult::BDEVICEREGISTERED, "Software Error: Device with that address already connected.")
        .value("invalid_params", BResult::BINVALIDPARAMS, "Software Error: Invalid parameters.")
        .value("disconnected", BResult::BDISCONNECTED, "Software Error: Stim is disconnected, invalid operation.")
        .value("connected", BResult::BCONNECTED, "Software Error: Stim is connected, invalid operation.")
        .value("stim_attached", BResult::BSTIMATTACHED, "Software Error: Stim is attached, invalid operation.")
        .value("stim_detached", BResult::BSTIMDETACHED, "Software Error: Stim is detached, invalid operation.")
        .value("device_notify", BResult::BDEVICENOTIFY, "Software Error: Cannot register for device change notification.")
        .value("invalid_command", BResult::BINVALIDCOMMAND, "Software Error: Invalid command.")
        .value("interface_write", BResult::BINTERFACEWRITE, "Software Error: Cannot open interface for write.")
        .value("interface_read", BResult::BINTERFACEREAD, "Software Error: Cannot open interface for read.")
        .value("write_err", BResult::BWRITEERR, "Software Error: Cannot write command to the interface.")
        .value("read_err", BResult::BREADERR, "Software Error: Cannot read command from the interface.")
        .value("invalid_module_enum", BResult::BINVALIDMODULENUM, "Software Error: Invalid module number specified.")
        .value("invalid_callback_type", BResult::BINVALIDCALLBACKTYPE, "Software Error: Invalid callback type.")
        .value("callback_reg_failed", BResult::BCALLBACKREGFAILED, "Software Error: Callback register/unregister failed.")
        .value("library_firmware", BResult::BLIBRARYFIRMWARE, "Software Error: CereStim Firmware version not supported by SDK Library Version.")
        .value("freq_period_zero", BResult::BFREQPERIODZERO, "Software Error: Frequency or Period is zero and unable to be converted.")
        .value("no_device_selected", BResult::BNODEVICESELECTED, "Software Error: No physical device has been set. See setDevice() for help.")
        .value("nok", BResult::BNOK, "Hardware Error: Comamnd result not OK.")
        .value("sequence_error", BResult::BSEQUENCEERROR, "Hardware Error: Sequence Error.")
        .value("invalid_trigger", BResult::BINVALIDTRIGGER, "Hardware Error: Invalid Trigger.")
        .value("invalid_channel", BResult::BINVALIDCHANNEL, "Hardware Error: Invalid Channel.")
        .value("invalid_config", BResult::BINVALIDCONFIG, "Hardware Error: Invalid Configuration.")
        .value("invalid_number", BResult::BINVALIDNUMBER, "Hardware Error: Invalid Number.")
        .value("invalid_rwr", BResult::BINVALIDRWR, "Hardware Error: Invalid Read/Write.")
        .value("invalid_voltage", BResult::BINVALIDVOLTAGE, "Hardware Error: Invalid Voltage.")
        .value("invalid_amplitude", BResult::BINVALIDAMPLITUDE, "Hardware Error: Invalid Amplitude.")
        .value("invalid_afcf", BResult::BINVALIDAFCF, "Hardware Error: Invalid AF/CF.")
        .value("invalid_pulses", BResult::BINVALIDPULSES, "Hardware Error: Invalid Pulses.")
        .value("invalid_width", BResult::BINVALIDWIDTH, "Hardware Error: Invalid Width.")
        .value("invalid_interpulse", BResult::BINVALIDINTERPULSE, "Hardware Error: Invalid Interpulse.")
        .value("invalid_interphase", BResult::BINVALIDINTERPHASE, "Hardware Error: Invalid Interphase.")
        .value("invalid_fastdisch", BResult::BINVALIDFASTDISCH, "Hardware Error: Invalid Fast Discharge.")
        .value("invalid_module", BResult::BINVALIDMODULE, "Hardware Error: Invalid Module.")
        .value("stimuli_modules", BResult::BSTIMULIMODULES, "Hardware Error: More Stimuli than Modules.")
        .value("module_unavailable", BResult::BMODULEUNAVAILABLE, "Hardware Error: Module not Available.")
        .value("channel_used_in_group", BResult::BCHANNELUSEDINGROUP, "Hardware Error: Channel already used in Group.")
        .value("config_not_active", BResult::BCONFIGNOTACTIVE, "Hardware Error: Configuration not Active.")
        .value("empty_config", BResult::BEMPTYCONFIG, "Hardware Error: Empty Config.")
        .value("phase_not_balanced", BResult::BPHASENOTBALANCED, "Hardware Error: Phases not Balanced.")
        .value("phase_great_max", BResult::BPHASEGREATMAX, "Hardware Error: Phase Charge Greater than Max.")
        .value("amp_great_max", BResult::BAMPGREATMAX, "Hardware Error: Amplitude Greater than Max.")
        .value("width_great_max", BResult::BWIDTHGREATMAX, "Hardware Error: Width Greater than Max.")
        .value("volt_great_max", BResult::BVOLTGREATMAX, "Hardware Error: Voltage Greater than Max.")
        .value("module_disabled", BResult::BMODULEDISABLED, "Hardware Error: Module already disabled can't disable it.")
        .value("module_enabled", BResult::BMODULEENABLED, "Hardware Error: Module already enabled can't reenable it.")
        .value("invalid_frequency", BResult::BINVALIDFREQUENCY, "Hardware Error: Invalid Frequency.")
        .value("frequency_great_max", BResult::BFREQUENCYGREATMAX, "Hardware Error: The frequency is greater than the max value allowed.")
        .value("device_locked", BResult::BDEVICELOCKED, "Hardware Error: Device locked due to hardware mismatch or not being configured.")
        .value("echo_error", BResult::BECHOERROR, "Hardware Error: Command returned was not the same command sent.")
        .export_values();

    py::class_<BUsbParams> usb_params(m, "USBParams");
    usb_params.doc() = "The USB parameters that need to be configured in order to have the stimulator object actually connect with the CereStim 96 over usb.";   
    usb_params.def(py::init<>(), "USB Parameters")
        .def_readwrite("size", &BUsbParams::size, "sizeof(BStimUsbParams)")
        .def_readwrite("timeout", &BUsbParams::timeout, "How long to try before timeout (ms)")
        .def_readwrite("vid", &BUsbParams::vid, "vendor ID")
        .def_readwrite("pid", &BUsbParams::pid, "product ID");
    

    py::class_<BVersion> version(m, "Version");
    version.doc() = "Gives the current version of the API that is being used.";
    version.def(py::init<>(), "API Version.")
        .def_readwrite("major", &BVersion::major, "Major Version.")
        .def_readwrite("minor", &BVersion::minor, "Minor Version.")
        .def_readwrite("release", &BVersion::release, "Wether the Version is Released.")
        .def_readwrite("beta", &BVersion::beta, "Whether the Version is Beta.")
        .def("__str__", 
            [](const BVersion &v) {
                //std::string major = std::string(v.major);
                //std::string minor = std::string(v.minor);
                std::string dev = v.release ? "" : " dev";
                std::string beta = v.beta ? " beta" : "";
                std::ostringstream vstr;
                vstr << std::to_string(v.major) << "." << std::to_string(v.minor) << beta << dev;
                //return std::string("<bversion ") + major + "." + std::string(v.minor) + release + beta + ">";
                return vstr.str();
            }
        )
        .def("__repr__", 
            [](const BVersion &v) {
                //std::string major = std::string(v.major);
                //std::string minor = std::string(v.minor);
                std::string dev = v.release ? "" : " dev";
                std::string beta = v.beta ? " beta" : "";
                std::ostringstream vstr;
                vstr << "<_bstimulator.version " << std::to_string(v.major) << "." << std::to_string(v.minor) << beta << dev << ">";
                //return std::string("<bversion ") + major + "." + std::string(v.minor) + release + beta + ">";
                return vstr.str();
            }
        );


    py::class_<BOutputMeasurement> output_measurement(m, "OutputMeasurement");
    output_measurement.def(py::init<>(), "Measured Stimulus Voltage.")
        .def_property_readonly("measurement", &get_output_measurement, "Voltages are returned in millivolts.");
    output_measurement.doc() = "The stimulator is capable of sending out a stimulus using known values and measure the voltage that is returned at five locations during the course "
    "of that stimulation. The five values in order are as follows: Just before the first phase, during the first phase, in between phases, during the second phase, and just after the second phase.";

    py::class_<BMaxOutputVoltage> max_output_voltage(m, "MaxOutputVoltage");
    max_output_voltage.def(py::init<>(), "Measured Output Voltage.")
        .def_readwrite("milivolts", &BMaxOutputVoltage::miliVolts, "Voltages are returned in millivolts.");
    max_output_voltage.doc() = "The Stimulator is capable of measuring what its current output compliance voltage level is using a known impedance and stimulus parameters.";

    py::class_<BDeviceInfo> device_info(m, "DeviceInfo");
    device_info.def(py::init<>(), "CereStim 96 Device Specific Information.")
        .def_readwrite("serial_no", &BDeviceInfo::serialNo, "Hardware part number, type, and serial number 0xPN TY SN SN.")
        .def_readwrite("mainboard_version", &BDeviceInfo::mainboardVersion, "MSB = version , LSB = subversion (i.e. 0x020A = version 2.10)")
        .def_readwrite("protocol_version", &BDeviceInfo::protocolVersion, "MSB = version , LSB = subversion (i.e. 0x020A = version 2.10)")
        .def_property_readonly("module_status", &get_module_status, "0x00 = Not available. 0x01 = Enabled. 0x02 = Disabled")
        .def_property_readonly("module_version", &get_module_version, "MSB = version , LSB = subversion (i.e. 0x020A = version 2.10)");
    device_info.doc() = "The stimulator has several different micro controllers that it uses. These are on the motherboard and current modules. As a result, it is very helpful for "
        "troubleshooting and debugging to see what versions of the firmware are stored on the motherboard and current modules as well as what the status of how many current modules "
        "are installed and what communication protocol is being used.";


    py::class_<BStimulusConfiguration> stimulus_configuration(m, "StimulusConfiguration");
    stimulus_configuration.def(py::init<>(), "Components of the Stimulus Configurations.")
        .def_readwrite("anodicFirst", &BStimulusConfiguration::anodicFirst, "0x01 = anodic first, 0x00 = cathodic first")
        .def_readwrite("pulses", &BStimulusConfiguration::pulses, "Number of biphasic pulses (from 1 to 255)")
        .def_readwrite("amp1", &BStimulusConfiguration::amp1, "Amplitude first phase (uA)")
        .def_readwrite("amp2", &BStimulusConfiguration::amp2, "Amplitude second phase (uA)")
        .def_readwrite("width1", &BStimulusConfiguration::width1, "Width first phase (us)")
        .def_readwrite("width2", &BStimulusConfiguration::width2, "Width second phase (us)")
        .def_readwrite("frequency", &BStimulusConfiguration::frequency, "Frequency of stimulation pulses (Hz)")
        .def_readwrite("interphase", &BStimulusConfiguration::interphase, "Time between phases (us)");
    stimulus_configuration.doc() = "The stimulator is capable of custom configuring a biphasic stimulus. The amplitudes and widths and frequency are all a part of the components "
        "that can be configured. The main restriction is that the two phases are balanced, i.e. width * amp of phase 1 is equal to width * amp of phase 2.";

    py::class_<BSequenceStatus> sequence_status(m, "SequenceStatus");
    sequence_status.def(py::init<>(), "Status of the Stimulator.")
        .def_readwrite("status", &BSequenceStatus::status, "Contains status of the stimulator.");
    sequence_status.doc() = "The stimulator can always be queried to determine what state it is in.";

    py::class_<BMaximumValues> maximum_values(m, "MaximumValues");
    maximum_values.def(py::init<>(), "Admin Max Values.")
        .def_readwrite("voltage", &BMaximumValues::voltage, "Max voltage value.")
        .def_readwrite("amplitude", &BMaximumValues::amplitude, "Amplitude (uA)")
        .def_readwrite("phase_charge", &BMaximumValues::phaseCharge, "Charge per phase (pC)")
        .def_readwrite("frequency", &BMaximumValues::frequency, "Frequency (Hz)");
    maximum_values.doc() = "The stimulator has an administrative interface that allows the primary researcher to set additional safety levels depending on there stimulation protocols and parameters.";

    py::class_<BTestElectrodes> test_electrodes(m, "TestElectrodes");
    test_electrodes.def(py::init<>(), "Electrode Diagnostics.")
        .def_property_readonly("electrodes", &get_test_electrodes_meas, "5 voltage measurements for all 96 channels reported in millivolts")
        .def_property_readonly("impedance", &get_test_electrodes_imp, "Real part of Impedance of each electrode reported in Ohms.");
    test_electrodes.doc() = "The stimulator allows for diagnosising the status of the electrodes attached to it. A known stimulus is sent to each electrode and the voltage "
        "is recorded for the five data points during a stimulation, i.e. before the first phase, during the first phase, between the two phases, during the second phase and "
        "after the second phase. These voltage levels are then used along with the known stimulation to calculate the impedance of each electrode. A 1 kHz frequency is used for the stimulation.";

    py::class_<BTestModules> test_modules(m, "TestModules");
    test_modules.def(py::init<>(), "Module Diagnostics.")
        .def_property_readonly("modules_mv", &get_modules_mv, "5 voltage measurements for all current modules reported in millivolts")
        .def_property_readonly("modules_status", &get_test_modules_status, "Status of each current module.");
    test_modules.doc() = "The stimulator uses current modules to deliver stimulus through electrodes. These modules may become damaged and so the stimulator uses a known load "
        "and stimulus parameter to determine if the voltage levels on the current module are as they should be.";

    py::class_<BGroupStimulus> group_stimulus(m, "GroupStimulus");
    group_stimulus.def(py::init<>(), "Group Stimulus.")
        .def_property("electrode", &get_group_electrodes, &set_group_electrodes, "electrodes to stimulate") // TODO need to wrap this to make it writeable
        .def_property("pattern", &get_group_pattern, &set_group_pattern, "Configuration Pattern to use with coresponding channel.");
    group_stimulus.doc() = "The stimulator allows for a group of simultaneous stimulations to occur. Two methods exist for doing this, first is creating a program script and "
        "issueing several different calls. The second method saves on the USB overhead by allowing a single call to set up the simultaneous stimulations.";

    py::class_<BReadEEpromOutput> read_eeprom_output(m, "ReadEEPROMOutput");
    read_eeprom_output.def(py::init<>(), "CereStim 96 Motherboard EEprom.")
        .def_property_readonly("eeprom", &get_eeprom, "eeprom values");
    read_eeprom_output.doc() = "The EEprom on the microcontroller stores the information that should be preserved over time even when the device is off or unplugged. These "
        "values can be read in order to debug or know the status of different components within the device.";


    py::class_<BReadHardwareValuesOutput> read_hardware_values_output(m, "ReadHardwareValuesOutput");
    read_hardware_values_output.def(py::init<>(), "Hardware Values of the CereStim 96.")
        .def_readwrite("amp", &BReadHardwareValuesOutput::amp, "Max phase amplitude based on hardware in uA.")
        .def_readwrite("max_comp_voltage", &BReadHardwareValuesOutput::maxCompVoltage, "Max output compliance voltage.")
        .def_readwrite("min_comp_voltage", &BReadHardwareValuesOutput::minCompVoltage, "Min output compliance voltage.")
        .def_readwrite("charge", &BReadHardwareValuesOutput::charge, "Max charge based on hardware in pC.")
        .def_readwrite("max_freq", &BReadHardwareValuesOutput::maxFreq, "Max Frequency based on hardware in Hz.")
        .def_readwrite("min_freq", &BReadHardwareValuesOutput::minFreq, "Min Frequency based on hardware in Hz.")
        .def_readwrite("width", &BReadHardwareValuesOutput::width, "Max Width for each phase based on hardware in uS.")
        .def_readwrite("interphase", &BReadHardwareValuesOutput::interphase, "Max Interphase width based on hardware in uS.")
        .def_readwrite("modules", &BReadHardwareValuesOutput::modules, "Number of modules installed in device.");
    read_hardware_values_output.doc() = "The stimulators various models have some different hardware configurations, so it is beneficial to get those hardware values of that particuliar CereStim 96.";

    py::class_<BElectrodeChannelMap> electrode_channel_map(m, "ElectrodeChannelMap");
    electrode_channel_map.def(py::init<>(), "Map Channels to Electrodes.")
        .def_property("bankA", &get_bankA, &set_bankA, "UINT8 Array, the pin on bank A is the index, and the value is the acutal electrode number.")
        .def_property("bankB", &get_bankB, &set_bankB, "UINT8 Array, the pin on bank B is the index, and the value is the acutal electrode number.")
        .def_property("bankC", &get_bankC, &set_bankC, "UINT8 Array, the pin on bank C is the index, and the value is the acutal electrode number.");
    electrode_channel_map.doc() = "The stimulator is capable of sending stimulation up to 96 different electrodes. The layout of where those electrodes are mapped to sometimes are "
        "not a straight channel 1 to electrode 1, such as in a Blackrock .CMP file. This struct allows the user to specify a mapping for there electrodes so that they do not need to "
        "worry about what channel they need to stimulate if they want electrode 20 to be stimulated.";

    py::class_<BStimulator> stimulator(m, "Stimulator");
    stimulator.doc() = "The stimulator class encapsulates all the functionallity of the stimulator and allows the user the ability to interface directly with Blackrock Microsystems CereStim 96 device. "
        "By encapsulating it in an object, multiple stimulators can be connected to a single Host PC and be used simultaneously.";

    stimulator.def(py::init<>(), "Creates a stimulator object that is able to bind to an actual CereStim 96 that is connected to the host PC.")
        .def_static("scan_for_devices", &scan_for_devices_wrap, 
            "Scans all USB devices and builds up a list of serial numbers of the devices connected to the computer. In order to connect to a device, "
            "this function has to be invoked first, then a device needs to be selected through setDevice() and only then connect()")
        //.def_static("scan_for_devices", &BStimulator::scanForDevices)
        .def("set_device", &BStimulator::setDevice, "device_index"_a, 
            "Using the index of the device in the serial number list obtained from scanForDevices(), set the device you want to connect.")
        .def("connect", &BStimulator::connect, "stim_interface"_a, "params"_a, 
            "Tries to establish a connection with a CereStim 96 device that has been selected using setDevice().\n\n"
            "stim_interface: The type of interface that the object should try and connect over\n"
            "params: A void pointer to either an initialized BUsbParams structure or initialized BRs232Params structure")
        .def("disconnect", &BStimulator::disconnect, "Disconnects from a connected CereStim 96 device.")
        .def("lib_version", &BStimulator::libVersion, "output"_a, "Takes a pointer to a BVersion structure and writes the libarary version to the structure.")

        .def("manual_stimulus", &BStimulator::manualStimulus, "electrode"_a, "configID"_a, 
            "Allows the user to send a single stimulus pulse of one of the stimulation waveforms to a specified electrode.\n\n"
            "electrode: The electrode that should be stimulated Valid values are from 1 - 96\n"
            "configID: The stimulation waveform to use Valid values are from 1 - 15")
        .def("measure_output_voltage", &BStimulator::measureOutputVoltage, "output"_a, "module"_a, "electrode"_a,
            "Sends a known stimulation configuration, 45 uA for micro and 9 mA for Macro, from a selected current module to a specific module. "
            "It is helpful for determining the impedance of the electrode.\n\n"
            "output: A pointer to a BOutpuMeasurment structure to store the returned measurement values\n"
            "module: The specific current module (0 - 15) that should send the stimulus The module must be enabled.\n"
            "electrode: The electrode to send the stimulation to Valid values are from 1 - 96")
        .def("beginning_of_sequence", &BStimulator::beginningOfSequence,
            "This is the first command that must be called when creating a stimulation script. After calling this you are able to call wait, "
            "autoStimulus, beginningOfGroup, and endOfGroup commands. The stimulation script can have up to 128 commands, excluding beginningOfSequence and endOfSequence")
        .def("end_of_sequence", &BStimulator::endOfSequence, 
            "This is the last command that must be called when creating a stimulation script. It does not count towards the maximum of 128 commands.")
        .def("beginning_of_group", &BStimulator::beginningOfGroup,
        "This command signifies that the following commands up to the endOfGroup command should all occur simultaneously. The only commands that are valid are the "
        "autoStimulus commands. You can only have as many stimulations as the number of current modules installed. Cant be called on the last of the 128 instructions "
        "since it needs to have a closing endOfGroup command.")
        .def("end_of_group", &BStimulator::endOfGroup, 
            "This command closes off a group of simultaneous stimulations. If beginningOfGroup is called during a sequence of commands, then there must be an endOfGroup "
            "otherwise the user will get a sequence error as a return value.")
        .def("auto_stimulus", &BStimulator::autoStimulus, "electrode"_a, "configID"_a,
            "This command tells the stimulator when to send a stimulus to an electrode in a stimulation script. It can be used as many times as needed so long as the total number "
            "of commands does not exceed 128. It should also be used within beginningOfGroup and endOfGroup commands to allow for simultaneous stimulations.\n\n"
            "electrode: The electrode that will be stimulated Valid values are from 1 - 96\n"
            "configID: One of the fifteen stimulation waveforms that should be used")
        .def("wait", &BStimulator::wait, "milliseconds"_a, 
            "This command can only be used within a stimulation script and is capable of adding a wait of up to 65,535 milliseconds.\n\n"
            "milliseconds: The number of milliseconds to wait before executing the next command")
        .def("play", &BStimulator::play, "times"_a, 
            "Tells the stimulator the number of times that it should run the stimulation script. A zero passed in will tell it to run indefinately until it is either stopped or "
            "paused by the user. Other values include between 1 and 65,535 repetitions. Can not be called during a beginningOfSequence and endOfSequence command call.\n\n"
            "times: Number of times to execute the stimulation script 0 means indefinately")
        .def("stop", &BStimulator::stop, 
            "This will stop a currently running stimulation script and reset it so when played again it will begin from the first command. Can only be called while the stimulator "
            "has a status of stimulating or paused.")
        .def("pause", &BStimulator::pause,
            "This will pause a currently running stimulation script and keep track of the next command that needs to be executed so if it receives a play command it can pick up where it left off.")
        .def("max_output_voltage", &BStimulator::maxOutputVoltage, "output"_a, "rw"_a, "voltage"_a, 
            "This will set the values of +VDD and -VSS on the stimulator which allows it to effectively limit the maximum output voltage that can be delivered during a stimulation. If the output "
            "current times the impedance of the electrode is greater than the max compliance voltage then it means the full current is not being deliverd to the electrode because it can not drive "
            "any more current.\n\n"
            "output: Pointer to a BMaxOutputVoltage structure that will contain the read value\n"
            "rw: Boolean expression for determining if you just want to read the output compliance voltage or update it with a new value Read = 0 and Write = 1\n"
            "voltage: The voltage level that is being set if writing, otherwise it is ignored")
        .def("read_device_info", &BStimulator::readDeviceInfo, "output"_a,
            "This returns all the information about the CereStim 96 that is connected to. It will tell its part number, serial number, firmware versions for both the motherboard and for the "
            "current modules. It will also tell you the protocol that the motherboard is using with the current modules and the number of installed current modules.\n\n"
            "output: Pointer to a BDeviceInfo structure, the structure will be populated with the CereStim's information")
        .def("enable_module", &BStimulator::enableModule, "module"_a, 
            "Allows the user to enable different current modules that have been disabled. This is useful for testing and making sure that multiple current modules are all giving the same output values.\n\n"
            "module: The current module to be enabled from 0 to 15")
        .def("disable_module", &BStimulator::disableModule, "module"_a,
            "Allows the user to disable different current modules that are installed in the CereStim. This is useful for testing and making sure that multiple current modules are all giving the same "
            "output values. The current module has to exist to be disabled.\n\n"
            "module: The current module to be disabled from 0 to 15")
        .def("configure_stimulus_pattern", &BStimulator::configureStimulusPattern, "configID"_a, "afcf"_a, "pulses"_a, "amp1"_a, "amp2"_a, "width1"_a, "width2"_a, "frequency"_a, "interphase"_a, 
            "Takes all of the parameters needed in order to create a custom biphasic stimulation waveform. The device is capable of handling 16 differnt waveforms, but waveform 0 is reserved and "
            "used for testing in getting measurements from electrodes and current modules. Micro and Macro stimulators have different ranges of valid values. Especially for the amplitude where "
            "micro stimulators are in the uA range with uA precision, Macro stimulators go from 100 uA to 10 mA with 100 uA precision. While the widths and interphases have quite a range, the "
            "user needs to somewhat understand how they interact with the frequency chosen. You dont want a stimulus waveform that is longer than the time between repeats.\n\n"
            "configID: The stimulation waveform that is being configured 1 - 15\n"
            "afcf: What polarity should the first phase be, Anodic or Cathodic first\n"
            "pulses: The number of stimulation pulses in waveform from 1 - 255\n"
            "amp1: The amplitude of the first phase, for Micro it is 1 - 215 uA, and for Macro it is 100 uA - 10 mA\n"
            "amp2: The amplitude of the first phase, for Micro it is 1 - 215 uA, and for Macro it is 100 uA - 10 mA\n"
            "width1: The width of the first phase in the stimulation 1 - 65,535 uS\n"
            "width2: The width of the second phase in the stimulation 1 - 65,535 uS\n"
            "frequency1: The stimulating frequency at which the biphasic pulses should repeat 4 - 5000 Hz\n"
            "interphase: The period of time between the first and second phases 53 - 65,535 uS")
        .def("read_stimulus_pattern", &BStimulator::readStimulusPattern, "output"_a, "configID"_a, 
            "Reads back all of the parameters associated with a specific stimulation waveform and stores it in the structure supplied by the user\n\n"
            "output: Pointer to a BStimulusConfiguration structure which contains all the parameters that consist in a stimulation waveform\n"
            "configID: The stimulation waveform that is being read back")
        .def("read_sequence_status", &BStimulator::readSequenceStatus, "output"_a,
            "Can be called anytime as it does not interrupt other functions from executing, but simply reads what state the stimulator is in.\n\n"
            "output: Pointer to a BSequenceStatus that gets populate with the value from the CereStim 96")
        .def("stimulus_max_values", &BStimulator::stimulusMaxValues, "output"_a, "rw"_a, "voltage"_a, "amplitude"_a, "phase_charge"_a, "frequency"_a, 
            "Intended to be an administrative interface that can be password protected and only allow the lead researcher to make changes. It allows the user to set other determined upper "
            "limits for the stimulation parameters for whatever safety protocol they are requireing. Again micro and macro stimulators will have some different bounds for setting max values "
            "due to the different ranges each are able to achieve.\n\n"
            "output: Pointer to a BMaximumValues structure that will contain the current max values that are set\n"
            "rw: Boolean to determine if updating new max values or just reading the old Read = 0 and Write = 1\n"
            "voltage: The Max Compliance Voltage that can be set\n"
            "amplitude: The Max amplitude that can be used in a stimulation\n"
            "phase_charge: The Max charge per phase that will be allowed (Charge = Amplitude * Width)\n"
            "frequency: The Max frequency at which the stimulations can take place\n")
        .def("group_stimulus", &BStimulator::groupStimulus, "begin_seq"_a, "play"_a, "times"_a, "number"_a, "input"_a, 
            "There is a lot of overhead in sending commands over the USB to the CereStim 96. each function call averages 2mS. This function allows the user to create the stimulation parameters "
            "beforehand and in a single function call perform simultaneous stimulations based on different electrodes and configured waveforms.\n\n"
            "begin_seq: Boolean expression to tell the function that it is the beginning of a sequence\n"
            "play: Boolean expression to tell if the stimulator should begin stimulating immedieatly after this call\n"
            "times: The number of times to play the stimulation, is ignored if play = false\n"
            "number: The number of stimulus that will occur simultaneously.\n"
            "input: Pointer to an instantiated BGroupStimulus structure which has a pair of arrays with electrodes and waveforms")
        .def("trigger_stimulus", &BStimulator::triggerStimulus, "edge"_a, 
            "Allows the stimulator to wait for a trigger event before executing a stimulation script. The stimulator has an external TTL Trigger input port that uses TTL logic levels to determine "
            "wheather the input is high or low. The stimulator can be set to fire on a rising edge, falling edge, or any edge transition. Once in trigger mode the stimulator is locked down from "
            "other function calls except for stopTriggerStimulus\n\n"
            "edge: The type of digital event to trigger the stimulation on")
        .def("stop_trigger_stimulus", &BStimulator::stopTriggerStimulus, "Changes the state of the stimulator so that it is no longer waiting for a trigger. Frees up the stimulator for other commands to be called.")
        .def("update_electrode_channel_map", &BStimulator::updateElectrodeChannelMap, "input"_a,
            "Since not all electrodes are found on channel 1 this function allows the user to create a map key pair where the channel is an index into an array which holds the value of the electrode at that channel.")
        .def("test_electrodes", &BStimulator::testElectrodes, "output"_a,
            "This is a diagnostic tool that can be used to help determine which electrodes are good and which ones are bad. The stimulator will send out a known stimulus configuration, "
            "(Config_0), and measure the voltage it returns. Off of these values the relative impedance calculated and returned.\n\n"
            "output: Pointer to a BTestElectrodes Structure which will contain all the information from all the channels.")
        .def("test_modules", &BStimulator::testModules, "output"_a,
            "Used as a way to diagnose the current modules that reside in the stimulator to determine if there output voltage levels are okay and ensure that they continue to function at the "
            "right levels over time. A known stimulus is applied to a known load and the voltage is compared to what it should be.\n\n"
            "output: Pointer to a BTestModules structure which will contain the status of all the current modules")
        .def("read_hardware_values", &BStimulator::ReadHardwareValues, "output"_a,
            "Reads the hardware values that are set based on the part number\n\n"
            "output: Structure containing the hardware values")
        .def("read_eeprom", &BStimulator::ReadEeprom, "output"_a,
            "Reads the CereStim 96 motherboards EEprom and returns all values\n\n"
            "output: Pointer to array of UINT8[256]")
        .def("erase_eeprom", &BStimulator::EraseEeprom, "Erases the complete EEProm on the the CereStim 96 motherboard, setting all values to 0xFF")
        .def("write_eeprom", &BStimulator::WriteEEProm, "addr"_a, "val"_a)
        .def("disable_stimulus_configuration", &BStimulator::DisableStimulusConfiguration, "config_id"_a,
            "Disables a stimulation waveform so that it is able to be reset\n\n"
            "config_id: The configuration to disable")
        .def("reset_stimulator", &BStimulator::ResetStimulator, "Administrative command that will call the reset interrupt vector on the uController User will need to call Connect after calling this.")

        .def("is_connected", &BStimulator::isConnected, "Lets the user know that the stimulator object is connected to a physical CereStim 96 device.\n\n"
            "Returns: a boolean result, 1 = TRUE, 0 = FALSE")
        .def("get_interface", &BStimulator::getInterface, "Checks to see what interface is being used for the connection between the stimulator object and the physical CereStim 96 Device.\n\n"
            "Returns: The interface being used for the stimulator object")
        .def("get_serial_number", &BStimulator::getSerialNumber, "Retrieves the serial number that is programmed into the CereStim 96 device that is attached. The format of the 32 bit serial number is "
            "as follows 0xPPXXSSSS, where PP is the part number, XX is ignored, and SSSS is the serial number. The part number is a BPartNumbers enumeration.\n\n"
            "Returns: Part Number and Serial number of the CereStim 96")
        .def("get_motherboard_firmware_version", &BStimulator::getMotherboardFirmwareVersion, "Retrieves the firmware revision of the microcontroller on the motherboard. The MSB is the Major revision "
            "number and the LSB is the minor revision number. I.e. 0x0500 would be version 5.0\n\n"
            "Returns: Firmware Version of the Motherboard")
        .def("get_protocol_version", &BStimulator::getProtocolVersion, "The protocol version that the motherboard uses to send and receive data from the current modules. The MSB is the Major revision "
            "number and the LSB is the minor revision number. I.e. 0x0105 would be version 1.5\n\n"
            "Returns: Protocol Version of the Motherboard")
        .def("get_min_max_amplitude", &BStimulator::getMinMaxAmplitude, "Since there are different models and version of the stimulator, such as the micro and macro versions, this will allow the user "
            "to get the min and max amplitudes that are allowed for stimulation. The upper two MSB are the maximum amplitude while the lower two LSB are the minimum amplitude.\n\n"
            "Returns: Min and Max Amplitude.")
        .def("get_module_firmware_version", &get_module_firmware_version_wrap,
            "Each current module has its own microcontroller and has a firmware version. All current modules in a single stimulator should have the same firmware version. The MSB is the Major revision "
            "number and the LSB is the minor revision number. I.e. 0x0105 would be version 1.5")
        .def("get_module_status", &get_module_status_wrap,
            "This tells the status of each current module, whether it is enabled, disabled, or not available.")        .def("get_usb_address", &BStimulator::getUSBAddress)
        .def("get_max_hard_charge", &BStimulator::getMaxHardCharge, "This value is based on the hardware of the particuliar model of the CereStim 96. Again the micro and macro versions of the stimulator have different values")
        .def("get_min_hard_frequency", &BStimulator::getMinHardFrequency, "This value is based on the hardware of the particuliar model of the CereStim 96. Again the micro and macro versions of the stimulator have different values\n\n"
            "Returns: Minimum Stimulating Frequency in Hz")
        .def("get_max_hard_frequency", &BStimulator::getMaxHardFrequency, "This value is based on the hardware of the particuliar model of the CereStim 96. Again the micro and macro versions of the stimulator have different values\n\n"
            "Returns: Maximum Stimulating Frequency in Hz")
        .def("get_number_modules", &BStimulator::getNumberModules, "This value is based on the hardware of the particuliar model of the CereStim 96. Again the micro and macro versions of the stimulator have different values\n\n"
            "Returns: Number of Modules installed")
        .def("get_max_hard_width", &BStimulator::getMaxHardWidth, "This value is based on the hardware of the particuliar model of the CereStim 96.\n\n"
            "Returns: Maximum width of each phase in uS")
        .def("get_max_hard_interphase", &BStimulator::getMaxHardInterphase, "This value is based on the hardware of the particuliar model of the CereStim 96\n\n"
            "Maximum interphase width in uS")
        .def("is_safety_disabled", &BStimulator::isSafetyDisabled, "For Internal validation and testing it is required to disable the safety limits in the firmware and API so that hardware "
            "limits can be observed and tested.\n\n"
            "Returns: true if disabled false otherwise")
        .def("is_device_locked", &BStimulator::isDeviceLocked, "If the detected number of current modules doesn't match the hardware configuration or if the hardware configuration is not"
            " setup, the device will be locked down preventing any stimulation from occuring.\n\n"
            "Returns: true if locked false otherwise");

    py::class_<BStimulator::maxStimulatorError>(stimulator, "MaxStimulatorError")
        .def(py::init<>(), "Error If there are more stimulator objects created than allowed which is MAX_STIMULATORS");

}