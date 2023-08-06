Build environment setup {#build_setup}
=======================
[TOC]

Build environment setup
=======================


Compilation tools {#build_tools}
-----------------

We advocate the use of free software, and building and using Yayi does not require any commercial software or any restrictive licence. Here are some excerpts from our
experience:
- Unix: Under Unices (Linux, Unix, etc.) there is a great number of free software that can be used for compiling and editing source code. 
- Mac OSX: XCode is free but downloading it requires a registration on the Apple Web site. 
- Windows: Under Windows, things are a bit more complicated. A free version of a great C++ compiler is shipped with Visual C++ Express Edition, 
which requires a (free) registration before using it. We recommend using version 10 or above. If you want to use the x64 compilation for Visual 10, 
you should first install the SP1 of Visual (unless already shipped) and also the Plateform SDK, which provides among many things the x64 C++ compiler. 

Build system {#build_build}
------------

Yayi uses [CMake](http://www.cmake.org) as the main build system. It currently depends on the version 2.8. 
CMake is a free and multi-platform meta-build engine. It proposes a language for defining the components of a project, their dependencies, their link, 
installation options, etc. in a cross-platform manner. It is able to generate makefiles, Visual C++/Studio or XCode projects directly, with no change 
in the build script.

CMake on Unix/Mac OSX {#build_cmake_unix}
---------------------

Usually, installing CMake on Unix/Mac OSX declares also the CMake binary in the `$PATH`. 
Hence, simply by typing 

  cmake --version

you should see something like "cmake version 2.8.XX". 

CMake on Windows {#build_cmake_win}
----------------

CMake on Windows is shipped with a nice front-end allowing you to properly configure the different options of the project before it is built. 

On Windows, CMake is able to generate Visual Studio/C++ solutions. Visual automatically uses several cores for building the solution. 
If you are familiar with Unix/Mac, or if you like your small Windows shell very much, you certainly would like to work on makefiles, that then can be 
built using the Microsoft flavour of make: NMake. However, one big inconvenient in using NMake is that it is not multi-threaded, and the builds 
can be much longer than in Visual. 

On way to have the advantages of using a shell and the Visual building engine is by using the MSbuild building engine, that comes with Microsoft .NET 
(preferably 4 or above). See @ref sub_msbuild_build for more details.

Python {#build_third_python}
------

Yayi exports all functions and relevant objects into the Python language, which means that you can manipulate images from Python, 
export measurements on image into Python native objects, etc. 

For specific topic concerning the x64 vs. x86 debate, please consider reading @ref sec_x86x64. 
