#ifndef PYTHONIC_STR_LSTRIP_HPP
#define PYTHONIC_STR_LSTRIP_HPP

#include "pythonic/utils/proxy.hpp"
#include "pythonic/types/str.hpp"

namespace pythonic { namespace __builtin__  {

    namespace str {
        types::str lstrip(types::str const& self, types::str const& to_del = " ")
        {
            return types::str(self.begin() + self.find_first_not_of(to_del), self.end());
        }
        PROXY(pythonic::__builtin__::str, lstrip);

    }

}

}
#endif

