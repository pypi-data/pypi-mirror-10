#ifndef PYTHONIC_INCLUDE_OPERATOR_IMUL_HPP
#define PYTHONIC_INCLUDE_OPERATOR_IMUL_HPP

#include "pythonic/utils/proxy.hpp"

namespace pythonic {

    namespace operator_ {

        template <class A, class B>
            auto imul(A const& a, B&& b) -> decltype(a * std::forward<B>(b));

        template <class A, class B>
            auto imul(A& a, B&& b) -> decltype( a*=std::forward<B>(b));

        PROXY_DECL(pythonic::operator_, imul);
    }

}

#endif
