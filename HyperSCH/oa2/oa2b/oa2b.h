#ifndef OA2B_H
#define OA2B_H

namespace OpenAccess_4 {
  class __declspec(dllexport) oaString {
    public:
      oaString(void);
      oaString(const char*);
      void toLower(void);
      unsigned int getLength(void);

  };
};

void init_oa2b();

#endif
