//==============================================================================
//         Copyright 2003 - 2012   LASMEA UMR 6602 CNRS/Univ. Clermont II
//         Copyright 2009 - 2012   LRI    UMR 8623 CNRS/Univ Paris Sud XI
//
//          Distributed under the Boost Software License, Version 1.0.
//                 See accompanying file LICENSE.txt or copy at
//                     http://www.boost.org/LICENSE_1_0.txt
//==============================================================================
#ifndef NT2_HYPERBOLIC_FUNCTIONS_SINHC_HPP_INCLUDED
#define NT2_HYPERBOLIC_FUNCTIONS_SINHC_HPP_INCLUDED
#include <nt2/include/functor.hpp>


namespace nt2 { namespace tag
  {
   /*!
     @brief sinhc generic tag

     Represents the sinhc function in generic contexts.

     @par Models:
        Hierarchy
   **/
    struct sinhc_ : ext::elementwise_<sinhc_> { typedef ext::elementwise_<sinhc_> parent; };
  }
  /*!
    Returns hyperbolic cardinal sine: \f$\frac{\sinh(a_0)}{a_0}\f$.

    @par Semantic:

    For every parameter of floating type T0

    @code
    T0 r = sinhc(a0);
    @endcode

    is similar to:

    @code
    T0 r = sinh(x)/x;
    @endcode

    @see @funcref{sinh}
    @param a0

    @return a value of the same type as the parameter
  **/
  NT2_FUNCTION_IMPLEMENTATION(tag::sinhc_, sinhc, 1)
}

#endif

