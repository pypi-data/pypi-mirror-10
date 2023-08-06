# @file
# This file contains installation related macros/functions
# @author Raffi Enficiaud

if(UNIX AND NOT APPLE)
  include(GNUInstallDirs)
endif()


set(YAYI_HEADER_INSTALLATION_RELATIVE_PATH          "include/yayi" CACHE STRING "Header installation directory")
set(YAYI_LIBRARIES_INSTALLATION_RELATIVE_PATH       "lib"          CACHE STRING "shared libraries installation directory")
set(YAYI_DOCUMENTATION_INSTALLATION_RELATIVE_PATH   "documentation" CACHE STRING "documentation installation directory")

function(set_installation_paths)

  if(UNIX AND NOT APPLE)
    message("[YAYI][install] Fixing the installation directories for Unix")
    set(YAYI_HEADER_INSTALLATION_RELATIVE_PATH ${CMAKE_INSTALL_INCLUDEDIR}/yayi CACHE STRING "Header installation directory" FORCE)
    set(YAYI_LIBRARIES_INSTALLATION_RELATIVE_PATH ${CMAKE_INSTALL_LIBDIR} CACHE STRING "Shared libraries installation directory" FORCE)
    set(YAYI_DOCUMENTATION_INSTALLATION_RELATIVE_PATH ${CMAKE_INSTALL_DOCDIR} CACHE STRING "documentation installation directory" FORCE)
  endif()

endfunction()


function(install_lib_and_dll file_names path_to_install component)
  foreach(loop_var ${file_names})
    get_filename_component(filepathabs ${loop_var} ABSOLUTE)
    get_filename_component(filepath ${filepathabs} PATH)
    get_filename_component(filename ${filepathabs} NAME_WE)
    set(file_to_install ${filepath}/${filename}${CMAKE_SHARED_LIBRARY_SUFFIX})
    if(NOT EXISTS ${file_to_install})
      message("[YAYI][install] file ${file_to_install} does not EXISTS !!!")
    endif()
    message("[YAYI][install] Installing ${file_to_install} to ${path_to_install}")
    install(FILES ${file_to_install} DESTINATION ${path_to_install} COMPONENT ${component})  
  endforeach()
endfunction(install_lib_and_dll)

function(install_realpath_with_rename file_names path_to_install component configuration)
  foreach(loop_var ${file_names})
    get_filename_component(filepathreal ${loop_var} REALPATH)
    get_filename_component(filename ${loop_var} NAME)
  
    if(NOT EXISTS ${filepathreal})
      message("file ${filepathreal} does not EXISTS !!!")
    endif()
    message("Installing ${loop_var} (${filepathreal}) to ${path_to_install} with name ${filename}")
    install(FILES ${loop_var} CONFIGURATIONS ${configuration} DESTINATION ${path_to_install} COMPONENT ${component} RENAME ${filename})  
  endforeach()
endfunction(install_realpath_with_rename)




#
# This function creates installation rule for yayi targets. The installation performs some
# configuration/actions, such as installing the headers along the produced shared libraries,
# configuring the relocation of the .so/.dylib, etc.
# The files installed with this function go to the "core" component. 
#
# install_yayi_targets(TARGET target_name HEADER_FILES files CONFIGURATION configuration COMPONENT component)
function(install_yayi_targets)

  set(options )
  set(oneValueArgs CONFIGURATION TARGET COMPONENT)
  set(multiValueArgs HEADER_FILES)
  cmake_parse_arguments(my_install "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})

  if("${my_install_COMPONENT}" STREQUAL "")
    set(component core)
  else()
    set(component ${my_install_COMPONENT})
  endif()

  message(STATUS "installing ${my_install_TARGET} into component ${component}")

  # installing the given targets
  if(my_install_TARGET)
    install(TARGETS ${my_install_TARGET}
            DESTINATION ${YAYI_LIBRARIES_INSTALLATION_RELATIVE_PATH}
            COMPONENT ${component}
            CONFIGURATIONS ${my_install_CONFIGURATION})
    
    
    # trying relocatable targets, works, except for the problem on boost 
    # on apple, the name of the so should be changed with the install_name_tool
    # with options -change to change the name of the dependency, and -id to change
    # the name of the shared object itself.
    if(APPLE)
      #set_target_properties(${my_install_TARGET} PROPERTIES INSTALL_NAME_DIR "@loader_path")
    elseif(UNIX)
      #set_target_properties(${my_install_TARGET}
      #  PROPERTIES
      #    INSTALL_RPATH "$ORIGIN/."
      #    BUILD_WITH_INSTALL_RPATH TRUE)
    endif()
  endif()


  # installing the header files
  get_filename_component(yayiabs ${YAYI_root_dir} ABSOLUTE)
  
  foreach(loop_var ${my_install_HEADER_FILES})
    get_filename_component(filepathabs ${loop_var} ABSOLUTE)
    get_filename_component(filepath ${filepathabs} PATH)
    file(RELATIVE_PATH relative_p "${yayiabs}" "${filepath}")
    
    get_filename_component(extensiont ${loop_var} EXT)
    string(TOLOWER "${extensiont}" extension)
    
    if("${extension}" STREQUAL ".hpp" OR "${extension}" STREQUAL ".h")
      install(FILES ${loop_var} 
              DESTINATION ${YAYI_HEADER_INSTALLATION_RELATIVE_PATH}/${relative_p}
              COMPONENT ${component}-dev
              CONFIGURATIONS ${my_install_CONFIGURATION}) 
    endif()
  endforeach()
  
endfunction(install_yayi_targets)
