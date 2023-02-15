# Author: Jeff Weiss <jeff.weiss@pitt.edu>
# May 2022

"""br_stimpy: a python package to interface with Blackrock Neurotech Cerestim API.

Example:

```
from br_stimpy import stimpy

stim_obj = Stimulator()
print(stim_obj.api_version)
stim_obj.connect()
stim_obj.simple_stimulus(
    electrode=1,
    afcf=stim_obj.WFTypes.wf_cathodic_first,
    pulses=1,
    amp1=10,
    amp2=10,
    width1=200,
    width2=200,
    frequency=100,
    interphase=100,
)
stim_obj.disconnect()
```
"""

__all__ = ["stimpy", "constants", "enums", "group_stim_struct"]
__private__ = ["_bstimulator", "_validation", "__version__"]

from .__version__ import (
    __author__,
    __author_email__,
    __copyright__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
)
