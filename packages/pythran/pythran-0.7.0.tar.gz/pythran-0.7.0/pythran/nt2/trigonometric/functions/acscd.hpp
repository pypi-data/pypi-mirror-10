//==============================================================================
//         Copyright 2003 - 2012   LASMEA UMR 6602 CNRS/Univ. Clermont II
//         Copyright 2009 - 2012   LRI    UMR 8623 CNRS/Univ Paris Sud XI
//
//          Distributed under the Boost Software License, Version 1.0.
//                 See accompanying file LICENSE.txt or copy at
//                     http://www.boost.org/LICENSE_1_0.txt
//==============================================================================
#ifndef NT2_TRIGONOMETRIC_FUNCTIONS_ACSCD_HPP_INCLUDED
#define NT2_TRIGONOMETRIC_FUNCTIONS_ACSCD_HPP_INCLUDED
#include <nt2/include/functor.hpp>


namespace nt2 { namespace tag
  {
   /*!
     @brief acscd generic tag

     Represents the acscd function in generic contexts.

     @par Models:
        Hierarchy
   **/
    struct acscd_ : ext::elementwise_<acscd_>
    {
      /// @brief Parent hierarchy
      typedef ext::elementwise_<acscd_> parent;
    };
  }
  /*!
    inverse cosecant in degree.

    @par Semantic:

    For every parameter of floating type T0

    @code
    T0 r = acscd(a0);
    @endcode

    is similar to:

    @code
    T0 r =  asind(rec(a0));;
    @endcode

    @see @funcref{acsc}
    @param a0

    @return a value of the same type as the parameter
  **/
  NT2_FUNCTION_IMPLEMENTATION(tag::acscd_, acscd, 1)
}

#endif


