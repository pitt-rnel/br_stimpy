from br_stimpy import stimulator

stim_obj = stimulator.stimulator()
print(stim_obj.lib_version())
stim_obj.connect()
stim_obj.configure_stimulus_pattern(
    configID=1,
    afcf=stimulator.wf_types.wf_cathodic_first,
    pulses=1,
    amp1=10,
    amp2=10,
    width1=200,
    width2=200,
    frequency=100,
    interphase=100
)
stim_obj.manual_stimulus(electrode=1, configID=1)
stim_obj.disconnect()