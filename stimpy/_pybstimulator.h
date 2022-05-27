#ifndef _PYBSTIMULATOR_H_INCLUDED
#define _PYBSTIMULATOR_H_INCLUDED

#include "../extern/pybind11/include/pybind11/pybind11.h"
#include "../extern/pybind11/include/pybind11/stl.h"
#include "../extern/pybind11/include/pybind11/stl_bind.h"
#include "../extern/CereStim-API/Binaries/BStimulator.h"
#include <vector>
#include <array>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>

template <class T, size_t ROW, size_t COL>
using Matrix = std::array<std::array<T, COL>, ROW>;

std::vector<UINT32> scan_for_devices_wrap();
std::array<UINT16, MAXMODULES> get_module_firmware_version_wrap(BStimulator *stimulator);
std::array<UINT8, MAXMODULES> get_module_status_wrap(BStimulator *stimulator);
std::array<INT16, NUMBER_VOLT_MEAS> get_output_measurement(BOutputMeasurement *output_measurement);
std::array<UINT8, MAXMODULES> get_module_status(BDeviceInfo *device_info);
std::array<UINT16, MAXMODULES> get_module_version(BDeviceInfo *device_info);
Matrix<INT16, MAXCHANNELS, NUMBER_VOLT_MEAS> get_test_electrodes_meas(BTestElectrodes *test_electrodes);
std::array<UINT32, MAXCHANNELS> get_test_electrodes_imp(BTestElectrodes *test_electrodes);
Matrix<INT16, MAXMODULES, NUMBER_VOLT_MEAS> get_modules_mv(BTestModules *testModules);
std::array<UINT32, MAXCHANNELS> get_test_electrodes_imp(BTestElectrodes *test_electrodes);
Matrix<INT16, MAXMODULES, NUMBER_VOLT_MEAS> get_modules_mv(BTestModules *testModules);
std::array<BModuleStatus, MAXMODULES> get_test_modules_status(BTestModules *testModules);
std::array<UINT8, MAXMODULES> get_group_electrodes(BGroupStimulus *group);
void set_group_electrodes(BGroupStimulus *group, std::array<UINT8, MAXMODULES> electrode);
std::array<UINT8, MAXMODULES> get_group_pattern(BGroupStimulus *group);
void set_group_pattern(BGroupStimulus *group, std::array<UINT8, MAXMODULES> pattern);
std::array<UINT8, EEPROM_SIZE> get_eeprom(BReadEEpromOutput* eeprom_output);
std::array<UINT8, BANKSIZE> get_bankA(BElectrodeChannelMap *map);
std::array<UINT8, BANKSIZE> get_bankB(BElectrodeChannelMap *map);
std::array<UINT8, BANKSIZE> get_bankC(BElectrodeChannelMap *map);
void set_bankA(BElectrodeChannelMap *map, std::array<UINT8, BANKSIZE> bank);
void set_bankB(BElectrodeChannelMap *map, std::array<UINT8, BANKSIZE> bank);
void set_bankC(BElectrodeChannelMap *map, std::array<UINT8, BANKSIZE> bank);



#endif _PYBSTIMULATOR_H_INCLUDED