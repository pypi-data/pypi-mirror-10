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
    unsigned int    flags;
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
static PyObject * Iface_get_interface(PyObject *cls, PyObject *args, PyObject *kwds);
static PyObject * Iface_set_broad_addr(Iface *self, PyObject *broad_addr);
static PyObject * Iface_set_inet_addr(Iface *self, PyObject *inet_addr);
static PyObject * Iface_set_inet_mask(Iface *self, PyObject *inet_mask);
static PyObject * Iface_update_tx_rx(Iface *self);
static PyObject * Iface_repr(Iface *self);
static PyObject * Iface_str(Iface *self);

static PyObject * pynic_get_list_interfaces(PyObject *self, PyObject *args);

#endif
