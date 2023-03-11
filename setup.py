import sys
import struct
import shutil
import glob
import os
from codecs import open

# from pybind11 import get_cmake_dir
# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

lib_dir = "extern/CereStim-API/Binaries/"
if sys.platform == "win32":  # windows
    bitness = struct.calcsize("P") * 8  # determine if 32-bit or 64-bit python
    if bitness == 64:  # 64-bit
        # lib_dir = '../x64/Release/'
        lib_name = "BStimAPIx64"
    else:  # 32-bit
        # lib_dir = '../Win32/Release/'
        lib_name = "BStimAPIx86"
    lib_ext = ".dll"
    lib_fname = lib_dir + lib_name + lib_ext

else:  # linux or mac
    # lib_dir = '../'
    lib_name = "BStimAPI"
    if sys.platform == "darwin":  # mac
        lib_ext = ".dylib"
    else:
        lib_ext = ".so"
    lib_fname = lib_dir + "lib" + lib_name + lib_ext
lib_glob_str = "*" + lib_ext
for file in glob.glob(lib_dir + lib_glob_str):
    # copy libs to module dir
    shutil.copy2(file, "br_stimpy")

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "br_stimpy", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()

ext_modules = [
    Pybind11Extension(
        "br_stimpy._bstimulator",
        ["br_stimpy/_pybstimulator.cpp"],
        # Example: passing in the version to the compiled code
        define_macros=[("VERSION_INFO", about["__version__"])],
        libraries=[lib_name],
        library_dirs=[lib_dir],
        include_dirs=["br_stimpy"],
        depends=["_pybstimulator.h"],
        language="c++",
    )
]

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    ext_modules=ext_modules,
    packages=["br_stimpy"],
    package_data={"br_stimpy": [lib_glob_str, "*.h"]},
    license=about["__license__"],
    # extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)
