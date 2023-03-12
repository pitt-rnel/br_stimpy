"""GroupStimulusStruct class

Defines a class for use with stimpy.Stimulator.group_stimulus()
"""
# Author: Jeff Weiss <jeff.weiss@pitt.edu>
# February 2023


from __future__ import annotations  # ensure forward compatibility
from br_stimpy.constants import *
from br_stimpy._validation import _ValidationFcns
from typing import List, Optional, Any


class GroupStimulusStruct(object):
    """Group Stimulus Structure

    Structure to input to Stimulator.group_stimulus() function.

    Optionally accepts electrode and pattern ID lists as input.
    Constructor will check that electrode and pattern IDs are valid and
    not longer than MAX_MODULES. Will zero-pad lists to length
    MAX_MODULES. User cannot modify these lengths after object creation.

    Args:
        electrode:
            List of electrodes to stimulate on, up to length
            MAX_MODULES. Defaults to None.
        pattern:
            List of pattern config IDs to match to electrodes above.
            Must be same length as electrode list. Defaults to None.
    
    Raises:
        ValueError: Electrode and Pattern lists must be the same length and cannot be longer than MAX_MODULES.
    """

    def __init__(
        self, electrode: Optional[List[int]] = None, pattern: Optional[List[int]] = None
    ):
        
        if electrode:
            self._number = len(electrode)
        else:
            self._number = 0

        if pattern:
            num_pat = len(pattern)
        else:
            num_pat = 0

        if num_pat != self._number:
            raise ValueError(f"Electrode and Pattern lists must be the same length")

        if self._number > MAX_MODULES:
            raise ValueError(
                f"Cannot simultaneously stimulate on more than {MAX_MODULES} electrodes."
            )

        for idx in range(0, self._number):
            _ValidationFcns.validate_electrode(electrode[idx])
            _ValidationFcns.validate_configID(pattern[idx])

        if self._number:
            self._electrode = electrode
            self._pattern = pattern
            if self._number < MAX_MODULES:
                ext_len = MAX_MODULES - self._number
                self._electrode.extend([0] * ext_len)
                self._pattern.extend([0] * ext_len)
        else:
            self._electrode = [0] * MAX_MODULES
            self._pattern = [0] * MAX_MODULES

    @property
    def electrode(self) -> List[int]:
        """List of electrodes"""
        return self._electrode

    @property
    def pattern(self) -> List[int]:
        """List of pattern IDs corresponding to electrode"""
        return self._pattern

    @property
    def number(self) -> int:
        """Number of electrodes contained in the group"""
        return self._number
