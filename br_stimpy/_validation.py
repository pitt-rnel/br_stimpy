"""Internal validation functions"""
# Author: Jeff Weiss <jeff.weiss@pitt.edu>
# February 2023

from __future__ import annotations  # ensure forward compatibility
from br_stimpy.constants import *


class _ValidationFcns:
    """Validation functions for internal use within this module"""

    @staticmethod
    def validate_electrode(electrode: int) -> None:
        if electrode < 1 or electrode > MAX_CHANNELS:
            raise ValueError("Invalid electrode")

    @staticmethod
    def validate_configID(configID: int) -> None:
        if configID < 1 or configID > MAX_CONFIGURATIONS:
            raise ValueError("Invalid pattern config ID")

    @staticmethod
    def validate_module(module: int) -> None:
        if module < 0 or module > MAX_MODULES:
            raise ValueError("Invalid module index")

    @staticmethod
    def validate_pulses(pulses: int) -> None:
        if pulses < 1 or pulses > 255:
            raise ValueError("Invalid pulse number")

    @staticmethod
    def validate_amp(amp: int) -> None:
        # TODO determine if micro or macro, for now assume micro
        if amp < 0 or amp > 215:  # micro
            # if amp < 100 or amp > 10000:
            raise ValueError("Invalid pulse amplitude")

    @staticmethod
    def validate_width(width: int) -> None:
        if width < 1 or width > 65535:
            raise ValueError("Invalid pulse width")

    @staticmethod
    def validate_frequency(freq: int) -> None:
        if freq < 4 or freq > 5000:
            raise ValueError("Invalid frequency")

    @staticmethod
    def validate_interphase(interphase: int) -> None:
        if interphase < 53 or interphase > 65535:
            raise ValueError("Invalid interphase")
