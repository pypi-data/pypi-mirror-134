#
# Config file for the OpenTREP Python package.
# It defines the following variables:
#  OPENTREP_VERSION         - version of OpenTREP
#  OPENTREP_PY_LIBRARY_DIRS - Python library directories for OpenTrep
#  OPENTREP_PY_LIBRARIES    - Python libraries to link against
#  OPENTREP_PY_EXECUTABLES  - Python binaries/executables
#

# Tell the user project where to find OpenTREP Python libraries
set (OPENTREP_VERSION "0.07.10")
set (OPENTREP_PY_LIBRARY_DIRS "/Users/DENIS/dev/geo/opentrep/_skbuild/macosx-12.0-x86_64-3.9/cmake-install/lib/python3.9/site-packages/pyopentrep")

# Library dependencies for OpenTrep (contains definitions for the OpenTREP
# IMPORTED targets)
include ("/Users/DENIS/dev/geo/opentrep/_skbuild/macosx-12.0-x86_64-3.9/cmake-install/share/opentrep/CMake/opentrep-python-library-depends.cmake")

# These are the OpenTREP IMPORTED targets, created by
# opentrep-python-library-depends.cmake
set (OPENTREP_PY_LIBRARIES pyopentreplib)
set (OPENTREP_PY_EXECUTABLES pyopentrep)

