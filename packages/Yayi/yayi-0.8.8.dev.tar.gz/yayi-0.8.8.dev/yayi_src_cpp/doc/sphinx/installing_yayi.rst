Installing Yayi
***************

.. toctree::
   :maxdepth: 1


Yayi supports the PIP installation procedure. However its compilation requires some dependencies to be available on 
your system. Those dependencies are:

* cmake
* boost


Windows
-------
Binary packages are already provided for Windows. If you are lucky, then there is no need for compilation and 
just a double click on the installer should do.

Mac OSX
-------
Binary packages are already provided for OSX. If you are lucky, then there is no need for recompilation, and the installation
is lightning fast, just type:

..  code-block:: bash
	:linenos:

    pip install yayi

Manuall installation
^^^^^^^^^^^^^^^^^^^^
If you are less lucky, then you need to install `boost` and `cmake` and then compile Yayi. The easiest way is to install first 
`brew` and then to tell `brew` to install all those things for you. Then 

..  code-block:: bash
	:linenos:

    pip install yayi

should also work.

Boost location and other system dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
As mentioned, Yayi depends on Boost and cmake. `cmake` should be in the path, while `boost` should be accessible during the 
compilation. 
In some circumstances, it is possible to specify the location of `boost`, if you do not want to have a dependency lying on the system
for a python package (different package managers might break the dependency chain). 

.. code-block:: bash

    python setup.py build_cmake --boostroot=/my_boost/installation/location/boost_1_55/ install

On OSX, a particular care has been taken to make everything relocatable. So the previous command can be run inside a virtual environment
without any problem and without setting an `DYLD_LIBRARY_PATH`.

Linux
-----
Currently the distribution supports only compilation with system wide available dependencies.

    pip install --upgrade --install-option "build_cmake" --install-option "--boostroot=/my_boost/installation/location/boost_1_55/" yayi-0.8.6.dev0.tar.gz

On Linux, no relocation of the binaries is performed (yet, check if this would be something interesting to have). So the patch where
yayi is installed should be added to your `LD_LIBRARY_PATH` variable. You should not have this problem if you have `boost` on the system.

