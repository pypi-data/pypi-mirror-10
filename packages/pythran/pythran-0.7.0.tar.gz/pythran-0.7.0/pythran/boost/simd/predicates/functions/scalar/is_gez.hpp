//==============================================================================
//         Copyright 2003 - 2011 LASMEA UMR 6602 CNRS/Univ. Clermont II
//         Copyright 2009 - 2011 LRI    UMR 8623 CNRS/Univ Paris Sud XI
//
//          Distributed under the Boost Software License, Version 1.0.
//                 See accompanying file LICENSE.txt or copy at
//                     http://www.boost.org/LICENSE_1_0.txt
//==============================================================================
#ifndef BOOST_SIMD_PREDICATES_FUNCTIONS_SCALAR_IS_GEZ_HPP_INCLUDED
#define BOOST_SIMD_PREDICATES_FUNCTIONS_SCALAR_IS_GEZ_HPP_INCLUDED
#include <boost/simd/predicates/functions/is_gez.hpp>
#include <boost/simd/include/constants/zero.hpp>
#include <boost/simd/include/constants/true.hpp>
#include <boost/simd/sdk/meta/as_logical.hpp>

namespace boost { namespace simd { namespace ext
{
  BOOST_SIMD_FUNCTOR_IMPLEMENTATION( boost::simd::tag::is_gez_, tag::cpu_
                            , (A0)
                            , (scalar_< fundamental_<A0> >)
                            )
  {
    typedef typename meta::as_logical<A0>::type result_type;
    BOOST_SIMD_FUNCTOR_CALL(1)
    {
      return result_type(a0 >= Zero<A0>());
    }
  };

  BOOST_SIMD_FUNCTOR_IMPLEMENTATION( boost::simd::tag::is_gez_, tag::cpu_
                            , (A0)
                            , (scalar_< unsigned_<A0> >)
                            )
  {
    typedef typename meta::as_logical<A0>::type result_type;
    inline result_type operator()(A0 const&)const
    {
      return boost::simd::True<result_type>();
    }
  };
} } }


#endif
