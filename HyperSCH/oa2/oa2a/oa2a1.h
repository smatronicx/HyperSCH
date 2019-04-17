#ifndef OA2A1_H
#define OA2A1_H

namespace OpenAccess_4 {
  class oaMemory {
    public:
      static void free(void *);
      static void * get(unsigned __int64);
      static void * resize(void *,unsigned long long);
  };

  class oaString {
    public:
      oaString(void);
      ~oaString(void);
      oaString(char const *);
      oaString(char const *,unsigned int);
      void toLower(void);
      unsigned int getLength(void) const;
      //oaString & operator=(oaString const &);
  };
};

namespace oa = OpenAccess_4;

#endif
