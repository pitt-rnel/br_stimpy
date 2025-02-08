"""br_stimpy: a python package to interface with Blackrock Neurotech Cerestim API.

Example::

    from br_stimpy import stimpy
    
    stim_obj = stimpy.Stimulator()
    print(stim_obj.api_version)
    stim_obj.connect()
    stim_obj.simple_stimulus(
        electrode=1,
        afcf=stimpy.WFType.wf_cathodic_first,
        pulses=1,
        amp1=10,
        amp2=10,
        width1=200,
        width2=200,
        frequency=100,
        interphase=100,
    )
    stim_obj.disconnect()

"""
# Author: Jeff Weiss <jeff.weiss@pitt.edu>
# May 2022

__all__ = ["stimpy", "constants", "enums", "group_stim_struct"]
__private__ = ["_bstimulator", "_validation", "__version__"]

import br_stimpy.stimpy as stimpy
import br_stimpy.constants as constants
import br_stimpy.enums as enums
import br_stimpy.group_stim_struct as group_stim_struct
import br_stimpy._bstimulator as _bstimulator
import br_stimpy._validation as _validation

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
