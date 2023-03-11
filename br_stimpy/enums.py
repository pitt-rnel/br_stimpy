# br_stimpy.enums
# Author: Jeff Weiss <jeff.weiss@pitt.edu>
# February 2023

from __future__ import annotations  # ensure forward compatibility
from br_stimpy import _bstimulator

# add references to enums and other classes from _bstimulator
OCVolt = _bstimulator.OCVolt  # enum class for compliance voltage
WFType = _bstimulator.WFType  # enum class for anodal or cathodal first
TriggerType = _bstimulator.TriggerType
ElectrodeChannelMap = _bstimulator.ElectrodeChannelMap
PartNumbers = _bstimulator.PartNumbers
ModuleStatus = _bstimulator.ModuleStatus
SeqType = _bstimulator.SeqType
ResultType = _bstimulator.ResultType
