"""Constants for use with br_stimpy"""
# Author: Jeff Weiss <jeff.weiss@pitt.edu>
# February 2023

from __future__ import annotations  # ensure forward compatibility
from br_stimpy import _bstimulator

#: Maximum channel count = 96
MAX_CHANNELS: int = (
    _bstimulator.MAX_CHANNELS - 1
)  # the API constant also includes internal channel 0

#: Maximum pattern configuration count = 16, only 15 configurations are available to the user
MAX_CONFIGURATIONS: int = _bstimulator.MAX_CONFIGURATIONS

#: Maximum cerestim modules count = 16
MAX_MODULES: int = _bstimulator.MAX_MODULES

#: Channels per bank = 32
BANK_SIZE: int = _bstimulator.BANK_SIZE

#: Maximum number of stimulators supported by API = 12
MAX_STIMULATORS: int = (
    12  # subject to change, this is not from public BStimulator.h header
)
