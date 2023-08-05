//==============================================================================
//         Copyright 2003 - 2012   LASMEA UMR 6602 CNRS/Univ. Clermont II
//         Copyright 2009 - 2012   LRI    UMR 8623 CNRS/Univ Paris Sud XI
//
//          Distributed under the Boost Software License, Version 1.0.
//                 See accompanying file LICENSE.txt or copy at
//                     http://www.boost.org/LICENSE_1_0.txt
//==============================================================================
#ifndef BOOST_SIMD_SDK_SIMD_META_HAS_EXTENSION_HPP_INCLUDED
#define BOOST_SIMD_SDK_SIMD_META_HAS_EXTENSION_HPP_INCLUDED

#include <boost/simd/sdk/simd/meta/extension_of.hpp>
#include <boost/type_traits/is_same.hpp>

namespace boost { namespace simd { namespace meta
{
  template<typename A0, typename X>
  struct  has_extension
        : is_same<typename meta::extension_of<A0>::type, X>
  {};
} } }

#endif
