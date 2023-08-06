
# This cmake will integrate the setup for the python package


set(manifest_config_file      ${YAYI_PYTHON_PACKAGE_LOCATION}/MANIFEST.in.config)
set(manifest_file             ${YAYI_PYTHON_PACKAGE_LOCATION}/MANIFEST.in)

if(NOT YAYI_PYTHON_PACKAGE_INSTALLATION_DIR)
  set(YAYI_PYTHON_PACKAGE_INSTALLATION_DIR ${YAYI_PYTHON_PACKAGE_LOCATION})
endif()
set(python_package_binary_dir ${YAYI_PYTHON_PACKAGE_INSTALLATION_DIR}/yayi/bin/)
get_filename_component(python_package_binary_dir ${python_package_binary_dir} ABSOLUTE)

set(python_package_binary_dir ${python_package_binary_dir} CACHE INTERNAL "python package binary destination path")



# this variable will contain additional include commands generated at setup.py time
set(YAYI_ADDITIONAL_INCLUDE_CMDS CACHE INTERNAL "manifest additional files")

# this variable will be filled during calls to add_files_to_python_packaging and add_to_python_packaging
set(YAYI_PYTHON_BINARY_EXTENSIONS "" CACHE INTERNAL "targets to copy to the python packaging")

# binary files with relocation
set(YAYI_PYTHON_BINARY_RELOCATION "" CACHE INTERNAL "targets to copy to the python packaging")





# ######################################################
#
# Adds the specified target to the python packaging system.
macro(add_to_python_packaging target_name)

  get_target_property(test_var ${target_name} INTERFACE_LINK_LIBRARIES)

  # do not install the .lib parts
  if(WIN32)
    set(element_to_install RUNTIME)
  else()
    set(element_to_install LIBRARY)
  endif()

  #list_prerequisites(${target_name} 0 0 1)

  # parsing the dependencies
  foreach(v ${test_var})
    if(TARGET ${v})
      # target known, we copy it
      set(YAYI_PYTHON_BINARY_EXTENSIONS ${YAYI_PYTHON_BINARY_EXTENSIONS} ${v} CACHE INTERNAL "source file to copy")

      install(
        TARGETS ${v}
        ${element_to_install}
          DESTINATION ${python_package_binary_dir}
          COMPONENT python_package_install_intermediate
      )

    endif()
    # We should also copy things that are not targets (check for thirdparties), but we do not want to copy system libraries.
    # This is performed in another function which does not check the graph of dependencies
  endforeach()

  # copy the main target
  # @todo better if the files here are explicitely stated (rather than a *.so in the manifest)
  set(YAYI_PYTHON_BINARY_EXTENSIONS ${YAYI_PYTHON_BINARY_EXTENSIONS} ${target_name} CACHE INTERNAL "source file to copy")

  install(
    TARGETS ${target_name}
    ${element_to_install}
      DESTINATION ${python_package_binary_dir}
      COMPONENT python_package_install_intermediate
  )


endmacro(add_to_python_packaging)


# ######################################################
#
# Add the specified files to the python packaging system
# add_files_to_python_packaging(FILES file1 [file2 ...]
#                               INSTALL_DLL ONLY_DLL )
#
# - INSTALL_DLL is set, install the DLLs corresponding to the .lib files as well. Ignored on non WIN32 platforms
# - ONLY_DLL is set, install only the DLLs corresponding to the .lib files (.libs are ignored). Ignored on non WIN32 platforms
macro(add_files_to_python_packaging)

  set(options INSTALL_DLL ONLY_DLL)
  set(oneValueArgs)
  set(multiValueArgs FILES)
  cmake_parse_arguments(_local_vars "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})

  set(_additional_files)

  if(WIN32 AND ${_local_vars_INSTALL_DLL})
    foreach(_local_vars ${_local_vars_FILES})
      get_filename_component(_filepathabs ${_local_vars} ABSOLUTE)
      get_filename_component(_filepath ${_filepathabs} PATH)
      get_filename_component(_filename ${_filepathabs} NAME_WE)
      set(_file_to_install ${_filepath}/${_filename}${CMAKE_SHARED_LIBRARY_SUFFIX})
      if(NOT EXISTS ${_file_to_install})
        message("[YAYI][install] file ${_file_to_install} does not EXISTS !!!")
      else()
        set(_additional_files ${_additional_files} ${_file_to_install})
      endif()

      unset(_filepathabs)
      unset(_filepath)
      unset(_filename)
      unset(_file_to_install)

    endforeach()


    if(${_local_vars_ONLY_DLL})
      set(_local_vars_FILES) # empty to have only the .dll part
    endif()

  elseif(APPLE AND ${_local_vars_INSTALL_DLL})
    # binary relocation for MAC
    foreach(_local_vars ${_local_vars_FILES})
      get_filename_component(_filename ${_local_vars} NAME)
      set(YAYI_PYTHON_BINARY_RELOCATION ${YAYI_PYTHON_BINARY_RELOCATION} ${_filename} CACHE INTERNAL "relocation files")
    endforeach()
  endif()

  set(_local_vars_FILES ${_local_vars_FILES} ${_additional_files})

  # for the manifest.in file
  foreach(_local_vars ${_local_vars_FILES})
    get_filename_component(_v_file_name ${_local_vars} NAME)
    set(YAYI_ADDITIONAL_INCLUDE_CMDS ${YAYI_ADDITIONAL_INCLUDE_CMDS} "include yayi/bin/${_v_file_name}" CACHE INTERNAL "manifest additional files")
    unset(_v_file_name)
  endforeach()

  # install rule
  install(
      FILES ${_local_vars_FILES}
      DESTINATION ${python_package_binary_dir}
      COMPONENT python_package_install_intermediate
    )

  unset(_local_vars)

endmacro(add_files_to_python_packaging)



# creates the install rules for the python installation on the system
function(create_python_package_system)
  file(GLOB _v_glob RELATIVE "${YAYI_root_dir}" "${YAYI_PYTHON_PACKAGE_LOCATION}}/yayi/*")

  install(FILES ${_v_glob}
          CONFIGURATIONS Release
          DESTINATION ${YAYI_PYTHON_PACKAGE_INSTALLATION_DIR}/yayi
          COMPONENT python)


endfunction()


# ######################################################
#
# This function gathers all information collected by the build tree to create the appropriate python packaging
macro(create_python_package)
  message(STATUS "[YAYIPython] Configuring Python package manifest ${YAYI_ADDITIONAL_INCLUDE_CMDS}")

  # should have been cached
  if(NOT DEFINED PYTHON_MODULES_EXTENSIONS)
    message(FATAL_ERROR "Something wrong in the configuration (PYTHON_MODULES_EXTENSIONS not defined)")
  endif()


  set(YAYI_PYTHON_EXT ${PYTHON_MODULES_EXTENSIONS})
  set(YAYI_PLATFORM_SO_EXT ${CMAKE_SHARED_LIBRARY_SUFFIX})
  set(_var_concat "")
  foreach(c IN LISTS YAYI_ADDITIONAL_INCLUDE_CMDS)
    set(_var_concat "${_var_concat}\n${c}")
  endforeach(c)
  set(YAYI_ADDITIONAL_INCLUDE_CMDS ${_var_concat})
  unset(_var_concat)

  if(EXISTS ${manifest_config_file})
    configure_file(${manifest_config_file} ${manifest_file} @ONLY)
  else()
    message(STATUS "[YAYI][pythonext] not configuring the MANIFEST.in since the template ${manifest_config_file} is not found."
                    "Should be an archive/source distribution, MANIFEST.in already configured?")
  endif()


  # declares the Python packaging target
  set(yayi_python_package_SRC
      ${YAYI_PYTHON_PACKAGE_LOCATION}/setup.py)

  if(EXISTS ${manifest_config_file})
    set(yayi_python_package_SRC
        ${yayi_python_package_SRC}
        ${manifest_config_file}
       )
  endif()


  # custom target just for installing the files to the appropriate place
  add_custom_target(
    PythonPackageSetup
    COMMENT "Python packaging"
    COMMAND ${CMAKE_COMMAND} -E echo " --+ [YAYI][pythonpackage] Installing the python package component to ${python_package_binary_dir} from ${CMAKE_BINARY_DIR}"
    COMMAND ${CMAKE_COMMAND} -E echo "${CMAKE_COMMAND} -DCOMPONENT=python_package_install_intermediate -P ${CMAKE_BINARY_DIR}/cmake_install.cmake"
    COMMAND ${CMAKE_COMMAND} -DCOMPONENT=python_package_install_intermediate -P ${CMAKE_BINARY_DIR}/cmake_install.cmake
    SOURCES ${yayi_python_package_SRC}
  )

  # dependencies of the build target
  list(LENGTH YAYI_PYTHON_BINARY_EXTENSIONS ext_length)
  if(${ext_length})
    add_dependencies(PythonPackageSetup ${YAYI_PYTHON_BINARY_EXTENSIONS})
  endif()



  # command built on the fly for pre/post-building the component installation
  # This is helpfull for creating relocatable binaries/python package, especially on OSX
  set(pre_build_cmd
      COMMAND ${CMAKE_COMMAND} -E echo " --+ [YAYI][pythonpackage] Creating destination directory ${python_package_binary_dir}"
      COMMAND ${CMAKE_COMMAND} -E make_directory ${python_package_binary_dir}
  )

  set(post_build_cmd "")

  # relocation after installation, in place
  list(LENGTH YAYI_PYTHON_BINARY_RELOCATION ext_length)
  if("${ext_length}" AND APPLE)
    foreach(_local_vars IN LISTS YAYI_PYTHON_BINARY_RELOCATION)
      set(post_build_cmd
          ${post_build_cmd}
          COMMAND ${CMAKE_COMMAND} -E echo " --+ [YAYI][pythonpackage] Relocating =file/dependency= ${_local_vars}"
          COMMAND ${PYTHON_EXECUTABLE} ${YAYI_root_dir}/cmake/osx_install_name_tool_utility.py
            ${python_package_binary_dir}/${_local_vars}
            ${python_package_binary_dir}
            "boost"
          )
    endforeach()
  endif()

  # relocation of the known targets, after the installation, in place
  list(LENGTH YAYI_PYTHON_BINARY_EXTENSIONS ext_length)
  if("${ext_length}" AND APPLE)
    # those are targets
    foreach(_local_vars IN LISTS YAYI_PYTHON_BINARY_EXTENSIONS)
      set(post_build_cmd
          ${post_build_cmd}
          COMMAND ${CMAKE_COMMAND} -E echo " --+ [YAYI][pythonpackage] Relocating =target= ${_local_vars}"
          COMMAND ${PYTHON_EXECUTABLE} ${YAYI_root_dir}/cmake/osx_install_name_tool_utility.py
            ${python_package_binary_dir}/$<TARGET_SONAME_FILE_NAME:${_local_vars}>
            ${python_package_binary_dir}/
            "boost"
          )
    endforeach()
  endif()

  if(NOT "${pre_build_cmd}" STREQUAL "")
    add_custom_command(
      TARGET PythonPackageSetup
      PRE_BUILD
      ${pre_build_cmd})
  endif()


  if(NOT "${post_build_cmd}" STREQUAL "")
    add_custom_command(
      TARGET PythonPackageSetup
      POST_BUILD
      ${post_build_cmd})
  endif()

endmacro(create_python_package)
