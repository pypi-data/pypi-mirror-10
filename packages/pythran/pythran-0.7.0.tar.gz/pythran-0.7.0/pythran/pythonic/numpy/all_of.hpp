#ifndef PYTHONIC_NUMPY_ALL_OF_HPP
#define PYTHONIC_NUMPY_ALL_OF_HPP

#include "pythonic/types/ndarray.hpp"
#include "pythonic/__builtin__/ValueError.hpp"

namespace pythonic {

    namespace numpy {

      template<class P, size_t N>
        struct _all_of;

      template<class P>
        struct _all_of<P, 1> {

          template<class E>
          bool operator()(E const & expr)
            {
              for(auto const & value : expr)
                if(not P{}(value))
                  return false;
              return true;
            }
        };
      template<class P, size_t N>
        struct _all_of {

          template<class E>
          bool operator()(E const & expr)
            {
                return std::all_of(expr.begin(), expr.end(), _all_of<P, N-1>{}) != expr.end();
            }
        };

        template<class P, class E>
            bool
            all_of(E const& expr, types::none_type _ = types::none_type()) {
                return _all_of<P, E::value>{}(expr);
            }

        template<class P, class E>
            auto all_of(E const& expr, long axis)
            -> typename std::enable_if<E::value == 1, decltype(_all_of<P>(expr))>::type
            {
                if(axis != 0)
                    throw types::ValueError("axis out of bounds");
                return all_of(array);
            }

        template<class P, class E>
          typename std::enable_if<E::value != 1, types::ndarray<bool,E::value - 1>::type
          all_of(E const& expr, long axis)
          {
              if(axis<0 || size_t(axis) >= E::value)
                  throw types::ValueError("axis out of bounds");
              auto shape = array.shape;
              if(axis==0)
              {
                  types::array<long, E::value - 1> shp;
                  std::copy(shape.begin() + 1, shape.end(), shp.begin());
                  types::ndarray<bool,N-1> out{shp, true};
                  return std::accumulate(array.begin(), array.end(), out, proxy::multiply());
              }
              else
              {
                  types::array<long, E::value-1> shp;
                  auto next = std::copy(shape.begin(), shape.begin() + axis, shp.begin());
                  std::copy(shape.begin() + axis + 1, shape.end(), next);
                  types::ndarray<bool, E::value - 1> sumy{shp, __builtin__::None};
                  std::transform(array.begin(), array.end(), sumy.begin(),
                                 [axis](typename E::iterator::value_type other) { return _all_of<P>(other, axis - 1); });
                  return sumy;
              }
          }

    }

}

#endif


