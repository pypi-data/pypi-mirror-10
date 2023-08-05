#include "pynic.h"

/*
 * Members table(variables)
 */

static PyMemberDef Iface_members[] = {
    {NULL}
};

/*
 * Constructor, Destructor, Init
 */

static void
Iface_dealloc(Iface* self)
{
    Py_XDECREF(self->name);
    Py_XDECREF(self->inet_addr);
    Py_XDECREF(self->inet6_addr);
    Py_XDECREF(self->inet_mask);
    Py_XDECREF(self->inet6_mask);
    Py_XDECREF(self->broad_addr);
    Py_XDECREF(self->hw_addr);
    Py_XDECREF(self->running);
    Py_XDECREF(self->updown);
    Py_XDECREF(self->tx_bytes);
    Py_XDECREF(self->rx_bytes);
    Py_XDECREF(self->tx_packets);
    Py_XDECREF(self->rx_packets);
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject *
Iface_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    Iface *self;

    self = (Iface *)type->tp_alloc(type, 0);
    if(self != NULL){
        self->name = PyString_FromString("");
        if (self->name == NULL){
            Py_DECREF(self);
            Py_RETURN_NONE;
        }
        self->inet_addr = PyString_FromString("");
        if (self->inet_addr == NULL){
            Py_DECREF(self);
            Py_RETURN_NONE;
        }
        self->inet6_addr = PyString_FromString("");
        if (self->inet6_addr == NULL){
            Py_DECREF(self);
            Py_RETURN_NONE;
        }
        self->hw_addr = PyString_FromString("");
        if (self->hw_addr == NULL){
            Py_DECREF(self);
            Py_RETURN_NONE;
        }
        self->broad_addr = PyString_FromString("");
        if (self->broad_addr == NULL){
            Py_DECREF(self);
            Py_RETURN_NONE;
        }
        self->inet_mask = PyString_FromString("");
        if (self->inet_mask == NULL){
            Py_DECREF(self);
            Py_RETURN_NONE;
        }
        self->inet6_mask = PyString_FromString("");
        if (self->inet6_mask == NULL){
            Py_DECREF(self);
            Py_RETURN_NONE;
        }
        self->running = PyBool_FromLong(0);
        if (self->running == NULL){
            Py_DECREF(self);
            Py_RETURN_NONE;
        }
        self->updown = PyBool_FromLong(0);
        if (self->updown == NULL){
            Py_DECREF(self);
            Py_RETURN_NONE;
        }
        self->flags = 0;
        
        self->tx_bytes = PyInt_FromLong(0);
        if (self->tx_bytes == NULL){
            Py_DECREF(self);
            Py_RETURN_NONE;
        }
        self->rx_bytes = PyInt_FromLong(0);
        if (self->rx_bytes == NULL){
            Py_DECREF(self);
            Py_RETURN_NONE;
        }
        self->tx_packets = PyInt_FromLong(0);
        if (self->tx_packets == NULL){
            Py_DECREF(self);
            Py_RETURN_NONE;
        }
        self->rx_packets = PyInt_FromLong(0);
        if (self->rx_packets == NULL){
            Py_DECREF(self);
            Py_RETURN_NONE;
        }
    }

    return (PyObject *)self;
}

static int
Iface_init(Iface *self, PyObject *args, PyObject *kwds)
{
    PyObject *name=NULL, *inet_addr=NULL, *inet6_addr=NULL, *hw_addr=NULL,
             *broad_addr=NULL, *inet_mask=NULL, *inet6_mask=NULL,
             *running=NULL, *updown=NULL, *tx_bytes=NULL, *rx_bytes=NULL,
             *tx_packets=NULL, *rx_packets=NULL, *tmp;

    static char *kwlist[] = {"name", "inet_addr", "inet6_addr", "hw_addr",
                             "broad_addr", "inet_mask", "inet6_mask",
                             "running", "updown", "flags", "tx_bytes",
                             "rx_bytes", "tx_packets", "rx_packets",
                             NULL};

    if(!PyArg_ParseTupleAndKeywords(args, kwds, "|OOOOOOOOOiOOOO", kwlist,
                                     &name, &inet_addr, &inet6_addr,
                                     &hw_addr, &broad_addr, &inet_mask,
                                     &inet6_mask, &running, &updown,
                                     &self->flags, &self->tx_bytes,
                                     &rx_bytes, &self->tx_packets,
                                     &self->rx_packets))
    {
        return -1;
    }

    if(name){
        tmp = self->name;
        Py_INCREF(name);
        self->name = name;
        Py_XDECREF(tmp);
    }
    
    if(inet_addr){
        tmp = self->inet_addr;
        Py_INCREF(inet_addr);
        self->inet_addr = inet_addr;
        Py_XDECREF(tmp);
    }
    
    if(inet6_addr){
        tmp = self->inet6_addr;
        Py_INCREF(inet6_addr);
        self->inet6_addr = inet6_addr;
        Py_XDECREF(tmp);
    }
    
    if(hw_addr){
        tmp = self->hw_addr;
        Py_INCREF(hw_addr);
        self->hw_addr = hw_addr;
        Py_XDECREF(tmp);
    }
    
    if(broad_addr){
        tmp = self->broad_addr;
        Py_INCREF(broad_addr);
        self->broad_addr = broad_addr;
        Py_XDECREF(tmp);
    }
    
    if(inet_mask){
        tmp = self->inet_mask;
        Py_INCREF(inet_mask);
        self->inet_mask = inet_mask;
        Py_XDECREF(tmp);
    }
    
    if(inet6_mask){
        tmp = self->inet6_mask;
        Py_INCREF(inet6_mask);
        self->inet6_mask = inet6_mask;
        Py_XDECREF(tmp);
    }
    
    if(running){
        tmp = self->running;
        Py_INCREF(running);
        self->running = running;
        Py_XDECREF(tmp);
    }
    
    if(updown){
        tmp = self->updown;
        Py_INCREF(updown);
        self->updown = updown;
        Py_XDECREF(tmp);
    }
    
    if(tx_bytes){
        tmp = self->tx_bytes;
        Py_INCREF(tx_bytes);
        self->tx_bytes = tx_bytes;
        Py_XDECREF(tmp);
    }
    
    if(rx_bytes){
        tmp = self->rx_bytes;
        Py_INCREF(rx_bytes);
        self->rx_bytes = rx_bytes;
        Py_XDECREF(tmp);
    }
    
    if(tx_packets){
        tmp = self->tx_packets;
        Py_INCREF(tx_packets);
        self->tx_packets = tx_packets;
        Py_XDECREF(tmp);
    }
    
    if(rx_packets){
        tmp = self->rx_packets;
        Py_INCREF(rx_packets);
        self->rx_packets = rx_packets;
        Py_XDECREF(tmp);
    }

    return 0;
}

/*
 * Methods
 */

static PyObject *
Iface_get_interface(PyObject *cls, PyObject *args, PyObject *kwds)
{
    const char *iface_name;
    struct iface ifa;
    Iface *self;
    
    if (!PyArg_ParseTuple(args, "s", &iface_name)){
        Py_RETURN_NONE;
    }
    
    if(get_info_interface(&ifa, iface_name)){
        PyErr_SetString(pynicIfaceError, "There is no NIC with this name.");
        Py_RETURN_NONE;
    }
    
    self = (Iface*) Iface_new(&IfaceType, args, kwds);
    Iface_init(self, args, kwds);
    
    self->name = PyString_FromString(ifa.name);
    self->inet_addr = PyString_FromString(ifa.inet_addr);
    self->inet6_addr = PyString_FromString(ifa.inet6_addr);
    self->hw_addr = PyString_FromString(ifa.hw_addr);
    self->broad_addr = PyString_FromString(ifa.broad_addr);
    self->inet_mask = PyString_FromString(ifa.inet_mask);
    self->inet6_mask = PyString_FromString(ifa.inet6_mask);
    self->running = PyBool_FromLong(ifa.running);
    self->updown = PyBool_FromLong(ifa.updown);
    //self->flags = ifa.flags;
    self->flags = PyInt_FromLong(ifa.flags);
    self->tx_bytes = PyInt_FromLong(ifa.tx_bytes);
    self->rx_bytes = PyInt_FromLong(ifa.rx_bytes);
    self->tx_packets = PyInt_FromLong(ifa.tx_packets);
    self->rx_packets = PyInt_FromLong(ifa.rx_packets);

    return (PyObject*)self;
 }

static PyObject *
Iface_update_tx_rx(Iface *self)
{
    struct iface ifa;
    PyObject* tmp;
    
    tmp = self->name;
    
    init_iface(&ifa);
    
    ifa.name = PyString_AsString(tmp);
    update_tx_rx(&ifa);
    self->tx_bytes = PyInt_FromLong(ifa.tx_bytes);
    self->rx_bytes = PyInt_FromLong(ifa.rx_bytes);
    self->tx_packets = PyInt_FromLong(ifa.tx_packets);
    self->rx_packets = PyInt_FromLong(ifa.rx_packets);
    
    Py_RETURN_TRUE;
}

/* Getters */

static PyObject *
Iface_get_broad_addr(Iface *self, void *closure)
{
    Py_INCREF(self->broad_addr);
    return self->broad_addr;
}

static PyObject *
Iface_get_flags(Iface *self, void *closure)
{
    Py_INCREF(self->flags);
    return self->flags;
}

static PyObject *
Iface_get_inet_addr(Iface *self, void *closure)
{
    Py_INCREF(self->inet_addr);
    return self->inet_addr;
}

static PyObject *
Iface_get_inet_mask(Iface *self, void *closure)
{
    Py_INCREF(self->inet_mask);
    return self->inet_mask;
}

static PyObject *
Iface_get_inet6_addr(Iface *self, void *closure)
{
    Py_INCREF(self->inet6_addr);
    return self->inet6_addr;
}

static PyObject *
Iface_get_inet6_mask(Iface *self, void *closure)
{
    Py_INCREF(self->inet6_mask);
    return self->inet6_mask;
}

static PyObject *
Iface_get_hw_addr(Iface *self, void *closure)
{
    Py_INCREF(self->hw_addr);
    return self->hw_addr;
}

static PyObject *
Iface_get_name(Iface *self, void *closure)
{
    Py_INCREF(self->name);
    return self->name;
}

static PyObject * 
Iface_get_running(Iface *self, void *closure)
{
    Py_INCREF(self->running);
    return self->running;
}

static PyObject * 
Iface_get_rx_bytes(Iface *self, void *closure)
{
    Py_INCREF(self->rx_bytes);
    return self->rx_bytes;
}

static PyObject * 
Iface_get_tx_bytes(Iface *self, void *closure)
{
    Py_INCREF(self->tx_bytes);
    return self->tx_bytes;
}

static PyObject * 
Iface_get_rx_packets(Iface *self, void *closure)
{
    Py_INCREF(self->rx_packets);
    return self->rx_packets;
}

static PyObject * 
Iface_get_tx_packets(Iface *self, void *closure)
{
    Py_INCREF(self->tx_packets);
    return self->tx_packets;
}

static PyObject * 
Iface_get_updown(Iface *self, void *closure)
{
    Py_INCREF(self->updown);
    return self->updown;
}

/* Setters */

static int
Iface_set_broad_addr(Iface *self, PyObject *value, void *closure)
{
    struct iface ifa;
    int result;
    
    if (value == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete the broad_addr attribute");
        return -1;
    }
      
    if(!PyString_Check(value)){
        PyErr_BadArgument();
        return -1;
    }
        
    init_iface(&ifa);
    
    ifa.name = PyString_AsString(self->name);
    result = set_broad_addr(&ifa, PyString_AsString(value));
    
    if(result == EPERM){
        PyErr_SetString(pynicIfaceError, strerror(result));
    }else if(result == -1){
        PyErr_SetString(pynicIfaceError, "Invalid address");
    }
    
    
    if(result != 0){
        return -1;
    }else{
        Py_DECREF(self->broad_addr);
        self->broad_addr = PyString_FromString(PyString_AsString(value));
        
        return 0;
    }
}

static int
Iface_set_flags(Iface *self, PyObject *value, void *closure)
{
    struct iface ifa;
    int result;
    
    if (value == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete the flags attribute");
        return -1;
    }
    
    /* TODO Check if it is working in all versions */
    if(!PyInt_Check(value)){
        PyErr_BadArgument();
        return -1;
    }
        
    init_iface(&ifa);
    
    ifa.name = PyString_AsString(self->name);
    result = set_flags(&ifa, PyInt_AsLong(value));
    
    if(result == EPERM){
        PyErr_SetString(pynicIfaceError, strerror(result));
    }
    
    if(result != 0){
        return -1;
    }else{
        Py_DECREF(self->flags);
        Py_DECREF(self->running);
        Py_DECREF(self->updown);
        
        self->flags = PyInt_FromLong(ifa.flags);
        self->running = PyBool_FromLong(ifa.running);
        self->updown = PyBool_FromLong(ifa.updown);
        
        return 0;
    }
}

static int
Iface_set_inet_addr(Iface *self, PyObject *value, void *closure)
{
    /* TODO Update all possible variables when happens a change */
    
    struct iface ifa;
    int result;
    
    if (value == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete the inet_addr attribute");
        return -1;
    }
    
    if(!PyString_Check(value)){
        PyErr_BadArgument();
        return -1;
    }
       
    init_iface(&ifa);
    
    ifa.name = PyString_AsString(self->name);
    result = set_inet_addr(&ifa, PyString_AsString(value));
    
    if(result == EPERM){
        PyErr_SetString(pynicIfaceError, strerror(result));
    }else if(result == -1){
        PyErr_SetString(pynicIfaceError, "Invalid address");
    }
    
    
    if(result != 0){
        return -1;
    }else{
        Py_DECREF(self->inet_addr);
        self->inet_addr = PyString_FromString(PyString_AsString(value));

        return 0;
    }
}

static int
Iface_set_inet_mask(Iface *self, PyObject *value, void *closure)
{
    struct iface ifa;
    int result;
    
    if (value == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete the inet_mask attribute");
        return -1;
    }
    
    if(!PyString_Check(value)){
        PyErr_BadArgument();
        
        return -1;
    }
    
    init_iface(&ifa);
    
    ifa.name = PyString_AsString(self->name);
    
    result = set_inet_mask(&ifa, PyString_AsString(value));
    
    if(result == EPERM){
        PyErr_SetString(pynicIfaceError, strerror(result));
    }else if(result == -1){
        PyErr_SetString(pynicIfaceError, "Invalid address");
    }
    
    if(result != 0){
        return -1;
    }else{
        Py_DECREF(self->inet_mask);
        self->inet_mask = PyString_FromString(PyString_AsString(value));

        return 0;
    }
}

static int 
Iface_set_running(Iface *self, PyObject *value, void *closure)
{
    struct iface ifa;
    int result;
    unsigned int flags;
    
    if (value == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete the running attribute");
        return -1;
    }
    
    if(!PyBool_Check(value)){
        PyErr_BadArgument();
        
        return -1;
    }
    
    init_iface(&ifa);
    
    ifa.name = PyString_AsString(self->name);
    
    if(PyObject_RichCompareBool(value, Py_True, Py_EQ))
    {
        flags = PyInt_AsLong(self->flags) | IFF_RUNNING;
    }else{
        flags = ~IFF_RUNNING;
        flags &= PyInt_AsLong(self->flags);
    }

    result = set_flags(&ifa, flags);
    
    if(result == EPERM){
        PyErr_SetString(pynicIfaceError, strerror(result));
    }
    
    if(result != 0){
        return -1;
    }else{
        Py_DECREF(self->flags);
        Py_DECREF(self->running);
        
        self->flags = PyInt_FromLong(ifa.flags);
        self->running = PyBool_FromLong(ifa.running);

        return 0;
    }
}

static int 
Iface_set_updown(Iface *self, PyObject *value, void *closure)
{
    struct iface ifa;
    int result;
    unsigned int flags;
    
    if (value == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete the updown attribute");
        return -1;
    }
    
    if(!PyBool_Check(value)){
        PyErr_BadArgument();
        
        return -1;
    }
    
    init_iface(&ifa);
    
    ifa.name = PyString_AsString(self->name);
    
    if(PyObject_RichCompareBool(value, Py_True, Py_EQ))
    {
        flags = PyInt_AsLong(self->flags) | IFF_UP;
    }else{
        flags = ~IFF_UP;
        flags &= PyInt_AsLong(self->flags);
    }

    result = set_flags(&ifa, flags);
    
    if(result == EPERM){
        PyErr_SetString(pynicIfaceError, strerror(result));
    }
    
    if(result != 0){
        return -1;
    }else{
        Py_DECREF(self->flags);
        Py_DECREF(self->updown);
        
        self->flags = PyInt_FromLong(ifa.flags);
        self->updown = PyBool_FromLong(ifa.updown);

        return 0;
    }
}

/*
 * Methods Table
 */

static PyMethodDef Iface_methods[] = {
    {"get_interface", (PyCFunction)Iface_get_interface, METH_VARARGS|METH_CLASS,
     "Return a Iface object with all its information."},
    {"update_tx_rx",  (PyCFunction)Iface_update_tx_rx, METH_NOARGS,
     "Update NIC's TX/RX information."},
    {NULL}  /* Sentinel */
};

/*
 * Callback Routines
 */

static PyObject *
Iface_repr(Iface *self)
{
    char *name;
    
    if(PyString_Check(self->name)){
        name = PyString_AsString(self->name);

        return PyString_FromString(name);
    }
    
    PyErr_SetString(pynicIfaceError, "Object's name is not a string object.");
    
    Py_RETURN_NONE;
}

static PyObject *
Iface_str(Iface *self)
{
    char *name;
    
    if(PyString_Check(self->name)){
        name = PyString_AsString(self->name);

        return PyString_FromString(name);
    }
    
    PyErr_SetString(pynicIfaceError, "Object's name is not a string object.");
    
    Py_RETURN_NONE;
}

static PyGetSetDef Iface_getseters[] = {
    {"broad_addr", (getter)Iface_get_broad_addr, (setter)Iface_set_broad_addr,
     "Interface's Broadcast address", NULL},
    {"flags", (getter)Iface_get_flags, (setter)Iface_set_flags,
     "Other Interface's flags", NULL},
    {"inet_addr", (getter)Iface_get_inet_addr, (setter)Iface_set_inet_addr,
     "Interface's IPv4 address", NULL},
    {"inet_mask", (getter)Iface_get_inet_mask, (setter)Iface_set_inet_mask,
     "Interface's Network Mask v4 address", NULL},
    {"inet6_addr", (getter)Iface_get_inet6_addr, (setter)NULL,
     "Interface's IPv6 address", NULL},
    {"inet6_mask", (getter)Iface_get_inet6_mask, (setter)NULL,
     "Interface's Network Mask v6 address", NULL},
    {"running", (getter)Iface_get_running, (setter)Iface_set_running,
     "Indicates if interface is running or not", NULL},
    {"hw_addr", (getter)Iface_get_hw_addr, (setter)NULL,
     "Interface's MAC address", NULL},
    {"name", (getter)Iface_get_name, (setter)NULL,
     "Interface's name", NULL},
    {"rx_bytes", (getter)Iface_get_rx_bytes, (setter)NULL,
     "Amount of bytes that the interface received", NULL},
    {"tx_bytes", (getter)Iface_get_tx_bytes, (setter)NULL,
     "Amount of bytes that the interface transmitted", NULL},
    {"rx_packets", (getter)Iface_get_rx_packets, (setter)NULL,
     "Amount of packets that the interface received", NULL},
    {"tx_packets", (getter)Iface_get_tx_packets, (setter)NULL,
     "Amount of packets that the interface transmitted", NULL},
    {"updown", (getter)Iface_get_updown, (setter)Iface_set_updown,
     "Indicates if interfaces is Up or Down", NULL},
    {NULL}  /* Sentinel */
};

/*
 * Type definition
 */

static PyTypeObject IfaceType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "pyiface.Iface",                            /* tp_name */
    sizeof(Iface),                              /* tp_basicsize */
    0,                                          /* tp_itemsize */
    (destructor)Iface_dealloc,                  /* tp_dealloc */
    0,                                          /* tp_print */
    0,                                          /* tp_getattr */
    0,                                          /* tp_setattr */
    0,                                          /* tp_compare */
    (reprfunc)Iface_repr,                       /* tp_repr */
    0,                                          /* tp_as_number */
    0,                                          /* tp_as_sequence */
    0,                                          /* tp_as_mapping */
    0,                                          /* tp_hash */
    0,                                          /* tp_call */
    (reprfunc)Iface_str,                        /* tp_str */
    0,                                          /* tp_getattro */
    0,                                          /* tp_setattro */
    0,                                          /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,   /* tp_flags */
    "Iface objects",                            /* tp_doc */
    0,		                                    /* tp_traverse */
    0,		                                    /* tp_clear */
    0,		                                    /* tp_richcompare */
    0,		                                    /* tp_weaklistoffset */
    0,		                                    /* tp_iter */
    0,		                                    /* tp_iternext */
    Iface_methods,                              /* tp_methods */
    Iface_members,                              /* tp_members */
    Iface_getseters,                                          /* tp_getset */
    0,                                          /* tp_base */
    0,                                          /* tp_dict */
    0,                                          /* tp_descr_get */
    0,                                          /* tp_descr_set */
    0,                                          /* tp_dictoffset */
    (initproc)Iface_init,                       /* tp_init */
    0,                                          /* tp_alloc */
    Iface_new,                                  /* tp_new */
};

/*
 * Module Functions
 */

static PyObject *
pynic_get_list_interfaces(PyObject *self, PyObject *args)
{
    char **list;
    int len_list;
    int i;
    len_list = get_list_interfaces(&list);
    PyObject *list_nic;
    
    list_nic = PyList_New(0);
    
    for(i=0; i < len_list; i++){
        PyList_Append(list_nic, PyString_FromString(list[i]));
    }
    
    Py_INCREF(list_nic);
    return list_nic;
}

/*
 * Module Functions Table
 */

static PyMethodDef module_functions[] = {
    {"get_list_interfaces",  pynic_get_list_interfaces, METH_NOARGS,
        "List all available Network Interface."},
    {NULL, NULL, 0, NULL}
};

#if PY_MAJOR_VERSION >= 3
/*
 * Module Definition
 */
    static struct PyModuleDef module_pynic = {
        PyModuleDef_HEAD_INIT,
        "pynic",                                                    /* m_name */
        "Module for getting Network Interface Cards information.",  /* m_doc */
        -1,                                                         /* m_size */
        module_functions,                                           /* m_methods */
        NULL,                                                       /* m_reload */
        NULL,                                                       /* m_traverse */
        NULL,                                                       /* m_clear */
        NULL,                                                       /* m_free */
    };
#endif

/*
 * Init Module
 */

#ifndef PyMODINIT_FUNC
    #define PyMODINIT_FUNC void
#endif

PyMODINIT_FUNC
MOD_INIT(pynic)
{
    PyObject* module;

    if (PyType_Ready(&IfaceType) < 0){
        RETURN_INIT(NULL);
    }
    
    #if PY_MAJOR_VERSION >= 3
    module = PyModule_Create(&module_pynic);
    #else
    module = Py_InitModule3("pynic", module_functions,
                       "Module for getting Network Interface Cards information.");
    #endif

    if (module == NULL){
        RETURN_INIT(NULL);
    }
    
    pynicIfaceError = PyErr_NewException("pynic.IfaceError", NULL, NULL);
    Py_INCREF(pynicIfaceError);
    PyModule_AddObject(module, "error", pynicIfaceError);
    
    Py_INCREF(&IfaceType);
    PyModule_AddObject(module, "Iface", (PyObject *)&IfaceType);
    
    /*
     * Exporting constants
     * You can check documentation on
     * http://man7.org/linux/man-pages/man7/netdevice.7.html
     */
    
    /*
     * TODO These flags should be revised about if they are really needed
     * on this module
     */
    /*PyModule_AddIntConstant(module, "SIOCGIFNAME", SIOCGIFNAME);
    PyModule_AddIntConstant(module, "SIOCGIFINDEX", SIOCGIFINDEX);
    PyModule_AddIntConstant(module, "SIOCGIFFLAGS", SIOCGIFFLAGS);
    PyModule_AddIntConstant(module, "SIOCSIFFLAGS", SIOCSIFFLAGS);
    PyModule_AddIntConstant(module, "SIOCGIFPFLAGS", SIOCGIFPFLAGS);
    PyModule_AddIntConstant(module, "SIOCSIFPFLAGS", SIOCSIFPFLAGS);
    PyModule_AddIntConstant(module, "SIOCGIFADDR", SIOCGIFADDR);
    PyModule_AddIntConstant(module, "SIOCSIFADDR", SIOCSIFADDR);
    PyModule_AddIntConstant(module, "SIOCGIFDSTADDR", SIOCGIFDSTADDR);
    PyModule_AddIntConstant(module, "SIOCSIFDSTADDR", SIOCSIFDSTADDR);
    PyModule_AddIntConstant(module, "SIOCGIFBRDADDR", SIOCGIFBRDADDR);
    PyModule_AddIntConstant(module, "SIOCSIFBRDADDR", SIOCSIFBRDADDR);
    PyModule_AddIntConstant(module, "SIOCGIFNETMASK", SIOCGIFNETMASK);
    PyModule_AddIntConstant(module, "SIOCSIFNETMASK", SIOCSIFNETMASK);
    PyModule_AddIntConstant(module, "SIOCGIFMETRIC", SIOCSIFMETRIC);
    PyModule_AddIntConstant(module, "SIOCGIFMTU", SIOCGIFMTU);
    PyModule_AddIntConstant(module, "SIOCSIFMTU", SIOCSIFMTU);
    PyModule_AddIntConstant(module, "SIOCGIFHWADDR", SIOCGIFHWADDR);
    PyModule_AddIntConstant(module, "SIOCSIFHWADDR", SIOCSIFHWADDR);
    PyModule_AddIntConstant(module, "SIOCSIFHWBROADCAST", SIOCSIFHWBROADCAST);
    PyModule_AddIntConstant(module, "SIOCGIFMAP", SIOCGIFMAP);
    PyModule_AddIntConstant(module, "SIOCSIFMAP", SIOCSIFMAP);
    PyModule_AddIntConstant(module, "SIOCADDMULTI", SIOCADDMULTI);
    PyModule_AddIntConstant(module, "SIOCDELMULTI", SIOCDELMULTI);
    PyModule_AddIntConstant(module, "SIOCGIFTXQLEN", SIOCGIFTXQLEN);
    PyModule_AddIntConstant(module, "SIOCSIFTXQLEN", SIOCSIFTXQLEN);
    PyModule_AddIntConstant(module, "SIOCSIFNAME", SIOCSIFNAME);
    PyModule_AddIntConstant(module, "SIOCGIFFLAGS", SIOCGIFFLAGS);
    PyModule_AddIntConstant(module, "SIOCGIFCONF", SIOCGIFCONF);*/
    
    PyModule_AddIntConstant(module, "IFF_UP", IFF_UP);
    PyModule_AddIntConstant(module, "IFF_BROADCAST", IFF_BROADCAST);
    PyModule_AddIntConstant(module, "IFF_DEBUG", IFF_DEBUG);
    PyModule_AddIntConstant(module, "IFF_LOOPBACK", IFF_LOOPBACK);
    PyModule_AddIntConstant(module, "IFF_POINTOPOINT", IFF_POINTOPOINT);
    PyModule_AddIntConstant(module, "IFF_RUNNING", IFF_RUNNING);
    PyModule_AddIntConstant(module, "IFF_NOARP", IFF_NOARP);
    PyModule_AddIntConstant(module, "IFF_PROMISC", IFF_PROMISC);
    PyModule_AddIntConstant(module, "IFF_NOTRAILERS", IFF_NOTRAILERS);
    PyModule_AddIntConstant(module, "IFF_ALLMULTI", IFF_ALLMULTI);
    PyModule_AddIntConstant(module, "IFF_MASTER", IFF_MASTER);
    PyModule_AddIntConstant(module, "IFF_SLAVE", IFF_SLAVE);
    PyModule_AddIntConstant(module, "IFF_MULTICAST", IFF_MULTICAST);
    PyModule_AddIntConstant(module, "IFF_PORTSEL", IFF_PORTSEL);
    PyModule_AddIntConstant(module, "IFF_AUTOMEDIA", IFF_AUTOMEDIA);
    PyModule_AddIntConstant(module, "IFF_DYNAMIC", IFF_DYNAMIC);
    PyModule_AddIntConstant(module, "IFF_LOWER_UP", IFF_LOWER_UP);
    PyModule_AddIntConstant(module, "IFF_DORMANT", IFF_DORMANT);
    PyModule_AddIntConstant(module, "IFF_ECHO", IFF_ECHO);
    
    /* TODO These flags must be revised */
    /*PyModule_AddIntConstant(module, "IFF_802_1Q_VLAN", IFF_802_1Q_VLAN);
    PyModule_AddIntConstant(module, "IFF_EBRIDGE", IFF_EBRIDGE);
    PyModule_AddIntConstant(module, "IFF_SLAVE_INACTIVE", IFF_SLAVE_INACTIVE);
    PyModule_AddIntConstant(module, "IFF_MASTER_8023AD", IFF_MASTER_8023AD);
    PyModule_AddIntConstant(module, "IFF_MASTER_ALB", IFF_MASTER_ALB);
    PyModule_AddIntConstant(module, "IFF_BONDING", IFF_BONDING);
    PyModule_AddIntConstant(module, "IFF_SLAVE_NEEDARP", IFF_SLAVE_NEEDARP);
    PyModule_AddIntConstant(module, "IFF_ISATAP", IFF_ISATAP);*/
    
    RETURN_INIT(module);
}
