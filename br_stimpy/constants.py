# br_stimpy.constants
# Author: Jeff Weiss <jeff.weiss@pitt.edu>
# February 2023

from __future__ import annotations  # ensure forward compatibility
from br_stimpy import _bstimulator

MAX_CHANNELS: int = (
    _bstimulator.MAX_CHANNELS - 1
)  # the API constant also includes internal channel 0
MAX_CONFIGURATIONS: int = _bstimulator.MAX_CONFIGURATIONS
MAX_MODULES: int = _bstimulator.MAX_MODULES
BANK_SIZE: int = _bstimulator.BANK_SIZE
MAX_STIMULATORS: int = (
    12  # subject to change, this is not from public BStimulator.h header
)
