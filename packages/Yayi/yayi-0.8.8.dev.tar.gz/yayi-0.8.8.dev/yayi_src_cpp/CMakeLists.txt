# The name of our project is "YAYI". CMakeLists files in this project can
# refer to the root source directory of the project as ${YAYI_SOURCE_DIR} and
# to the root binary directory of the project as ${YAYI_BINARY_DIR}.

# example of run on MAC OS X
# cmake -DENABLE_HDF5=True -DBOOST_INSTALLATION_DIR=~/ThirdParties/install__Darwin_i386/ -DHDF5_INSTALL_DIR=~/ThirdParties/install__Darwin_i386/ -DCMAKE_BUILD_TYPE=Release CMakeLists.txt
# cmake -G "Visual Studio 10" -DBOOST_INSTALLATION_DIR="C:\Documents and Settings\Raffi\Mes documents\Code Raffi\Externals\boost_1_46_1" CMakeLists.txt

# cmake -DBOOST_ROOT=~/Code/sw_thirdparties/osx/boost_1_55_patched/ -DBoost_COMPILER=-clang-darwin42 ..


cmake_minimum_required (VERSION 2.8.12)

project(Yayi)


# some global properties
set_property(GLOBAL PROPERTY USE_FOLDERS ON)
set_property(GLOBAL PROPERTY PREDEFINED_TARGETS_FOLDER "CMakePredefined")

# build type, by default to release (with optimisations)
if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  message(STATUS "Setting build type to 'Release' as none was specified.")
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)
  # Set the possible values of build type for cmake-gui
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()


enable_testing()

# current version
set(YAYI_MAJOR    0 )
set(YAYI_MINOR    8 )
set(YAYI_SUBMINOR 8 )
set(YAYI_VERSION ${YAYI_MAJOR}.${YAYI_MINOR}.${YAYI_SUBMINOR})


option(BUILD_SHARED_LIBS "Build Shared Libraries" ON)

set(ENABLE_HDF5  FALSE CACHE BOOL "Enable HDF5 support (you should have it already built)")
set(ENABLE_NUMPY FALSE CACHE BOOL "Enable NumPy support for YayiIOPython (should be installed in your python distribution")

set(YAYI_root_dir         ${Yayi_SOURCE_DIR}   CACHE PATH "Base of the input directory")

# General library settings
set(YAYI_CORE_DIR
    ${YAYI_root_dir}/core
    CACHE PATH
    "Root path of the Core of YAYI")

set(YAYI_CORE_TEST_DIR
    ${YAYI_root_dir}/coreTests
    CACHE PATH
    "Root path of the Core of YAYI's tests")

set(YAYI_PYTHONEXT_DIR
    ${YAYI_root_dir}/python
    CACHE PATH
    "Python extension root path of YAYI")

set(THIRD_PARTIES_PATH
    ${YAYI_root_dir}/plugins/external_libraries
    CACHE PATH
    "Directory of the external third parties installation (built outside the project)")

set(TEMPORARY_DIRECTORY
    ${CMAKE_BINARY_DIR}/temporary/
    CACHE PATH
    "Directory for temporary files")

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin/)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin/)


# this is where the python package is located. The Yayi binaries will be copied
# into this place when creating the python package. This is also used for the Sphinx documentation.
if(NOT YAYI_PYTHON_PACKAGE_LOCATION)
  set(YAYI_PYTHON_PACKAGE_LOCATION ${YAYI_root_dir}/plugins/PythonPackage)
endif()
file(TO_CMAKE_PATH ${YAYI_PYTHON_PACKAGE_LOCATION} YAYI_PYTHON_PACKAGE_LOCATION)
message(STATUS "[YAYI][python] package location is ${YAYI_PYTHON_PACKAGE_LOCATION}")

# Compiler specific configurations
# this also includes some boost configurations
include(cmake/CMakeCompilerSpecific.cmake)


# relocatable binaries, so that we can use wheel
# actually this should be set by the setup.py if needed
if(APPLE)
  set(CMAKE_SKIP_BUILD_RPATH FALSE)
  set(CMAKE_BUILD_WITH_INSTALL_RPATH  TRUE)
  set(CMAKE_INSTALL_RPATH_USE_LINK_PATH FALSE)
  set(CMAKE_INSTALL_RPATH "@loader_path/.")
  set(CMAKE_MACOSX_RPATH ON)
endif()


message(STATUS "CMake ${CMAKE_VERSION} running on OS ${CMAKE_HOST_SYSTEM_NAME} version ${CMAKE_HOST_SYSTEM_VERSION} on processor ${CMAKE_HOST_SYSTEM_PROCESSOR}")
message(STATUS "HDF5 support is ${ENABLE_HDF5}")
message(STATUS "NumPy support is ${ENABLE_NUMPY}")

if(BUILD_SHARED_LIBS)
  message(STATUS "Building shared libraries")
  add_definitions(-DYAYI_DYNAMIC)
else()
  message(STATUS "Building static libraries")
endif()



# Some useful functions
include(CMakeParseArguments)
include(cmake/CMakeVersion.cmake)
include(cmake/CMakeInstallUtils.cmake)
include(cmake/CMakePCHUtils.cmake NO_POLICY_SCOPE)
include(cmake/CMakeInstallUtils.cmake)
include(cmake/CMakePythonUtils.cmake)
include(cmake/CMakeTestUtils.cmake)

# Python packaging
message(STATUS "Configuring the python packaging")
include(cmake/CMakePythonPackage.cmake)

# fix the isntallation folders
set_installation_paths()


# Third parties
add_subdirectory(${THIRD_PARTIES_PATH} ${TEMPORARY_DIRECTORY}/thirdParties)
add_definitions(-DBOOST_TEST_DYN_LINK)

# warning the order is important
include_directories(${YAYI_CORE_DIR})
include_directories(${YAYI_CORE_TEST_DIR})
include_directories(${YAYI_PYTHONEXT_DIR})


include_directories(${Boost_INCLUDE_DIRS})


# generating the versions files
generate_library_version(${YAYI_root_dir}/cmake/yayi_revision.cpp.config
                         ${YAYI_CORE_DIR}/yayiCommon/src/current_configuration_generated.cpp)

generate_library_version(${YAYI_root_dir}/cmake/yayi_revision.py.config
                         ${YAYI_PYTHON_PACKAGE_LOCATION}/yayi/version.py)



# the yayi core libraries
add_subdirectory (${YAYI_CORE_DIR}/yayiCommon                 ${TEMPORARY_DIRECTORY}/yayiCommon)
add_subdirectory (${YAYI_CORE_DIR}/yayiImageCore              ${TEMPORARY_DIRECTORY}/yayiImageCore)
add_subdirectory (${YAYI_CORE_DIR}/yayiIO                     ${TEMPORARY_DIRECTORY}/yayiIO)
add_subdirectory (${YAYI_CORE_DIR}/yayiStructuringElement     ${TEMPORARY_DIRECTORY}/yayiStructuringElement)
add_subdirectory (${YAYI_CORE_DIR}/yayiPixelProcessing        ${TEMPORARY_DIRECTORY}/yayiPixelProcessing)
add_subdirectory (${YAYI_CORE_DIR}/yayiLowLevelMorphology     ${TEMPORARY_DIRECTORY}/yayiLowLevelMorphology)
add_subdirectory (${YAYI_CORE_DIR}/yayiNeighborhoodProcessing ${TEMPORARY_DIRECTORY}/yayiNeighborhoodProcessing)
add_subdirectory (${YAYI_CORE_DIR}/yayiDistances              ${TEMPORARY_DIRECTORY}/yayiDistances)
add_subdirectory (${YAYI_CORE_DIR}/yayiSegmentation           ${TEMPORARY_DIRECTORY}/yayiSegmentation)
add_subdirectory (${YAYI_CORE_DIR}/yayiLabel                  ${TEMPORARY_DIRECTORY}/yayiLabel)
add_subdirectory (${YAYI_CORE_DIR}/yayiMeasurements           ${TEMPORARY_DIRECTORY}/yayiMeasurements)
add_subdirectory (${YAYI_CORE_DIR}/yayiReconstruction         ${TEMPORARY_DIRECTORY}/yayiReconstruction)


#export(PACKAGE Yayi)

# creates the python package
create_python_package()
create_python_package_system()



# this should be at the end, in order to retrieve all the include paths (could be also a bit earlier)
message(STATUS "[YAYIDoc] Configuring the documentation")
include(cmake/CMakeDoc.cmake)


add_custom_target(
  CMakeFiles
  SOURCES
  cmake/CMakeCompilerSpecific.cmake
  cmake/CMakeCPackConf.cmake
  cmake/CMakeDoc.cmake
  cmake/CMakeInstallUtils.cmake
  cmake/CMakeOptimizationLib.cmake
  cmake/CMakePCHUtils.cmake
  cmake/CMakePythonPackage.cmake
  cmake/CMakePythonUtils.cmake
  cmake/CMakeTestUtils.cmake
  cmake/CMakeVersion.cmake
  cmake/yayi_revision.cpp.config
  cmake/yayi_revision.py.config
  cmake/osx_install_name_tool_utility.py
  LICENSE_1_0.txt
  README.md
)

# Should be last
include(cmake/CMakeCPackConf.cmake)

