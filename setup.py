import sys, struct, shutil

#from pybind11 import get_cmake_dir
# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

__version__ = "0.0.1"

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

lib_dir = './extern/CereStim-API/Binaries/'
if sys.platform == 'win32': # windows
    bitness = struct.calcsize("P")*8 # determine if 32-bit or 64-bit python
    if bitness == 64: # 64-bit
        #lib_dir = '../x64/Release/'
        lib_name = 'BStimAPIx64'
    else: # 32-bit
        #lib_dir = '../Win32/Release/'
        lib_name = 'BStimAPIx86'
    shutil.copy2(lib_dir+lib_name+'.dll','.')
    shutil.copy2(lib_dir+lib_name+'.lib','.')
else: # linux or mac
    #lib_dir = '../'
    lib_name = 'BStimAPI'
    if sys.platform == 'darwin': # mac
        lib_ext = '.dylib'
    else:
        lib_ext = '.so'
    shutil.copy2(lib_dir+'lib'+lib_name+lib_ext,'.')


ext_modules = [
    Pybind11Extension("_bstimulator",
        ["br_stimpy/_pybstimulator.cpp"],
        # Example: passing in the version to the compiled code
        define_macros = [('VERSION_INFO', __version__)],
        libraries = [lib_name],
        language='c++'
        ),
]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="br_stimpy",
    version=__version__,
    author="Jeff Weiss",
    author_email="jeff.weiss@pitt.edu",
    url="https://github.com/pitt-rnel/br_stimpy",
    description="br_stimpy: python bindings to Blackrock Neurotech Cerestim API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    ext_modules=ext_modules,
    #extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.6",
)