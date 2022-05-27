from stimpy import stimulator
import time

# create cerestim API object
cerestim = stimulator.stimulator()

# check API versoin
lib_version = cerestim.lib_version()
if lib_version.beta:
    beta = ' beta'
else:
    beta = ''
print(f"API version: {lib_version.major}.{lib_version}.minor{beta}")

# scan for devices
device_serial_nums = cerestim.scan_for_devices()
for (i, d) in enumerate(device_serial_nums):
    print(f"device {i+1}: {d}")

# Open the USB connection
# note that 0 is default and will automatically call scan_for_devices
# if only one stimulator is attached, these two calls can be combined
# with simple call to "cerestim.connect()"
dev_idx = 0
cerestim.connect(device_index = dev_idx)
# note that 0 is default and will automatically call scan_for_devices

# Check the connection
connect_result = cerestim.is_connected()
USB_address = cerestim.get_usb_address()
if connect_result:
    print(f"Stimulator connected on USB address {USB_address}")
else:
    print(f"Stimulator not connected....this should never happen...")
    raise RuntimeError

device_info = cerestim.read_device_info()
breakpoint()
sn = device_info['serial_no']
mv = device_info['mainboard_version']
pv = device_info['protocol_version']

print(f"Device Serial #:          {sn['part'].name}-{sn['serial_no']}")
print(f"Device Mainboard Version: {mv['major']}.{mv['minor']}")
print(f"Device Protocol Version:  {pv['major']}.{pv['minor']}")

print("Device Module Status:")
for (i, ms) in enumerate(device_info['module_status']):
    if ms == True:
        mv = device_info['module_version'][i]
        print(f"Module {i + 1}: {ms.name} - Version {mv['major']}.{mv['minor']}")
    else:
        print(f"Module {i + 1}: {ms.name}")
print(f"{cerestim.get_number_modules()} modules installed.")

max_hard_charge = cerestim.get_max_hard_charge();
min_hard_frequency = cerestim.get_min_hard_frequency();
max_hard_frequency = cerestim.get_max_hard_frequency();
max_hard_width = cerestim.get_max_hard_width();

print(f"Maximum Hardware Charge: {max_hard_charge}")
print(f"Minimum Hardware Frequency: {min_hard_frequency}")
print(f"Maximum Hardware Frequency: {max_hard_frequency}")
print(f"Maximum Hardware Width: {max_hard_width}")

# TODO set max values

# Read the maximum settings to make sure that everything is OK
max_values = cerestim.read_stimulus_max_values()
print("Read Maximum Values:  ")
print(f"Maximum Voltage:      {stimulator.get_enum_docstr(stimulator.oc_volt(max_values.voltage))}")
print(f"Maximum Amplitude:    {max_values.amplitude}")
print(f"Maximum Phase Charge: {max_values.phase_charge}")
print(f"Maximum Frequency:    {max_values.frequency}")

# Set up additional configurations to a default value
cath = stimulator.wf_types.wf_cathodic_first
for i in range(1,16):
    cerestim.configure_stimulus_pattern(configID=i,afcf=cath, pulses=1, amp1=0, amp2=0, width1=200, width2=200, frequency=100, interphase=100)
print("Default Configs Done")

# Ensure that the max values are set high enough so you don't get errors when configuring patterns
for i in range(1,3):
    cerestim.configure_stimulus_pattern(configID=i,afcf=cath, pulses=1, amp1=10*i, amp2=10*i, width1=200, width2=200, frequency=100, interphase=100)
print("Example Configs Done")

# first stim method is single configuration
print("manual stimulus 1")
cerestim.manual_stimulus(electrode=1, configID=1)
time.sleep(0.2)

print("manual stimulus 2")
cerestim.manual_stimulus(electrode=2, configID=2)
time.sleep(0.2)

# There is a way to write a program that contains a group fo stimulus commands in one call
# This does a group of two simultaneous stimulations with one configuration
group_stim_input = stimulator.group_stimulus_struct(electrode=[1, 45], pattern=[1, 1])
# groupStimulus(beginSeq, play, times, number, group_stimlus_struct);
# beginSeq should be True if this is first part of a new program
# play should be True if you want to stimulate immedietaly after.
# times is the number of times to play the stimulation
# number is the number of electrodes to simulatneously stimulate
# group_stimlus_struct is the structure containing the electrodes and patterns to use
print("group stimulus:")
cerestim.group_stimulus(begin_seq=True, play=True, times=1, number=2, group_stim_struct=group_stim_input)
print("done")
time.sleep(0.2)

# Another method for stimulating is a program.  With the program you have to call beg of sequence followed
# by a number of autoStimulus and wait commands and then close it with end of sequence.  Then you will call play with
# the number of times to play the program.
print("Programming sequence")
cerestim.begin_sequence()
for i in range(1,10):
    cerestim.auto_stimulus(electrode=i, configID=i)
cerestim.end_sequence()
cerestim.play(times=5)
print("playing")
status = stimulator.seq_type.playing
while status == stimulator.seq_type.playing:
    status = cerestim.read_sequence_status()
    print('.',end=None, flush=True)
    time.sleep(0.05)
time.sleep(0.1)


print('disconnect ')
cerestim.disconnect()
print('done')
