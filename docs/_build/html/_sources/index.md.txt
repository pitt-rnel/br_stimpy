```{toctree}
   :hidden:

   Home page <self>
   API Reference <_autosummary/br_stimpy.stimpy>
```

# br_stimpy: python wrapper for the Blackrock Neurotech Cerestim API
br_stimpy is an unofficial python wrapper for the [Blackrock
Neurotech](https://blackrockneurotech.com) Cerestim API. br_stimpy was developed
by Jeff Weiss at the University of Pittsburgh's [Rehab Neural Engineering
Labs](https://rnel.pitt.edu). The author of this package is not affiliated with
Blackrock Neurotech.

## Dependencies and Installation
This package depends on the Blackrock Cerestim API (for C++),
[pybind11](https://github.com/pybind/pybind11), and a C++ compiler.

The Blackrock Cerestim API can be downloaded from their website
[here](https://blackrockneurotech.com/research/wp-content/software/CereStim-API.zip).
The SDK should be unzipped into the `extern/` directory (such that the binary
and header files are located in `extern/Cerestim-API/Binaries`).

Pybind11 is included as a git submodule and can be initialized in the source
tree by running:

```sh
git submodule update --init
```

Once these dependencies are met, the package can be built and installed with pip
from the package directory by running:

```sh
pip install .
```

## Quick Example:
```python
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
```

See additional examples in the examples directory. Or start with API
documentation for the {py:class}`br_stimpy.stimpy.Stimulator` class within the
{py:mod}`br_stimpy.stimpy` module.


## Maintainer
Maintained by [Jeff Weiss](https://github.com/jmw182) and
[RNEL](https://github.com/pitt-rnel) at the University of Pittsburgh.

### Disclaimer
The graphic included in this README is not intended to be an official logo or
mascot for this package. The maintainers of this package do not claim any
ownership over the copyright of this image or the character depicted within it.
The authors of this package are not affiliated with Blackrock Neurotech.