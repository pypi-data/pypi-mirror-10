##
##
## Installation
##
set(CPACK_PACKAGE_NAME                  "yayi")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY   "Mathematical morphology and image processing framework for research and development")
set(CPACK_PACKAGE_VENDOR                "Raffi Enficiaud")

set(CPACK_PACKAGE_DESCRIPTION_FILE      "${YAYI_root_dir}/README.md")
set(CPACK_RESOURCE_FILE_LICENSE         "${YAYI_root_dir}/LICENSE_1_0.txt")
set(CPACK_PACKAGE_VERSION_MAJOR         ${YAYI_MAJOR})
set(CPACK_PACKAGE_VERSION_MINOR         ${YAYI_MINOR})
set(CPACK_PACKAGE_VERSION_PATCH         ${YAYI_SUBMINOR})
set(CPACK_PACKAGE_VERSION               ${CPACK_PACKAGE_VERSION_MAJOR}.${CPACK_PACKAGE_VERSION_MINOR}.${CPACK_PACKAGE_VERSION_PATCH})
set(CPACK_PACKAGE_INSTALL_DIRECTORY     "yayi")
set(CPACK_PACKAGE_CONTACT               "Raffi Enficiaud <raffi.enficiaud@free.fr>")

# components setup
set(CPACK_COMPONENTS_ALL CORE CORE-DEV PYTHON API_DOC PYTHON_DOC)
set(CPACK_COMPONENT_CORE_DISPLAY_NAME           "Core libraries")
set(CPACK_COMPONENT_CORE-DEV_DISPLAY_NAME       "Core libraries development files")
set(CPACK_COMPONENT_PYTHON_DISPLAY_NAME         "Python extensions")
set(CPACK_COMPONENT_API_DOC_DISPLAY_NAME        "Developer C++ documentation")
set(CPACK_COMPONENT_PYTHON_DOC_DISPLAY_NAME     "Developer Python documentation")

set(CPACK_COMPONENT_CORE_DESCRIPTION            "Shared libraries for running programs based on Yayi")
set(CPACK_COMPONENT_CORE-DEV_DESCRIPTION        "C++ Headers for developing with Yayi")
set(CPACK_COMPONENT_PYTHON_DESCRIPTION          "Python extensions for prototyping with Yayi")
set(CPACK_COMPONENT_API_DOC_DESCRIPTION         "Auto generated doxygen documentation of the C++ part of Yayi")
set(CPACK_COMPONENT_PYTHON_DOC_DESCRIPTION      "Auto generated Sphinx documentation of the Python bindings and Python packages of Yayi")

set(CPACK_COMPONENT_PYTHON_DEPENDS              CORE)
set(CPACK_COMPONENT_CORE-DEV_DEPENDS            CORE)
set(CPACK_COMPONENT_API-DOC_DEPENDS             CORE-DEV)
set(CPACK_COMPONENT_PYTHON-DOC_DEPENDS          PYTHON)

set(CPACK_COMPONENT_PYTHON_DOC_GROUP                "Documentation")
set(CPACK_COMPONENT_API_DOC_GROUP                   "Documentation")
set(CPACK_COMPONENT_GROUP_DOCUMENTATION_DESCRIPTION "Documentation")

# source package configuration
set(CPACK_SOURCE_PACKAGE_FILE_NAME "yayi_${YAYI_VERSION}")
set(CPACK_SOURCE_IGNORE_FILES
    ${CPACK_SOURCE_IGNORE_FILES}
    ${CMAKE_BINARY_DIR}
    ${YAYI_root_dir}/.git
    ${YAYI_root_dir}/.gitignore
    ${YAYI_root_dir}/debian
    ${YAYI_root_dir}/plugins/project_management
    ${YAYI_root_dir}/plugins/Benches
    ${YAYI_root_dir}/plugins/WebSite
    ${YAYI_root_dir}/plugins/www_jekyll
    ${YAYI_root_dir}/plugins/PythonPackage/yayi/bin
    ${YAYI_root_dir}/working-dir # in case I am playing with bazaar
    )

file(GLOB_RECURSE _v_glob_tmp ${YAYI_root_dir}/*.pyc
                              ${YAYI_root_dir}/*.user
                              ${YAYI_root_dir}/*~
                              ${YAYI_root_dir}/*.recipe)
set(CPACK_SOURCE_IGNORE_FILES
    ${CPACK_SOURCE_IGNORE_FILES}
    ${_v_glob_tmp})

file(GLOB _v_glob_tmp RELATIVE "${YAYI_root_dir}" "${YAYI_root_dir}/plugins/Logos/*.*")
list(REMOVE_ITEM _v_glob_tmp "plugins/Logos/yayi_logo_seul.png")
set(CPACK_SOURCE_IGNORE_FILES
    ${CPACK_SOURCE_IGNORE_FILES}
    ${_v_glob_tmp})
unset(_v_glob_tmp)

# under Linux, we add the image I/O libs to the exclusion list
if(UNIX AND NOT APPLE)
  file(GLOB _v_glob RELATIVE "${YAYI_root_dir}" "${YAYI_root_dir}/plugins/external_libraries/*.tar*")
  set(CPACK_SOURCE_IGNORE_FILES
      ${CPACK_SOURCE_IGNORE_FILES}
      ${_v_glob}
      ${YAYI_root_dir}/plugins/external_libraries/Config)
  # the name is changed to comply with the Debian rules
  set(CPACK_SOURCE_PACKAGE_FILE_NAME "yayi-${YAYI_VERSION}")
  #set(CPACK_INCLUDE_TOPLEVEL_DIRECTORY FALSE) # no directory in the tar
  set(CPACK_SOURCE_GENERATOR "TGZ")
endif()

#set(CPACK_ALL_INSTALL_TYPES Full Developer Python)
#set(CPACK_COMPONENT_LIBRARIES_INSTALL_TYPES         Python Developer Full)
#set(CPACK_COMPONENT_HEADERS_INSTALL_TYPES           Developer Full)
#set(CPACK_COMPONENT_PYTHON_INSTALL_TYPES            Python Full)



if(WIN32 AND NOT UNIX)
  # There is a bug in NSI that does not handle full unix paths properly. Make
  # sure there is at least one set of four (4) backlasshes.
  #set(CPACK_PACKAGE_ICON                "")
  #set(CPACK_NSIS_INSTALLED_ICON_NAME    "")
  set(CPACK_NSIS_DISPLAY_NAME           "${CPACK_PACKAGE_INSTALL_DIRECTORY}")
  set(CPACK_NSIS_HELP_LINK              "http:////raffi.enficiaud.free.fr")
  set(CPACK_NSIS_URL_INFO_ABOUT         "http:////raffi.enficiaud.free.fr")
  set(CPACK_NSIS_CONTACT                "raffi.enficiaud@free.fr")
  set(CPACK_NSIS_MODIFY_PATH            ON)

  set(CPACK_NSIS_ENABLE_UNINSTALL_BEFORE_INSTALL ON)
  set(CPACK_NSIS_URL_INFO_ABOUT ${CPACK_NSIS_HELP_LINK})
  set(CPACK_NSIS_MENU_LINKS
       "documentation/index.html" "C++ library documentation"
       )


  if(CMAKE_CL_64)
    set(CPACK_NSIS_INSTALL_ROOT "$PROGRAMFILES64")
    set(CPACK_NSIS_PACKAGE_NAME "${CPACK_PACKAGE_INSTALL_DIRECTORY} (Win64)")
    set(CPACK_PACKAGE_INSTALL_REGISTRY_KEY "${CPACK_PACKAGE_NAME} ${CPACK_PACKAGE_VERSION} (Win64)")
  else()
    set(CPACK_NSIS_INSTALL_ROOT "$PROGRAMFILES")
    set(CPACK_NSIS_PACKAGE_NAME "${CPACK_PACKAGE_INSTALL_DIRECTORY}")
    set(CPACK_PACKAGE_INSTALL_REGISTRY_KEY "${CPACK_PACKAGE_NAME} ${CPACK_PACKAGE_VERSION}")
  endif()


else()
  set(CPACK_STRIP_FILES                 TRUE)
  #set(CPACK_SOURCE_STRIP_FILES          TRUE)
endif()



# debian package generation
if(UNIX AND NOT APPLE)
  set(CPACK_GENERATOR DEB)
  set(CPACK_MONOLITHIC_INSTALL OFF)
  #set(CPACK_DEB_PACKAGE_COMPONENT core core-dev)
  set(CPACK_DEB_COMPONENT_INSTALL "ON")#TRUE)
  set(CPACK_COMPONENTS_ALL_IN_ONE_PACKAGE)
  #set(CPACK_DEB_PACKAGE_COMPONENT TRUE)
  set(CPACK_COMPONENTS_GROUPING "IGNORE")
  #set(CPACK_COMPONENTS_IGNORE_GROUPS TRUE)

  set(CPACK_DEBIAN_PACKAGE_DESCRIPTION ${CPACK_PACKAGE_DESCRIPTION_SUMMARY})

  # default shlibdeps off
  set(CPACK_DEBIAN_PACKAGE_SHLIBDEPS OFF)

  set(CPACK_DEBIAN_PACKAGE_DEBUG TRUE)
  set(CPACK_DEBIAN_PACKAGE_DEPENDS)
  list(LENGTH debian_dependencies debian_dependencies_lenght)
  if(${debian_dependencies_lenght} GREATER 0)
    list(GET debian_dependencies 0 CPACK_DEBIAN_PACKAGE_DEPENDS)
    list(REMOVE_AT debian_dependencies 0)
  endif()

  foreach(var IN LISTS debian_dependencies)
    set(CPACK_DEBIAN_PACKAGE_DEPENDS "${CPACK_DEBIAN_PACKAGE_DEPENDS}, ${var}")
  endforeach()

  # lets shlibdeps make its job for the core component
  set(CPACK_DEBIAN_CORE_PACKAGE_SHLIBDEPS ON)
  set(CPACK_DEBIAN_CORE_PACKAGE_DEPENDS "")

  # the other components dependencies are explicitely defined
  set(CPACK_DEBIAN_CORE-DEV_PACKAGE_DEPENDS "yayi-core (= ${CPACK_PACKAGE_VERSION}), libboost-all-dev")
  set(CPACK_DEBIAN_PYTHON_PACKAGE_DEPENDS "yayi-core (= ${CPACK_PACKAGE_VERSION}), python, python-numpy")
  set(CPACK_DEBIAN_API_DOC_PACKAGE_DEPENDS "yayi-core-dev (= ${CPACK_PACKAGE_VERSION})")
  set(CPACK_DEBIAN_PYTHON_DOC_PACKAGE_DEPENDS "yayi-python (= ${CPACK_PACKAGE_VERSION})")


endif()
include(CPack)
