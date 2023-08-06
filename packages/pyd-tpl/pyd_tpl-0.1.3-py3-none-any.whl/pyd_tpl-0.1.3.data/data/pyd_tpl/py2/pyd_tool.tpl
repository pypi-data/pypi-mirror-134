#ifdef _WIN32
  #define ENCODING "gb18030"
#else
  #define ENCODING "utf8"
#endif
#define get_c_string(x) PyString_AsString(PyUnicode_AsEncodedString(x,ENCODING,"ignore"))
#define print(x){\
   PyObject* builtins = PyImport_ImportModule("__builtin__");\
   PyObject_CallMethod(builtins, (char*)"print", (char*)"O", x);\
}
