#include "oa2a.h"
#include <stdio.h>
#include <cstring>

test::test(const char* str) {
  _str = str;
}

unsigned int test::getlen() {
  return _str.length();
}

oaString_w::oaString_w(void) {
  //self = new oa::oaString();
  //self = new int;
}

oaString_w::~oaString_w(void) {
  //self = new oa::oaString();
  //self = new int;
  printf("des:%s\n", ptr);
  oa::oaMemory::free(ptr);

  printf("done\n");
}

/*void oa::oaMemory::free(void * ptr) {
  printf("my free\n");
  free(ptr);
}

void * oa::oaMemory::get(unsigned __int64 size) {
  printf("my size\n");
  return malloc(size);
}
void * oa::oaMemory::resize(void * ptr,unsigned __int64 size) {
  //oa::oaMemory::free(ptr);
  //return oa::oaMemory::get(size);
  printf("my resize\n");
}*/

oaString_w::oaString_w(char const * str) {
  //_str = str;
  printf("1: %s\n", str);
  oa::oaString s1(str);
  printf("2: %x\n", &s1);
  printf("3: %d\n", s1.getLength());
  //self = new oa::oaString(str, strlen(str));
  //self = new oa::oaString("teststr");
  //oa::oaString* ptr = new oa::oaString();
  //void* ptr1 = oa::oaMemory::get(sizeof(oa::oaString));
  //printf("32: ptr1: %x : %d: %d\n", ptr1, sizeof(oa::oaString), sizeof(s1));
  //oa::oaString* ptr = new(ptr1) oa::oaString("test1234");
  //oa::oaString* ptr = new(ptr1) oa::oaString();
  //printf("32: ptr1: %x : %d: %d\n", ptr, sizeof(oa::oaString), sizeof(s1));
  //oa::oaString* self;
  //printf("31:%x, %x\n", self, ptr);
  //ptr->~oaString();
  //printf("33: ptr1: %x : %d: %d\n", ptr, sizeof(oa::oaString), sizeof(s1));
  //oa::oaMemory::free(ptr);
  //printf("32: %d\n", ptr->getLength());
  //self = new oa::oaString();
  //*self = s1;
  //self = (oa::oaString*)malloc(sizeof(oa::oaString));
  //self = &s1;
  //printf("4: %d\n", self->getLength());
  //self1 = new test(str);
  //self->oaString(str);
  //memcpy(self, &s1, sizeof(oa::oaString));
  ptr = (char*) oa::oaMemory::get(strlen(str)+1);
  strcpy(ptr, str);
  printf("5: ?\n");
  //delete ptr;
}

/*oaString_w::oaString_w() {
}*/

int oaString_w::getlen() {
  //return _str.length();
  //return self->getLength();
  //return self1->getlen();
  //printf("ptr: %x\n", self);
  return 0;
}

void oaString_w::setstr(const char* str) {
  //self = new oa::oaString(str, strlen(str));
  //_str = str;
}

void oaString_w::toLower() {
  //self->toLower();
}

int main() {
  oaString_w* self = new oaString_w("teststr");
  //printf("13: %d\n", self->getlen());
  printf("14: %d\n", 0);
  delete self;
  return 0;
}
