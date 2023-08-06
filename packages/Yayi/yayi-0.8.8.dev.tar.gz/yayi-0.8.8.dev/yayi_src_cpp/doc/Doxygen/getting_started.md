Tutorial {#start}
========
[TOC]



Getting started with Images {#images}
===========================


Creating an image
-----------------

Images are implemented in a template structure @c yayi::Image. The parameters of this template indicate the type of the pixels 
and the coordinate system of their pixels:

Template images can be 
- of any pixel type: there is no default type so this parameter should always be specified
- in any coordinate system, by default the pixels lie in a 2D space.

Once an image is defined, its size should be specified and it should be allocated. 

Most of the operations in Yayi return an error code, @c yayi::yaRC that allows you to check if the call went well. An example of
image definition and allocation is given below:

~~~~~~~~~~~~~~~~~~~~~~
#include <yayi/core/yayiImageCore/include/yayiImageCore_Impl.hpp>

void create_image() 
{
  // 2D image of unsigned short
  yayi::Image< yayi::yaUINT16 > im2D_ui16;

  // Sets the size of the image to be 20 pixels in _x_ and 30 pixels in _y_
  yaRC res = im2D_ui16.SetSize(c2D(20, 30));

  // check the size settings
  if(res != yayi::yaRC_ok)
  {
    std::cerr << "Error in the size settings " << res << std::endl;
    return;
  }
  
  // Allocates the pixel buffer
  res = im2D_ui16.Allocate();
  if(res != yayi::yaRC_ok)
  {
    std::cerr << "Error in the allocation " << res << std::endl;
    return;
  }

  // ... do some processing 

  // the buffer is freed when im2D_ui16 gets out of the scope.
}
~~~~~~~~~~~~~~~~~~~~~~  



Generic interface layer
-----------------------
The template layer is very nice for a fully C++ framework. However Yayi creates precompiled libraries as well to plug with other frameworks, such as Python.
These frameworks do not understand the templates. To bind with those, it is then necessary to have a layer on the top of the templates that has a fixed definition
(no compilation time definitions such as for templates). 

This is the purpose of the so called _generic interface layer_, from which all @c yayi::Image derive. It is implemented in a virtual base class @c yayi::IImage . 

~~~~~~~~~~~~~~~~~~~~~~
#include <yayi/core/yayiImageCore/include/yayiImageCore_Impl.hpp>

void generic_layer() 
{
  // 2D image of unsigned short
  yayi::Image< yayi::yaUINT16 > im2D_ui16;

  // ... allocate the image

  yayi::IImage *image_interface = &im2D_ui16;
}
~~~~~~~~~~~~~~~~~~~~~~

### Variants
Variants are a way to abstract the types managed by the template to the interface layer. Variants are objects that may contain almost everything.



Accessing and modifying the images {#modifying}
==================================
Images in Yayi expose an iterator interface. 




Reading and writing images {#read_write}
==========================
Now we will read and write images to disk.



Structuring elements {#structuring_elements}
====================
Structuring element are a concept from the Mathematical Morphology field. 



