#ifndef PYTHONIC_FILE_READLINES_HPP
#define PYTHONIC_FILE_READLINES_HPP

#include "pythonic/utils/proxy.hpp"
#include "pythonic/types/file.hpp"

namespace pythonic { namespace __builtin__  {

    namespace file {
        template<class F>
            types::list<types::str> readlines(F&& f){return f.readlines();}
        template<class F>
            types::list<types::str> readlines(F&& f, int sizehint){return f.readlines(sizehint);}
        PROXY(pythonic::__builtin__::file, readlines);

    }

}

}
#endif

