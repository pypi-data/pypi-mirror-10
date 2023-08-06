#include "main.hpp"
#include <yayiCommon/common_histogram.hpp>
#include <yayiCommon/common_variant.hpp>

BOOST_AUTO_TEST_SUITE(histograms)

BOOST_AUTO_TEST_CASE(histogram_8bits)
{
  using namespace yayi;
  typedef s_histogram_t<yaUINT8, yaUINT16> histogram_type;
  typedef s_histogram_t<yaUINT16, yaUINT16> histogram16_type;

  histogram_type hist;
  BOOST_CHECK_EQUAL(hist.max_bin(), 0);
  BOOST_CHECK_EQUAL(hist.min_bin(), 255);

  hist[255]++;

  BOOST_CHECK_EQUAL(hist.max_bin(), 255);
  BOOST_CHECK_EQUAL(hist.min_bin(), 255);
  BOOST_CHECK_EQUAL(hist.sum(), 1);

  hist[128]++;
  BOOST_CHECK_EQUAL(hist.max_bin(), 255);
  BOOST_CHECK_EQUAL(hist.min_bin(), 128);
  BOOST_CHECK_EQUAL(hist.sum(), 2);

  histogram16_type hist16;
  BOOST_CHECK_EQUAL(hist16.max_bin(), 0);
  BOOST_CHECK_EQUAL(hist16.min_bin(), (1<<16)-1);

  hist16[255]++;
  BOOST_CHECK_EQUAL(hist16.max_bin(), 255);
  BOOST_CHECK_EQUAL(hist16.min_bin(), 255);
  BOOST_CHECK_EQUAL(hist16.sum(), 1);

  hist16[((1<<16)-1)]++;
  BOOST_CHECK_EQUAL(hist16.max_bin(), std::numeric_limits<yaUINT16>::max());
  BOOST_CHECK_EQUAL(hist16.min_bin(), 255);
  BOOST_CHECK_EQUAL(hist16.sum(), 2);
}

BOOST_AUTO_TEST_CASE(histogram_8bits_to_variant)
{
  using namespace yayi;
  typedef s_histogram_t<yaUINT8, yaUINT16> histogram_type;

  histogram_type hist;
  BOOST_CHECK_EQUAL(hist.max_bin(), 0);
  BOOST_CHECK_EQUAL(hist.min_bin(), 255);

  hist[255]++;

  BOOST_CHECK_EQUAL(hist.max_bin(), 255);
  BOOST_CHECK_EQUAL(hist.min_bin(), 255);

  yayi::variant v = hist;
  std::vector<std::pair<yaUINT8, yaUINT16> > vv = v;
  BOOST_REQUIRE_EQUAL(vv.size(), 1);
  BOOST_CHECK_EQUAL(vv[0].first, 255);
}

BOOST_AUTO_TEST_CASE(histogram_16bits_to_variant)
{
  using namespace yayi;
  typedef s_histogram_t<yaUINT16, yaUINT16> histogram_type;

  histogram_type hist;
  BOOST_CHECK_EQUAL(hist.max_bin(), 0);
  BOOST_CHECK_EQUAL(hist.min_bin(), std::numeric_limits<yaUINT16>::max());

  hist[255]++;

  BOOST_CHECK_EQUAL(hist.max_bin(), 255);
  BOOST_CHECK_EQUAL(hist.min_bin(), 255);

  yayi::variant v = hist;
  std::vector<std::pair<yaUINT8, yaUINT16> > vv = v;
  BOOST_REQUIRE_EQUAL(vv.size(), 1);
  BOOST_CHECK_EQUAL(vv[0].first, 255);
}

BOOST_AUTO_TEST_CASE(histogram_clear_bug)
{
  using namespace yayi;
  typedef s_histogram_t<yaUINT16, yaUINT16> histogram_type;

  histogram_type hist;
  BOOST_CHECK_NO_THROW(hist.clear());

  typedef s_histogram_t<yaUINT8, yaUINT16> histogram_type2;
  histogram_type2 hist2;
  BOOST_CHECK_NO_THROW(hist2.clear());
}

BOOST_AUTO_TEST_SUITE_END()
