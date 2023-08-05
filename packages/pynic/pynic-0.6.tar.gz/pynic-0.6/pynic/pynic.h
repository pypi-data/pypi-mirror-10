#ifndef PYIFACE_H
#define PYIFACE_H

#include <Python.h>
#include "structmember.h"

#include "config.h"
#include "iface.h"

typedef struct{
    PyObject_HEAD
    PyObject        *name;
    PyObject        *inet_addr;
    PyObject        *inet6_addr;
    PyObject        *hw_addr;
    PyObject        *broad_addr;
    PyObject        *inet_mask;
    PyObject        *inet6_mask;
    PyObject        *running;
    PyObject        *updown;
    PyObject        *flags;
    PyObject        *tx_bytes;
    PyObject        *rx_bytes;
    PyObject        *tx_packets;
    PyObject        *rx_packets;
    
}Iface;

static PyTypeObject IfaceType;
static PyObject *pynicIfaceError;

static void Iface_dealloc(Iface* self);
static PyObject * Iface_new(PyTypeObject *type, PyObject *args, PyObject *kwds);
static int Iface_init(Iface *self, PyObject *args, PyObject *kwds);
/* Methods */
static PyObject * Iface_get_interface(PyObject *cls, PyObject *args, PyObject *kwds);
static PyObject * Iface_update_tx_rx(Iface *self);
/* Getters */
static PyObject * Iface_get_broad_addr(Iface *self, void *closure);
static PyObject * Iface_get_flags(Iface *self, void *closure);
static PyObject * Iface_get_inet_addr(Iface *self, void *closure);
static PyObject * Iface_get_inet_mask(Iface *self, void *closure);
static PyObject * Iface_get_inet6_addr(Iface *self, void *closure);
static PyObject * Iface_get_inet6_mask(Iface *self, void *closure);
static PyObject * Iface_get_hw_addr(Iface *self, void *closure);
static PyObject * Iface_get_name(Iface *self, void *closure);
static PyObject * Iface_get_running(Iface *self, void *closure);
static PyObject * Iface_get_rx_bytes(Iface *self, void *closure);
static PyObject * Iface_get_tx_bytes(Iface *self, void *closure);
static PyObject * Iface_get_rx_packets(Iface *self, void *closure);
static PyObject * Iface_get_tx_packets(Iface *self, void *closure);
static PyObject * Iface_get_updown(Iface *self, void *closure);
/* Setters */
static int Iface_set_broad_addr(Iface *self, PyObject *value, void *closure);
static int Iface_set_flags(Iface *self, PyObject *value, void *closure);
static int Iface_set_hw_addr(Iface *self, PyObject *value, void *closure);
static int Iface_set_inet_addr(Iface *self, PyObject *value, void *closure);
static int Iface_set_inet_mask(Iface *self, PyObject *value, void *closure);
static int Iface_set_name(Iface *self, PyObject *value, void *closure);
static int Iface_set_running(Iface *self, PyObject *value, void *closure);
static int Iface_set_updown(Iface *self, PyObject *value, void *closure);
/* Callback Routines */
static PyObject * Iface_repr(Iface *self);
static PyObject * Iface_str(Iface *self);

static PyObject * pynic_get_list_interfaces(PyObject *self, PyObject *args);

#endif
