%module oa2a
%{
  #define SWIG_FILE_WITH_INIT
  #include "oa2a.h"
%}

/* Header Files */

%apply long long { __int64 }
%apply unsigned long long {unsigned __int64 }

%include "oa2a.h"
%include "oa2a1.h"
