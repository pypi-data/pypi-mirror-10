#ifndef YAYI_MORPHOLOGICAL_DISTANCES_HPP__
#define YAYI_MORPHOLOGICAL_DISTANCES_HPP__

/*!@file
 * This file defines the classical morphological distances. The implementation is based
 * on the simple queue propagation
 * @author Raffi Enficiaud
 */


#include <yayiDistances/yayiDistances.hpp>
#include <yayiImageCore/include/yayiImageCore.hpp>
#include <yayiStructuringElement/yayiStructuringElement.hpp>

namespace yayi
{
  namespace distances
  {
    /*!@defgroup morphologicaldistance_grp Morphological distances
     * @ingroup distances_grp
     * @{
     */


    /*!@brief Morphological/city-block distance transform.
     *
     * This function computes the morphological distance from a binary pattern in the input image. This transformation is
     * also known as grid/city block distance transform, depending on the underlying structuring element. The underlying algorithm 
     * is due to Luc Vincent in @cite vincent:1990, which can work in any dimension.
     *
     * @note the city block distance computed depends on the structuring element given as parameter. For cross-shaped structuring 
     * element (@ref yayi::se::SECross2D) the @f$\ell_1@f$ distance, or City Block, is computed, while for box-shaped structuring element (see eg. 
     * @ref yayi::se::SESquare2D) the @f$\ell_{+\infty}@f$ distance is computed.
     *
     * @author Raffi Enficiaud
     */
    YDist_ yaRC DistanceFromSetsBoundary(
      const IImage* input, 
      const se::IStructuringElement* se, 
      IImage* output_distance);


    /*!@brief Morphological geodesic distance on input image (from sets boundary).
     *
     * Roughly the same as @ref DistanceFromSetsBoundary, but the distance is computed in a geodesic manner inside the image mask.
     *
     * @author Raffi Enficiaud
     */
    YDist_ yaRC GeodesicDistanceFromSetsBoundary(
      const IImage* input, 
      const IImage* mask, 
      const se::IStructuringElement* se, 
      IImage* output_distance);

    //! @} //morphologicaldistance_grp

  }

}

#endif /* YAYI_MORPHOLOGICAL_DISTANCES_HPP__ */
