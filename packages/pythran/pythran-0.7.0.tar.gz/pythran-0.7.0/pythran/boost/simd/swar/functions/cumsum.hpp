//==============================================================================
//         Copyright 2003 - 2012   LASMEA UMR 6602 CNRS/Univ. Clermont II
//         Copyright 2009 - 2012   LRI    UMR 8623 CNRS/Univ Paris Sud XI
//
//          Distributed under the Boost Software License, Version 1.0.
//                 See accompanying file LICENSE.txt or copy at
//                     http://www.boost.org/LICENSE_1_0.txt
//==============================================================================
#ifndef BOOST_SIMD_SWAR_FUNCTIONS_CUMSUM_HPP_INCLUDED
#define BOOST_SIMD_SWAR_FUNCTIONS_CUMSUM_HPP_INCLUDED
#include <boost/simd/include/functor.hpp>
#include <boost/dispatch/include/functor.hpp>
#include <boost/simd/operator/functions/plus.hpp>
#include <boost/simd/constant/constants/zero.hpp>


namespace boost { namespace simd { namespace tag
  {
    /*!
      @brief cumsum generic tag

      Represents the cumsum function in generic contexts.

      @par Models:
      Hierarchy
    **/
    struct cumsum_ : ext::cumulative_<cumsum_, tag::plus_, tag::Zero>
    {
      /// @brief Parent hierarchy
      typedef ext::cumulative_<cumsum_, tag::plus_, tag::Zero> parent;
    };
  }
  /*!
    compute the cumulate sum of the vector elements

    @par Semantic:

    For every parameter of type T0

    @code
    T0 r = cumsum(a0);
    @endcode

    is similar to:

    @code
    T r =x;
    for(int i=0;i < T::static_size; ++i)
      r[i] += r[i-1];
    @endcode

    @param a0

    @return a value of the same type as the second parameter
  **/
  BOOST_DISPATCH_FUNCTION_IMPLEMENTATION(tag::cumsum_, cumsum, 1)
  BOOST_DISPATCH_FUNCTION_IMPLEMENTATION(tag::cumsum_, cumsum, 2)
} }

#endif
