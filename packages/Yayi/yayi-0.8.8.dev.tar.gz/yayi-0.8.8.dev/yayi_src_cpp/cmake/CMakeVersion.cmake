# @file
# This file contains macro for generating a header file containing the current version
# of the sources the library is compiled against

# @author Raffi Enficiaud



function(get_git_revisions GIT_REV GIT_DATE GIT_BRANCH)

  find_package(Git)
  if(NOT ${GIT_FOUND})
    message(WARNING "[GIT] Git not found")
    set(${GIT_REV} "none" PARENT_SCOPE)
    set(${GIT_DATE} "none" PARENT_SCOPE)
    set(${GIT_BRANCH} "none" PARENT_SCOPE)
    return()
  endif()

  # from http://stackoverflow.com/questions/1435953/how-can-i-pass-git-sha1-to-compiler-as-definition-using-cmake
  execute_process(COMMAND
    "${GIT_EXECUTABLE}" describe --match=NeVeRmAtCh --always --abbrev=40 --dirty
    WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}"
    OUTPUT_VARIABLE _GIT_REV
    RESULT_VARIABLE GIT_CMD_RESULT
    ERROR_VARIABLE GIT_CMD_ERROR
    #ERROR_QUIET
    OUTPUT_STRIP_TRAILING_WHITESPACE)

  if(NOT (${GIT_CMD_RESULT} EQUAL 0))
    message(STATUS "[GIT] command error: maybe not a git repository: ${GIT_CMD_RESULT} / ${GIT_CMD_ERROR}")
    set(${GIT_REV} "none" PARENT_SCOPE)
    set(${GIT_BRANCH} "none" PARENT_SCOPE)
    set(${GIT_DATE} "none" PARENT_SCOPE)
  else()
    set(${GIT_REV} ${_GIT_REV} PARENT_SCOPE)

    # the date of the commit
    execute_process(COMMAND
      "${GIT_EXECUTABLE}" log -1 --format=%ai --date=local
      WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}"
      OUTPUT_VARIABLE _GIT_DATE
      ERROR_QUIET OUTPUT_STRIP_TRAILING_WHITESPACE)
    set(${GIT_DATE} ${_GIT_DATE} PARENT_SCOPE)

    # get the name of the branch, if any
    # from http://stackoverflow.com/questions/6245570/how-to-get-current-branch-name-in-git
    execute_process(COMMAND
      "${GIT_EXECUTABLE}" symbolic-ref -q --short HEAD
      WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}"
      OUTPUT_VARIABLE _GIT_BRANCH
      ERROR_QUIET
      OUTPUT_STRIP_TRAILING_WHITESPACE)

    set(${GIT_BRANCH} ${_GIT_BRANCH} PARENT_SCOPE)
  endif()


endfunction(get_git_revisions)



# Old Subversion commands, might be reused.
#if(EXISTS ${YAYI_root_dir}/.svn)
#  find_package(Subversion)
#  if(Subversion_FOUND)
#    Subversion_WC_INFO(${YAYI_CORE_DIR} YayiCoreSVN)
#  else()
#    message(WARNING "Subversion not found")
#    set(YayiCoreSVN_WC_REVISION "XXX" CACHE STRING "Yayi SVN version")
#  endif(Subversion_FOUND)
#else()
#  message(WARNING "no .svn")
#  set(YayiCoreSVN_WC_REVISION "XXX" CACHE STRING "Yayi SVN version")
#endif()




macro(generate_library_version template_file_name filename_to_generate)

  set(_should_generate FALSE)
  set(_is_archive FALSE)

  if(NOT "${EXTERNAL_REVISION}" STREQUAL "")
    set(_current_rev ${EXTERNAL_REVISION})
    set(_current_date "not available")
    set(_current_branch "master")
    set(_should_generate TRUE)
  else()


    set(_current_rev)
    set(_current_date)
    set(_current_branch)
    get_git_revisions(_current_rev _current_date _current_branch)
    if(${_current_rev} STREQUAL "none")
      message(STATUS "[REVISION] looks like a tarball")
      set(_is_archive TRUE)
      if(NOT EXISTS ${filename_to_generate})
        set(_current_rev "archive")
        set(_current_date "archive")
        set(_should_generate TRUE)
        message(FATAL_ERROR "[REVISION] Cannot determine the version of the current code. The file ${filename_to_generate} is missing.")
      else()
        message(STATUS "[REVISION] file ${filename_to_generate} already contains the version")
      endif()
    endif()
  endif()

  # this looks to be working well: we concatenate the name of the file to generate to the string
  # _yayi_previous_revision, and this gives us the variable name for this specific file
  # If we use only one variable name (non dependent on the filename to generate) then the second
  # call to the macro does not generate the second file
  set(_yayi_previous_revision_file _yayi_previous_revision${filename_to_generate})

  if(NOT ${_is_archive})
    if(DEFINED ${_yayi_previous_revision_file})
      if(NOT (${${_yayi_previous_revision_file}} STREQUAL ${_current_rev}) OR (NOT EXISTS ${filename_to_generate}))
        set(_should_generate TRUE)
      endif()
    else()
      set(_should_generate TRUE)
    endif()
  endif()

  if(_should_generate)
    set(${_yayi_previous_revision_file} ${_current_rev} CACHE INTERNAL "internal revision to avoid repeated rebuild for file ${filename_to_generate}" FORCE)

    set(yayi_version      ${YAYI_VERSION})
    if(NOT _current_branch STREQUAL master)
      set(yayi_version ${yayi_version}.dev)
    endif()
    set(revision_version  ${_current_rev})
    set(revision_date     ${_current_date})

    message(STATUS "[REVISION] Yayi version ${yayi_version}, revision ${_current_rev}, branch ${_current_branch}, commited at ${_current_date} flushed into file ${filename_to_generate}")
    configure_file(${template_file_name} ${filename_to_generate})
    set_source_files_properties(${filename_to_generate} PROPERTIES GENERATED TRUE)
    unset(revision_version)
    unset(revision_date)

  endif()

  unset(_should_generate)
  unset(_is_archive)
  unset(_current_rev)
  unset(_current_date)

endmacro(generate_library_version)


