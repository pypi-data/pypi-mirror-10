#ifndef CONFIG_H
#define CONFIG_H

#if PY_MAJOR_VERSION >= 3
    #define MOD_INIT(name) PyInit_##name(void)
    #define RETURN_INIT(r)  return r;
    
    #define PyString_Check(obj) PyUnicode_Check(obj)
    #define PyString_FromString(obj) PyUnicode_FromString(obj)
    #define PyString_AsString(obj) PyUnicode_AsUTF8(obj)
    #define PyInt_FromLong(obj) PyLong_FromLong(obj)
#else
    #define MOD_INIT(name) init##name(void)
    #define RETURN_INIT(r)  return;
#endif

#if PY_VERSION_HEX <= 0x02050000
    #define Py_TYPE(ob) (((PyObject*)(ob))->ob_type)
    #define PyVarObject_HEAD_INIT(type, size)   PyObject_HEAD_INIT(type) size,
#endif

#endif
