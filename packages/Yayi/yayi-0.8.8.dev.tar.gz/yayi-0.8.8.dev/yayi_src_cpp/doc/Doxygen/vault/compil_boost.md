Compiling Boost {#compil_boost}
===============
[TOC]

This is somewhat out of the scope of such as documentation, but since Boost is one of the main dependency and we do not want you to be stuck,
we detail the steps in order to make Boost running in your platform.

How to compile Boost 
====================

The compilation of Boost might be a bit tricky, and people are often afraid of it. However, the compilation in itself is not particularly hard. 
The thing usually disturbing developers seems to be the dedicated cross-platform build system of Boost. 
In the facts, compiling Boost reduces merely to 2 lines in bash, as explained below. 


Linux/MacOSX     {#compil_boost_linmac}
------------

~~~~~~~~~~~~~~~~~~~~~~~~{.sh}
$> ./bootstrap.sh
$> ./bjam --prefix=your_install_prefix_directory --ignore-config install
~~~~~~~~~~~~~~~~~~~~~~~~

The `--ignore-config` option is to avoid any troubleshooting between your freshly untared version of boost, and a possibly preinstalled version of boost in your system. 

### Compilation of universal binaries on MacOSX {#compil_boost_linmac_universallib}

If you would like to generate universal binaries for MacOSX (same binaries containing both the x86 and x64 versions), you must add the following options to bjam:
~~~~~~~~~~~~~~~~~~~~~~~~{.sh}
$> ./b2 --prefix=your_install_prefix_directory address-model=32_64 architecture=x86 --ignore-config install
~~~~~~~~~~~~~~~~~~~~~~~~

Note that since v0.08, Yayi by default compiles as universal binaries. If boost was not compiled as universal binaries, you may encounter link issues.


- Remarks on MacOSX:
This was the theory. Now the practice: building under MacOSX can be a perfect pain. The problems are the following:
  - curiously, the @b ~ is not developed for your prefix installation (hence `--prefix=~/usr/local` will not properly go to your 
    `$HOME/usr/local` but into a subdirectory of your current directory). You must provide the full installation prefix.
  - the compiler shipped by Apple and targeted as being the default on new versions of OSX, namely @b llvm, does not seem to be perfectly compatible with boost. 
  - the version of python shipped by Apple does not seem to be compatible with packages that are interesting for us (namely @b numpy). 


The second point may make you willing to install the official version of Python. This can easily be done by downloading the installation package 
from the official Python web page, and double click on it. You should however ensure during your build steps that this is precisely the version used for 
compilation, including boost. You may check the version of Python with the following command:

~~~~~~~~~~~~~~~~~~~~~~~~{.sh}
$> ./b2 -q  --prefix=your_install_prefix_directory --debug-configuration install
~~~~~~~~~~~~~~~~~~~~~~~~

which flushes in the terminal the complete version of Python, its headers and library location, and also the compiler chosen by the boost toolchain. 

If you have installed the "official" Python, I strongly encourage you to read @ref install_python "this page". 


~~~~~~~~~~~~~~~~~~~~~~~~{.sh}
$> ./b2  -j 6 -q --prefix=our_prefix_install macosx-version=10.6 toolset=darwin architecture=x86 target-os=darwin address-model=32_64 install
~~~~~~~~~~~~~~~~~~~~~~~~

Windows {#compil_boost_windows}
-------

~~~~~~~~~~~~~~~~~~~~~~~~{.sh}
$> bootstrap.bat
$> bjam --prefix=your_install_prefix_directory --build-type=complete --layout=versioned --ignore-config install
~~~~~~~~~~~~~~~~~~~~~~~~

However, the compilation takes time, and some parts (though not needed for Yayi) are easily missed. 


Remarks for all platforms {#boostremarks_allplatforms}
-------------------------

Using the following option:
~~~~~~~~~~~~~~~~~~~~~~~~{.sh}
$> b2 -q [...]
~~~~~~~~~~~~~~~~~~~~~~~~
will stop the build at first encountered error. 

The option
~~~~~~~~~~~~~~~~~~~~~~~~{.sh}
$> b2 -j XX [...]
~~~~~~~~~~~~~~~~~~~~~~~~
will use XX processes for the build (significantly faster). 
