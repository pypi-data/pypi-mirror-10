//==============================================================================
//         Copyright 2003 - 2011 LASMEA UMR 6602 CNRS/Univ. Clermont II
//         Copyright 2009 - 2011 LRI    UMR 8623 CNRS/Univ Paris Sud XI
//
//          Distributed under the Boost Software License, Version 1.0.
//                 See accompanying file LICENSE.txt or copy at
//                     http://www.boost.org/LICENSE_1_0.txt
//==============================================================================
#ifndef NT2_OPERATOR_FUNCTIONS_COMPLEX_GENERIC_IS_LESS_HPP_INCLUDED
#define NT2_OPERATOR_FUNCTIONS_COMPLEX_GENERIC_IS_LESS_HPP_INCLUDED
#include <nt2/operator/functions/is_less.hpp>
#include <nt2/include/functions/is_less.hpp>
#include <nt2/include/functions/logical_and.hpp>
#include <nt2/include/functions/is_real.hpp>
#include <nt2/include/functions/is_imag.hpp>
#include <nt2/include/functions/imag.hpp>
#include <nt2/include/functions/real.hpp>
#include <nt2/include/functions/is_gtz.hpp>
#include <nt2/include/functions/is_ltz.hpp>
#include <nt2/include/functions/is_less.hpp>
#include <nt2/sdk/complex/complex.hpp>
#include <nt2/include/constants/false.hpp>
#include <nt2/sdk/meta/as_logical.hpp>
#include <nt2/sdk/complex/meta/as_dry.hpp>
#include <nt2/sdk/complex/meta/as_real.hpp>

namespace nt2 { namespace ext
{
  // complex/complex
  NT2_FUNCTOR_IMPLEMENTATION( nt2::tag::is_less_, tag::cpu_, (A0)
                            , (generic_< complex_< arithmetic_<A0> > >)
                              (generic_< complex_< arithmetic_<A0> > >)
                            )
  {
    typedef typename  meta::as_real<A0>::type rA0;
    typedef typename meta::as_logical<rA0>::type result_type;
    NT2_FUNCTOR_CALL_REPEAT(2)
    {
      return is_less(nt2::real(a0),nt2::real(a1));
    }
  };
  // complex/complex
  NT2_FUNCTOR_IMPLEMENTATION( nt2::tag::is_less_, tag::cpu_, (A0)
                            , (generic_< dry_< arithmetic_<A0> > >)
                              (generic_< dry_< arithmetic_<A0> > >)
                            )
  {
    typedef typename  meta::as_real<A0>::type rA0;
    typedef typename meta::as_logical<rA0>::type result_type;
    NT2_FUNCTOR_CALL_REPEAT(2)
    {
      return is_less(nt2::real(a0),nt2::real(a1));
    }
  };
  // complex/arithmetic
  NT2_FUNCTOR_IMPLEMENTATION( nt2::tag::is_less_, tag::cpu_, (A0)(A1)
                            , (generic_< complex_< arithmetic_<A0> > >)
                              (generic_< arithmetic_<A1> >)
                            )
  {
    typedef typename  meta::as_real<A0>::type rA0;
    typedef typename meta::as_logical<rA0>::type result_type;
    NT2_FUNCTOR_CALL(2)
    {
      return is_less(nt2::real(a0), a1);
    }
  };
  // complex/dry
  NT2_FUNCTOR_IMPLEMENTATION( nt2::tag::is_less_, tag::cpu_, (A0)(A1)
                            , (generic_< complex_< arithmetic_<A0> > >)
                              (generic_< dry_ < arithmetic_<A1> > >)
                            )
  {
    typedef typename  meta::as_real<A0>::type rA0;
    typedef typename meta::as_logical<rA0>::type result_type;
    NT2_FUNCTOR_CALL(2)
    {
      return is_less(nt2::real(a0), nt2::real(a1));
    }
  };
  // arithmetic/complex
  NT2_FUNCTOR_IMPLEMENTATION( nt2::tag::is_less_, tag::cpu_, (A0)(A1),
                              (generic_< arithmetic_<A0> >)
                              (generic_< complex_< arithmetic_<A1> > >)
                            )
  {
    typedef typename  meta::as_real<A0>::type rA0;
    typedef typename meta::as_logical<rA0>::type result_type;
    NT2_FUNCTOR_CALL(2)
    {
      return is_less(nt2::real(a1),a0);
    }
  };
  // dry/complex
  NT2_FUNCTOR_IMPLEMENTATION( nt2::tag::is_less_, tag::cpu_, (A0)(A1),
                              (generic_< dry_ < arithmetic_<A0> > >)
                              (generic_< complex_< arithmetic_<A1> > >)
                            )
  {
    typedef typename  meta::as_real<A0>::type rA0;
    typedef typename meta::as_logical<rA0>::type result_type;
    NT2_FUNCTOR_CALL(2)
    {
      return is_less(nt2::real(a1),nt2::real(a0));
    }
  };

} }

#endif
