#ifndef YAYI_LABEL_EXTREMA_HPP__
#define YAYI_LABEL_EXTREMA_HPP__


#include <yayiLabel/yayi_Label.hpp>


namespace yayi
{
  namespace label
  {
    /*!@defgroup label_extrema_grp Labelling extrema
     * @ingroup label_grp
     * @{
     */
     
     
    //! Connected minima plateaus with a single "id" per minimum in the output image
    YLab_ yaRC image_label_minimas(const IImage* imin, const se::IStructuringElement* se, IImage* imout);

    //! Connected maximas plateaus with a single "id" per maximas in the output image
    YLab_ yaRC image_label_maximas(const IImage* imin, const se::IStructuringElement* se, IImage* imout);

    //! @} 
  }
}

#endif /* YAYI_LABEL_EXTREMA_HPP__ */ 
