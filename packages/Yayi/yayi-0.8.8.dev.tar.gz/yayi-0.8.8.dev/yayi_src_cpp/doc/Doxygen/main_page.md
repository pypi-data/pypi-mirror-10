My Main Page {#mainpage}
============

[TOC]

What is Yayi?
-------------

**Yayi** is a open-source image processing framework, mostly written in (not so more) advanced C++03 and with Python bindings. It is released under the very
permissive Boost license. 

Yayi offers a great flexibility mainly using templatized code and metaprogramming, which enables a high level of genericity. It implements some of the main concepts
of Mathematical Morphology into an efficient and proven design. 
    
Yayi aims at providing robust, efficient and flexible algorithms for image analysis, but also reference algorithms for Mathematical Morphology.
    
The Home Page of the Yayi can be found at: http://raffi.enficiaud.free.fr/.

 
Licence
-------

Yayi is distributed under the Boost licence, and the official licence as well as the possibility offered by the licence can be found 
[here](http://www.boost.org/users/license.html).

Download
--------

* The code is freely available from the Bitbucket repository located here: https://bitbucket.org/renficiaud/yayi. 
* Python source and binary packages can be downloaded as well from the Pypi repository located here: https://pypi.python.org/pypi/Yayi


Major functionalities
---------------------

- Multidimensional and multispectral image processing and morphology structures (coordinates and pixels are templatized over their type respectively)
- Algorithms are written in a multidimensional and multispectral fashion (orders are parameters)
- Classical useful structures are included: 
  - graphs, 
  - trees, 
  - histograms, ...
- Several types of structuring elements (SE) are provided: 
  - compile-time SE, 
  - runtime SE, 
  - functional SE, ...
- Yayi includes a dispatching mechanism for creating compiled libraries over a large combinations of the templates input types


Where to go from here?
----------------------

- If you want to start using Yayi, or explore its functionality, have a look at @subpage start "this page". 
  Most of the commands in the C++ layer also apply to the Python bindings as well. 
- The advanced topics are described in @subpage advanced "this page"
- For installation instructions, have a look at @subpage install "this page"
- Finally, if you want to contribute, don't miss the @subpage devel "development guidelines"

