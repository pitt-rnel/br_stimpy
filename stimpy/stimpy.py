# Author: Jeff Weiss <jeff.weiss@pitt.edu>
# May 2022

"""stimpy: a package to interface with Blackrock cerestim API."""

import _bstimulator

def stimpy_test():
    stimulator = _bstimulator.stimulator()
    devices = stimulator.scan_for_devices()
    stimulator.set_device(0)
    stimulator.connect
    return stimulator