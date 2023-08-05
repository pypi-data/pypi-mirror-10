//==============================================================================
//         Copyright 2003 - 2012   LASMEA UMR 6602 CNRS/Univ. Clermont II
//         Copyright 2009 - 2012   LRI    UMR 8623 CNRS/Univ Paris Sud XI
//
//          Distributed under the Boost Software License, Version 1.0.
//                 See accompanying file LICENSE.txt or copy at
//                     http://www.boost.org/LICENSE_1_0.txt
//==============================================================================
#ifndef BOOST_SIMD_PREDICATES_FUNCTIONS_IS_ORD_HPP_INCLUDED
#define BOOST_SIMD_PREDICATES_FUNCTIONS_IS_ORD_HPP_INCLUDED
#include <boost/simd/include/functor.hpp>
#include <boost/dispatch/include/functor.hpp>


namespace boost { namespace simd { namespace tag
  {
   /*!
     @brief is_ord generic tag

     Represents the is_ord function in generic contexts.

     @par Models:
        Hierarchy
   **/
    struct is_ord_ : ext::elementwise_<is_ord_>
    {
      /// @brief Parent hierarchy
      typedef ext::elementwise_<is_ord_> parent;
    };}
  /*!
    Returns True if neither a0 nor a1 is nan.

    @par Semantic:

    @code
    logical<T> r = is_ord(a0,a1);
    @endcode

    is similar to:

    @code
    logical<T> r = (a0 == a0) && (a1 == a1);
    @endcode

    @param a0

    @param a1

    @return a logical value
  **/
  BOOST_DISPATCH_FUNCTION_IMPLEMENTATION(tag::is_ord_, is_ord, 2)
} }

#endif

