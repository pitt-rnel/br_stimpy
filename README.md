stimpy: python wrapper for cerestim API

This package depends on the Blackrock Cerestim API (for C++), pybind11, and a C++ compiler.

The Blackrock Cerestim API can be downloaded from their website [here](https://blackrockneurotech.com/research/wp-content/software/CereStim-API.zip). The SDK should be unzipped into the `extern` directory (such that the binary and header files are located in `extern/Cerestim-API/Binaries`).

Pybind11 is included as a git submodule and can be initialized in the source tree by running `git submodule update --init`.

Once these dependencies are met, the package can be compiled and installed with `pip install .`