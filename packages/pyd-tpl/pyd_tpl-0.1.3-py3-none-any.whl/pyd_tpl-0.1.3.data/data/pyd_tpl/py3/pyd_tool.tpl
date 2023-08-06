#ifdef _WIN32
  #define ENCODING "gb18030"
#else
  #define ENCODING "utf8"
#endif
#define get_c_string(x) PyBytes_AS_STRING(PyUnicode_AsEncodedString(x,ENCODING,"ignore"))
#define print(x){\
   PyObject* builtins = PyImport_ImportModule("builtins");\
   PyObject_CallMethod(builtins, (char*)"print", (char*)"O", x);\
}
