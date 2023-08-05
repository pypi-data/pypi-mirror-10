//==============================================================================
//         Copyright 2003 - 2012   LASMEA UMR 6602 CNRS/Univ. Clermont II
//         Copyright 2009 - 2012   LRI    UMR 8623 CNRS/Univ Paris Sud XI
//
//          Distributed under the Boost Software License, Version 1.0.
//                 See accompanying file LICENSE.txt or copy at
//                     http://www.boost.org/LICENSE_1_0.txt
//==============================================================================
#ifndef NT2_REDUCTION_FUNCTIONS_CONTAINER_MINIMUM_HPP_INCLUDED
#define NT2_REDUCTION_FUNCTIONS_CONTAINER_MINIMUM_HPP_INCLUDED

#include <nt2/reduction/functions/minimum.hpp>
#include <nt2/core/container/dsl/reduction.hpp>
#include <boost/simd/reduction/functions/minimum.hpp>

#include <nt2/include/functions/min.hpp>
#include <nt2/include/constants/valmax.hpp>

namespace nt2 { namespace ext
{
  template<class Domain, class Expr>
  struct  size_of<boost::simd::tag::minimum_,Domain,1,Expr>
        : meta::reduction_size<Expr,1>
  {};

  template<class Domain, class Expr>
  struct  size_of<boost::simd::tag::minimum_,Domain,2,Expr>
        : meta::reduction_size<Expr,2>
  {};

  template<class Domain, int N, class Expr>
  struct  value_type<boost::simd::tag::minimum_,Domain,N,Expr>
        : meta::reduction_value<boost::simd::tag::minimum_,Expr>
  {};
} }

#endif
