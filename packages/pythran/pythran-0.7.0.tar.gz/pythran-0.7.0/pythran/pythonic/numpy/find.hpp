#ifndef PYTHONIC_NUMPY_FIND_IF_HPP
#define PYTHONIC_NUMPY_FIND_IF_HPP

#include "pythonic/types/ndarray.hpp"
#include "pythonic/__builtin__/None.hpp"
#include "pythonic/__builtin__/ValueError.hpp"

#include <algorithm>

namespace pythonic {

    namespace numpy {
        template<class Op, class E>
            bool _find_if(E e, utils::int_<1>)
            {
              return std::find_if(e.begin(), e.end(),
                                  [](typename E::const_iterator::value_type value) -> bool { return value; }) != e.end();
            }
        template<class Op, class E, size_t N>
            F _find_if(E e, utils::int_<N>)
            {
              return std::find_if(e.begin(), e.end(),
                                  [](typename E::const_iterator::value_type value) { return _find_if<Op>(value, utils::int_<N - 1>{}); }
              return acc;
            }


        template<class Op, class E>
          bool find_if(E const& expr, types::none_type _ = types::none_type()) {
                return _find_if<Op>(expr, utils::int_<types::numpy_expr_to_ndarray<E>::N>());
          }

        template<class Op, class E>
            auto find_if(E const& array, long axis)
            -> typename std::enable_if<E::value == 1, decltype(find_if<Op>(array))>::type
            {
                if(axis != 0)
                    throw types::ValueError("axis out of bounds");
                return find_if<Op>(array);
            }

        namespace {
          template<class E>
            using found_type = types::ndarray<typename E::dtype, E::value - 1>;
        }
        template<class Op, class E>
            typename std::enable_if<E::value != 1, found_type<E>>::type
            find_if(E const& array, long axis)
            {
                if(axis<0 || size_t(axis) >= E::value)
                    throw types::ValueError("axis out of bounds");
                auto shape = array.shape;
                if(axis==0)
                {
                    types::array<long, E::value - 1> shp;
                    std::copy(shape.begin() + 1, shape.end(), shp.begin());
                    return _find_if<Op>(array, found_type<E>{shp, utils::neutral<Op, typename E::dtype>::value}, utils::int_<1>{});
                }
                else
                {
                    types::array<long, E::value-1> shp;
                    auto next = std::copy(shape.begin(), shape.begin() + axis, shp.begin());
                    std::copy(shape.begin() + axis + 1, shape.end(), next);
                    reduced_type<E> sumy{shp, __builtin__::None};
                    std::transform(array.begin(), array.end(), sumy.begin(),
                                   [axis](typename E::iterator::value_type other) { return reduce<Op>(other, axis - 1); });
                    return sumy;
                }
            }
    }

}

#endif


