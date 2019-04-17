#include <string>
#include "oa2a1.h"

#ifndef OA2A_H
#define OA2A_H

class test {
  public:
    test(const char* str);
    unsigned int getlen();
  private:
    std::string _str;

};

class oaString_w {
  public:
    oaString_w(void);
    ~oaString_w(void);
    //int junk(void);
    oaString_w(char const * str);
    int getlen();
    void setstr(const char* str);
    void toLower();

  private:
    //oa::oaString* self;
    test* self1;
    char* ptr;
    //int* self;
    std::string _str;
};

int main();

#endif
