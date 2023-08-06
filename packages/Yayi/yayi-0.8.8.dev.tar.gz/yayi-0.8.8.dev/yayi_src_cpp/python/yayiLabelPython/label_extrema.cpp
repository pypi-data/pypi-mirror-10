
#include <yayiLabelPython/label_python.hpp>
#include <yayiLabel/yayi_label_extrema.hpp>
using namespace yayi::label;

void declare_label_extrema() {
  bpy::def("image_label_minimas", 
           &image_label_minimas, 
           "(imin, se, imout) : labels minimum plateaus of imin into imout with a single id per connected component");

  bpy::def("image_label_maximas", 
           &image_label_maximas, 
           "(imin, se, imout) : labels maximum plateaus of imin into imout with a single id per connected component");
}
