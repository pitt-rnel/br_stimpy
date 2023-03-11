from br_stimpy.stimpy import Stimulator

stim_obj = Stimulator()
print(stim_obj.api_version)
stim_obj.connect()
stim_obj.simple_stimulus(
    electrode=1,
    afcf=stim_obj.WFType.wf_cathodic_first,
    pulses=1,
    amp1=10,
    amp2=10,
    width1=200,
    width2=200,
    frequency=100,
    interphase=100,
)
stim_obj.disconnect()
