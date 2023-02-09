# br_stimpy.group_stim_struct
# Author: Jeff Weiss <jeff.weiss@pitt.edu>
# February 2023

from __future__ import annotations  # ensure forward compatibility
from br_stimpy.constants import *
from br_stimpy._validation import ValidationFcns
from typing import List, Optional, Any

class GroupStimulusStruct(object):
    """Group Stimulus Structure

    Structure to input to Stimulator.group_stimulus() function.

    Optionally accepts electrode and pattern ID lists as input.
    Constructor will check that electrode and pattern IDs are valid and
    not longer than MAX_MODULES. Will zero-pad lists to length
    MAX_MODULES. User cannot modify these lengths after object creation.
    """

    def __init__(
        self, electrode: Optional[List[int]] = None, pattern: Optional[List[int]] = None
    ) -> None:
        """
        GroupStimulusStruct constructor

        Args:
            electrode (Optional[List[int]], optional):
                List of electrodes to stimulate on, up to length
                MAX_MODULES. Defaults to None.
            pattern (Optional[List[int]], optional):
                List of pattern config IDs to match to electrodes above.
                Must be same length as electrode list. Defaults to None.

        Raises:
            ValueError: Electrode and Pattern lists must be the same length and cannot be longer than MAX_MODULES.
        """
        if electrode:
            self._num_elec = len(electrode)
        else:
            self._num_elec = 0

        if pattern:
            self._num_pat = len(pattern)
        else:
            self._num_pat = 0

        if self._num_elec > MAX_MODULES or self._num_pat > MAX_MODULES:
            raise ValueError(
                f"Cannot simultaneously stimulate on more than {MAX_MODULES} electrodes."
            )

        if self._num_elec != self._num_pat:
            raise ValueError(f"Electrode and Pattern lists must be the same length")

        for idx in range(0, self._num_elec):
            ValidationFcns.validate_electrode(electrode[idx])
            ValidationFcns.validate_configID(pattern[idx])

        if self._num_elec:
            self._electrode = electrode
            self._pattern = pattern
            if self._num_elec < MAX_MODULES:
                ext_len = MAX_MODULES - self._num_elec
                self._electrode.extend([0] * ext_len)
                self._pattern.extend([0] * ext_len)
        else:
            self._electrode = [0] * MAX_MODULES
            self._pattern = [0] * MAX_MODULES

        @property
        def electrode(self) -> List[int]:
            return self._electrode

        @property 
        def pattern(self) -> List[int]:
            return self._pattern