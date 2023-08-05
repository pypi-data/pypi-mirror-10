#ifndef PYTHONIC_TYPES_HOLLOW_NDARRAY_HPP
#define PYTHONIC_TYPES_HOLLOW_NDARRAY_HPP

#include "pythonic/types/ndarray.hpp"

namespace pythonic {

namespace types {

  /* a shape without element, used for generating functions like numpy.random.random() */
template<class T, size_t N>
  struct hollow_ndarray : ndarray<T, N> {
    hollow_ndarray() = default;
    hollow_ndarray(hollow_ndarray const&) = default;
    hollow_ndarray(hollow_ndarray &&) = default;
    hollow_ndarray& operator=(hollow_ndarray const&) = default;

    hollow_ndarray(array<long, N> const& shape) : ndarray<T,N>(shape, utils::no_memory()) {}
  };

}

}

#endif
