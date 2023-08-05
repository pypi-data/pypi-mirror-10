
#include <Python.h>
#include <stddef.h>

/* this block of #ifs should be kept exactly identical between
   c/_cffi_backend.c, cffi/vengine_cpy.py, cffi/vengine_gen.py */
#if defined(_MSC_VER)
# include <malloc.h>   /* for alloca() */
# if _MSC_VER < 1600   /* MSVC < 2010 */
   typedef __int8 int8_t;
   typedef __int16 int16_t;
   typedef __int32 int32_t;
   typedef __int64 int64_t;
   typedef unsigned __int8 uint8_t;
   typedef unsigned __int16 uint16_t;
   typedef unsigned __int32 uint32_t;
   typedef unsigned __int64 uint64_t;
   typedef __int8 int_least8_t;
   typedef __int16 int_least16_t;
   typedef __int32 int_least32_t;
   typedef __int64 int_least64_t;
   typedef unsigned __int8 uint_least8_t;
   typedef unsigned __int16 uint_least16_t;
   typedef unsigned __int32 uint_least32_t;
   typedef unsigned __int64 uint_least64_t;
   typedef __int8 int_fast8_t;
   typedef __int16 int_fast16_t;
   typedef __int32 int_fast32_t;
   typedef __int64 int_fast64_t;
   typedef unsigned __int8 uint_fast8_t;
   typedef unsigned __int16 uint_fast16_t;
   typedef unsigned __int32 uint_fast32_t;
   typedef unsigned __int64 uint_fast64_t;
   typedef __int64 intmax_t;
   typedef unsigned __int64 uintmax_t;
# else
#  include <stdint.h>
# endif
# if _MSC_VER < 1800   /* MSVC < 2013 */
   typedef unsigned char _Bool;
# endif
#else
# include <stdint.h>
# if (defined (__SVR4) && defined (__sun)) || defined(_AIX)
#  include <alloca.h>
# endif
#endif

#if PY_MAJOR_VERSION < 3
# undef PyCapsule_CheckExact
# undef PyCapsule_GetPointer
# define PyCapsule_CheckExact(capsule) (PyCObject_Check(capsule))
# define PyCapsule_GetPointer(capsule, name) \
    (PyCObject_AsVoidPtr(capsule))
#endif

#if PY_MAJOR_VERSION >= 3
# define PyInt_FromLong PyLong_FromLong
#endif

#define _cffi_from_c_double PyFloat_FromDouble
#define _cffi_from_c_float PyFloat_FromDouble
#define _cffi_from_c_long PyInt_FromLong
#define _cffi_from_c_ulong PyLong_FromUnsignedLong
#define _cffi_from_c_longlong PyLong_FromLongLong
#define _cffi_from_c_ulonglong PyLong_FromUnsignedLongLong

#define _cffi_to_c_double PyFloat_AsDouble
#define _cffi_to_c_float PyFloat_AsDouble

#define _cffi_from_c_int_const(x)                                        \
    (((x) > 0) ?                                                         \
        ((unsigned long long)(x) <= (unsigned long long)LONG_MAX) ?      \
            PyInt_FromLong((long)(x)) :                                  \
            PyLong_FromUnsignedLongLong((unsigned long long)(x)) :       \
        ((long long)(x) >= (long long)LONG_MIN) ?                        \
            PyInt_FromLong((long)(x)) :                                  \
            PyLong_FromLongLong((long long)(x)))

#define _cffi_from_c_int(x, type)                                        \
    (((type)-1) > 0 ? /* unsigned */                                     \
        (sizeof(type) < sizeof(long) ?                                   \
            PyInt_FromLong((long)x) :                                    \
         sizeof(type) == sizeof(long) ?                                  \
            PyLong_FromUnsignedLong((unsigned long)x) :                  \
            PyLong_FromUnsignedLongLong((unsigned long long)x)) :        \
        (sizeof(type) <= sizeof(long) ?                                  \
            PyInt_FromLong((long)x) :                                    \
            PyLong_FromLongLong((long long)x)))

#define _cffi_to_c_int(o, type)                                          \
    (sizeof(type) == 1 ? (((type)-1) > 0 ? (type)_cffi_to_c_u8(o)        \
                                         : (type)_cffi_to_c_i8(o)) :     \
     sizeof(type) == 2 ? (((type)-1) > 0 ? (type)_cffi_to_c_u16(o)       \
                                         : (type)_cffi_to_c_i16(o)) :    \
     sizeof(type) == 4 ? (((type)-1) > 0 ? (type)_cffi_to_c_u32(o)       \
                                         : (type)_cffi_to_c_i32(o)) :    \
     sizeof(type) == 8 ? (((type)-1) > 0 ? (type)_cffi_to_c_u64(o)       \
                                         : (type)_cffi_to_c_i64(o)) :    \
     (Py_FatalError("unsupported size for type " #type), (type)0))

#define _cffi_to_c_i8                                                    \
                 ((int(*)(PyObject *))_cffi_exports[1])
#define _cffi_to_c_u8                                                    \
                 ((int(*)(PyObject *))_cffi_exports[2])
#define _cffi_to_c_i16                                                   \
                 ((int(*)(PyObject *))_cffi_exports[3])
#define _cffi_to_c_u16                                                   \
                 ((int(*)(PyObject *))_cffi_exports[4])
#define _cffi_to_c_i32                                                   \
                 ((int(*)(PyObject *))_cffi_exports[5])
#define _cffi_to_c_u32                                                   \
                 ((unsigned int(*)(PyObject *))_cffi_exports[6])
#define _cffi_to_c_i64                                                   \
                 ((long long(*)(PyObject *))_cffi_exports[7])
#define _cffi_to_c_u64                                                   \
                 ((unsigned long long(*)(PyObject *))_cffi_exports[8])
#define _cffi_to_c_char                                                  \
                 ((int(*)(PyObject *))_cffi_exports[9])
#define _cffi_from_c_pointer                                             \
    ((PyObject *(*)(char *, CTypeDescrObject *))_cffi_exports[10])
#define _cffi_to_c_pointer                                               \
    ((char *(*)(PyObject *, CTypeDescrObject *))_cffi_exports[11])
#define _cffi_get_struct_layout                                          \
    ((PyObject *(*)(Py_ssize_t[]))_cffi_exports[12])
#define _cffi_restore_errno                                              \
    ((void(*)(void))_cffi_exports[13])
#define _cffi_save_errno                                                 \
    ((void(*)(void))_cffi_exports[14])
#define _cffi_from_c_char                                                \
    ((PyObject *(*)(char))_cffi_exports[15])
#define _cffi_from_c_deref                                               \
    ((PyObject *(*)(char *, CTypeDescrObject *))_cffi_exports[16])
#define _cffi_to_c                                                       \
    ((int(*)(char *, CTypeDescrObject *, PyObject *))_cffi_exports[17])
#define _cffi_from_c_struct                                              \
    ((PyObject *(*)(char *, CTypeDescrObject *))_cffi_exports[18])
#define _cffi_to_c_wchar_t                                               \
    ((wchar_t(*)(PyObject *))_cffi_exports[19])
#define _cffi_from_c_wchar_t                                             \
    ((PyObject *(*)(wchar_t))_cffi_exports[20])
#define _cffi_to_c_long_double                                           \
    ((long double(*)(PyObject *))_cffi_exports[21])
#define _cffi_to_c__Bool                                                 \
    ((_Bool(*)(PyObject *))_cffi_exports[22])
#define _cffi_prepare_pointer_call_argument                              \
    ((Py_ssize_t(*)(CTypeDescrObject *, PyObject *, char **))_cffi_exports[23])
#define _cffi_convert_array_from_object                                  \
    ((int(*)(char *, CTypeDescrObject *, PyObject *))_cffi_exports[24])
#define _CFFI_NUM_EXPORTS 25

typedef struct _ctypedescr CTypeDescrObject;

static void *_cffi_exports[_CFFI_NUM_EXPORTS];
static PyObject *_cffi_types, *_cffi_VerificationError;

static int _cffi_setup_custom(PyObject *lib);   /* forward */

static PyObject *_cffi_setup(PyObject *self, PyObject *args)
{
    PyObject *library;
    int was_alive = (_cffi_types != NULL);
    (void)self; /* unused */
    if (!PyArg_ParseTuple(args, "OOO", &_cffi_types, &_cffi_VerificationError,
                                       &library))
        return NULL;
    Py_INCREF(_cffi_types);
    Py_INCREF(_cffi_VerificationError);
    if (_cffi_setup_custom(library) < 0)
        return NULL;
    return PyBool_FromLong(was_alive);
}

static int _cffi_init(void)
{
    PyObject *module, *c_api_object = NULL;

    module = PyImport_ImportModule("_cffi_backend");
    if (module == NULL)
        goto failure;

    c_api_object = PyObject_GetAttrString(module, "_C_API");
    if (c_api_object == NULL)
        goto failure;
    if (!PyCapsule_CheckExact(c_api_object)) {
        PyErr_SetNone(PyExc_ImportError);
        goto failure;
    }
    memcpy(_cffi_exports, PyCapsule_GetPointer(c_api_object, "cffi"),
           _CFFI_NUM_EXPORTS * sizeof(void *));

    Py_DECREF(module);
    Py_DECREF(c_api_object);
    return 0;

  failure:
    Py_XDECREF(module);
    Py_XDECREF(c_api_object);
    return -1;
}

#define _cffi_type(num) ((CTypeDescrObject *)PyList_GET_ITEM(_cffi_types, num))

/**********/



#include <wayland-client.h>
#include <wayland-server.h>
#include <wayland-version.h>


static int _cffi_const_WL_EVENT_READABLE(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(WL_EVENT_READABLE);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "WL_EVENT_READABLE", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return ((void)lib,0);
}

static int _cffi_const_WL_EVENT_WRITABLE(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(WL_EVENT_WRITABLE);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "WL_EVENT_WRITABLE", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_WL_EVENT_READABLE(lib);
}

static int _cffi_const_WL_EVENT_HANGUP(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(WL_EVENT_HANGUP);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "WL_EVENT_HANGUP", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_WL_EVENT_WRITABLE(lib);
}

static int _cffi_const_WL_EVENT_ERROR(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(WL_EVENT_ERROR);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "WL_EVENT_ERROR", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_WL_EVENT_HANGUP(lib);
}

static PyObject *
_cffi_f_wl_client_add_destroy_listener(PyObject *self, PyObject *args)
{
  struct wl_client * x0;
  struct wl_listener * x1;
  Py_ssize_t datasize;
  PyObject *arg0;
  PyObject *arg1;

  if (!PyArg_ParseTuple(args, "OO:wl_client_add_destroy_listener", &arg0, &arg1))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(0), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(0), arg0) < 0)
      return NULL;
  }

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(1), arg1, (char **)&x1);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x1 = alloca((size_t)datasize);
    memset((void *)x1, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x1, _cffi_type(1), arg1) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_client_add_destroy_listener(x0, x1); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_client_create(PyObject *self, PyObject *args)
{
  struct wl_display * x0;
  int x1;
  Py_ssize_t datasize;
  struct wl_client * result;
  PyObject *arg0;
  PyObject *arg1;

  if (!PyArg_ParseTuple(args, "OO:wl_client_create", &arg0, &arg1))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  x1 = _cffi_to_c_int(arg1, int);
  if (x1 == (int)-1 && PyErr_Occurred())
    return NULL;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_client_create(x0, x1); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(0));
}

static PyObject *
_cffi_f_wl_client_destroy(PyObject *self, PyObject *arg0)
{
  struct wl_client * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(0), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(0), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_client_destroy(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_client_flush(PyObject *self, PyObject *arg0)
{
  struct wl_client * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(0), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(0), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_client_flush(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_client_get_object(PyObject *self, PyObject *args)
{
  struct wl_client * x0;
  uint32_t x1;
  Py_ssize_t datasize;
  struct wl_resource * result;
  PyObject *arg0;
  PyObject *arg1;

  if (!PyArg_ParseTuple(args, "OO:wl_client_get_object", &arg0, &arg1))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(0), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(0), arg0) < 0)
      return NULL;
  }

  x1 = _cffi_to_c_int(arg1, uint32_t);
  if (x1 == (uint32_t)-1 && PyErr_Occurred())
    return NULL;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_client_get_object(x0, x1); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(4));
}

static PyObject *
_cffi_f_wl_display_add_socket(PyObject *self, PyObject *args)
{
  struct wl_display * x0;
  char const * x1;
  Py_ssize_t datasize;
  int result;
  PyObject *arg0;
  PyObject *arg1;

  if (!PyArg_ParseTuple(args, "OO:wl_display_add_socket", &arg0, &arg1))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(5), arg1, (char **)&x1);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x1 = alloca((size_t)datasize);
    memset((void *)x1, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x1, _cffi_type(5), arg1) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_display_add_socket(x0, x1); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int);
}

static PyObject *
_cffi_f_wl_display_connect(PyObject *self, PyObject *arg0)
{
  char const * x0;
  Py_ssize_t datasize;
  struct wl_display * result;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(5), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(5), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_display_connect(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(3));
}

static PyObject *
_cffi_f_wl_display_connect_to_fd(PyObject *self, PyObject *arg0)
{
  int x0;
  struct wl_display * result;

  x0 = _cffi_to_c_int(arg0, int);
  if (x0 == (int)-1 && PyErr_Occurred())
    return NULL;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_display_connect_to_fd(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(3));
}

static PyObject *
_cffi_f_wl_display_create(PyObject *self, PyObject *noarg)
{
  struct wl_display * result;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_display_create(); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  (void)noarg; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(3));
}

static PyObject *
_cffi_f_wl_display_create_queue(PyObject *self, PyObject *arg0)
{
  struct wl_display * x0;
  Py_ssize_t datasize;
  struct wl_event_queue * result;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_display_create_queue(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(6));
}

static PyObject *
_cffi_f_wl_display_destroy(PyObject *self, PyObject *arg0)
{
  struct wl_display * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_display_destroy(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_display_disconnect(PyObject *self, PyObject *arg0)
{
  struct wl_display * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_display_disconnect(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_display_dispatch(PyObject *self, PyObject *arg0)
{
  struct wl_display * x0;
  Py_ssize_t datasize;
  int result;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_display_dispatch(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int);
}

static PyObject *
_cffi_f_wl_display_dispatch_pending(PyObject *self, PyObject *arg0)
{
  struct wl_display * x0;
  Py_ssize_t datasize;
  int result;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_display_dispatch_pending(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int);
}

static PyObject *
_cffi_f_wl_display_dispatch_queue(PyObject *self, PyObject *args)
{
  struct wl_display * x0;
  struct wl_event_queue * x1;
  Py_ssize_t datasize;
  int result;
  PyObject *arg0;
  PyObject *arg1;

  if (!PyArg_ParseTuple(args, "OO:wl_display_dispatch_queue", &arg0, &arg1))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(6), arg1, (char **)&x1);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x1 = alloca((size_t)datasize);
    memset((void *)x1, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x1, _cffi_type(6), arg1) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_display_dispatch_queue(x0, x1); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int);
}

static PyObject *
_cffi_f_wl_display_flush(PyObject *self, PyObject *arg0)
{
  struct wl_display * x0;
  Py_ssize_t datasize;
  int result;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_display_flush(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int);
}

static PyObject *
_cffi_f_wl_display_get_event_loop(PyObject *self, PyObject *arg0)
{
  struct wl_display * x0;
  Py_ssize_t datasize;
  struct wl_event_loop * result;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_display_get_event_loop(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(7));
}

static PyObject *
_cffi_f_wl_display_get_fd(PyObject *self, PyObject *arg0)
{
  struct wl_display * x0;
  Py_ssize_t datasize;
  int result;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_display_get_fd(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int);
}

static PyObject *
_cffi_f_wl_display_get_serial(PyObject *self, PyObject *arg0)
{
  struct wl_display * x0;
  Py_ssize_t datasize;
  uint32_t result;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_display_get_serial(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, uint32_t);
}

static PyObject *
_cffi_f_wl_display_next_serial(PyObject *self, PyObject *arg0)
{
  struct wl_display * x0;
  Py_ssize_t datasize;
  uint32_t result;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_display_next_serial(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, uint32_t);
}

static PyObject *
_cffi_f_wl_display_roundtrip(PyObject *self, PyObject *arg0)
{
  struct wl_display * x0;
  Py_ssize_t datasize;
  int result;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_display_roundtrip(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int);
}

static PyObject *
_cffi_f_wl_display_run(PyObject *self, PyObject *arg0)
{
  struct wl_display * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_display_run(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_display_terminate(PyObject *self, PyObject *arg0)
{
  struct wl_display * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_display_terminate(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_event_loop_add_destroy_listener(PyObject *self, PyObject *args)
{
  struct wl_event_loop * x0;
  struct wl_listener * x1;
  Py_ssize_t datasize;
  PyObject *arg0;
  PyObject *arg1;

  if (!PyArg_ParseTuple(args, "OO:wl_event_loop_add_destroy_listener", &arg0, &arg1))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(7), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(7), arg0) < 0)
      return NULL;
  }

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(1), arg1, (char **)&x1);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x1 = alloca((size_t)datasize);
    memset((void *)x1, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x1, _cffi_type(1), arg1) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_event_loop_add_destroy_listener(x0, x1); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_event_loop_add_fd(PyObject *self, PyObject *args)
{
  struct wl_event_loop * x0;
  int x1;
  uint32_t x2;
  int(* x3)(int, uint32_t, void *);
  void * x4;
  Py_ssize_t datasize;
  struct wl_event_source * result;
  PyObject *arg0;
  PyObject *arg1;
  PyObject *arg2;
  PyObject *arg3;
  PyObject *arg4;

  if (!PyArg_ParseTuple(args, "OOOOO:wl_event_loop_add_fd", &arg0, &arg1, &arg2, &arg3, &arg4))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(7), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(7), arg0) < 0)
      return NULL;
  }

  x1 = _cffi_to_c_int(arg1, int);
  if (x1 == (int)-1 && PyErr_Occurred())
    return NULL;

  x2 = _cffi_to_c_int(arg2, uint32_t);
  if (x2 == (uint32_t)-1 && PyErr_Occurred())
    return NULL;

  x3 = (int(*)(int, uint32_t, void *))_cffi_to_c_pointer(arg3, _cffi_type(8));
  if (x3 == (int(*)(int, uint32_t, void *))NULL && PyErr_Occurred())
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(9), arg4, (char **)&x4);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x4 = alloca((size_t)datasize);
    memset((void *)x4, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x4, _cffi_type(9), arg4) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_event_loop_add_fd(x0, x1, x2, x3, x4); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(10));
}

static PyObject *
_cffi_f_wl_event_loop_add_idle(PyObject *self, PyObject *args)
{
  struct wl_event_loop * x0;
  void(* x1)(void *);
  void * x2;
  Py_ssize_t datasize;
  struct wl_event_source * result;
  PyObject *arg0;
  PyObject *arg1;
  PyObject *arg2;

  if (!PyArg_ParseTuple(args, "OOO:wl_event_loop_add_idle", &arg0, &arg1, &arg2))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(7), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(7), arg0) < 0)
      return NULL;
  }

  x1 = (void(*)(void *))_cffi_to_c_pointer(arg1, _cffi_type(11));
  if (x1 == (void(*)(void *))NULL && PyErr_Occurred())
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(9), arg2, (char **)&x2);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x2 = alloca((size_t)datasize);
    memset((void *)x2, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x2, _cffi_type(9), arg2) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_event_loop_add_idle(x0, x1, x2); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(10));
}

static PyObject *
_cffi_f_wl_event_loop_add_signal(PyObject *self, PyObject *args)
{
  struct wl_event_loop * x0;
  int x1;
  int(* x2)(int, void *);
  void * x3;
  Py_ssize_t datasize;
  struct wl_event_source * result;
  PyObject *arg0;
  PyObject *arg1;
  PyObject *arg2;
  PyObject *arg3;

  if (!PyArg_ParseTuple(args, "OOOO:wl_event_loop_add_signal", &arg0, &arg1, &arg2, &arg3))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(7), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(7), arg0) < 0)
      return NULL;
  }

  x1 = _cffi_to_c_int(arg1, int);
  if (x1 == (int)-1 && PyErr_Occurred())
    return NULL;

  x2 = (int(*)(int, void *))_cffi_to_c_pointer(arg2, _cffi_type(12));
  if (x2 == (int(*)(int, void *))NULL && PyErr_Occurred())
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(9), arg3, (char **)&x3);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x3 = alloca((size_t)datasize);
    memset((void *)x3, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x3, _cffi_type(9), arg3) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_event_loop_add_signal(x0, x1, x2, x3); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(10));
}

static PyObject *
_cffi_f_wl_event_loop_add_timer(PyObject *self, PyObject *args)
{
  struct wl_event_loop * x0;
  int(* x1)(void *);
  void * x2;
  Py_ssize_t datasize;
  struct wl_event_source * result;
  PyObject *arg0;
  PyObject *arg1;
  PyObject *arg2;

  if (!PyArg_ParseTuple(args, "OOO:wl_event_loop_add_timer", &arg0, &arg1, &arg2))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(7), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(7), arg0) < 0)
      return NULL;
  }

  x1 = (int(*)(void *))_cffi_to_c_pointer(arg1, _cffi_type(13));
  if (x1 == (int(*)(void *))NULL && PyErr_Occurred())
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(9), arg2, (char **)&x2);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x2 = alloca((size_t)datasize);
    memset((void *)x2, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x2, _cffi_type(9), arg2) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_event_loop_add_timer(x0, x1, x2); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(10));
}

static PyObject *
_cffi_f_wl_event_loop_create(PyObject *self, PyObject *noarg)
{
  struct wl_event_loop * result;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_event_loop_create(); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  (void)noarg; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(7));
}

static PyObject *
_cffi_f_wl_event_loop_destroy(PyObject *self, PyObject *arg0)
{
  struct wl_event_loop * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(7), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(7), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_event_loop_destroy(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_event_loop_dispatch(PyObject *self, PyObject *args)
{
  struct wl_event_loop * x0;
  int x1;
  Py_ssize_t datasize;
  int result;
  PyObject *arg0;
  PyObject *arg1;

  if (!PyArg_ParseTuple(args, "OO:wl_event_loop_dispatch", &arg0, &arg1))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(7), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(7), arg0) < 0)
      return NULL;
  }

  x1 = _cffi_to_c_int(arg1, int);
  if (x1 == (int)-1 && PyErr_Occurred())
    return NULL;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_event_loop_dispatch(x0, x1); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int);
}

static PyObject *
_cffi_f_wl_event_loop_dispatch_idle(PyObject *self, PyObject *arg0)
{
  struct wl_event_loop * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(7), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(7), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_event_loop_dispatch_idle(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_event_loop_get_fd(PyObject *self, PyObject *arg0)
{
  struct wl_event_loop * x0;
  Py_ssize_t datasize;
  int result;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(7), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(7), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_event_loop_get_fd(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int);
}

static PyObject *
_cffi_f_wl_event_queue_destroy(PyObject *self, PyObject *arg0)
{
  struct wl_event_queue * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(6), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(6), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_event_queue_destroy(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_event_source_check(PyObject *self, PyObject *arg0)
{
  struct wl_event_source * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(10), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(10), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_event_source_check(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_event_source_fd_update(PyObject *self, PyObject *args)
{
  struct wl_event_source * x0;
  uint32_t x1;
  Py_ssize_t datasize;
  int result;
  PyObject *arg0;
  PyObject *arg1;

  if (!PyArg_ParseTuple(args, "OO:wl_event_source_fd_update", &arg0, &arg1))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(10), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(10), arg0) < 0)
      return NULL;
  }

  x1 = _cffi_to_c_int(arg1, uint32_t);
  if (x1 == (uint32_t)-1 && PyErr_Occurred())
    return NULL;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_event_source_fd_update(x0, x1); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int);
}

static PyObject *
_cffi_f_wl_event_source_remove(PyObject *self, PyObject *arg0)
{
  struct wl_event_source * x0;
  Py_ssize_t datasize;
  int result;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(10), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(10), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_event_source_remove(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int);
}

static PyObject *
_cffi_f_wl_event_source_timer_update(PyObject *self, PyObject *args)
{
  struct wl_event_source * x0;
  int x1;
  Py_ssize_t datasize;
  int result;
  PyObject *arg0;
  PyObject *arg1;

  if (!PyArg_ParseTuple(args, "OO:wl_event_source_timer_update", &arg0, &arg1))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(10), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(10), arg0) < 0)
      return NULL;
  }

  x1 = _cffi_to_c_int(arg1, int);
  if (x1 == (int)-1 && PyErr_Occurred())
    return NULL;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_event_source_timer_update(x0, x1); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int);
}

static PyObject *
_cffi_f_wl_fixed_from_double(PyObject *self, PyObject *arg0)
{
  double x0;
  int32_t result;

  x0 = (double)_cffi_to_c_double(arg0);
  if (x0 == (double)-1 && PyErr_Occurred())
    return NULL;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_fixed_from_double(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int32_t);
}

static PyObject *
_cffi_f_wl_fixed_from_int(PyObject *self, PyObject *arg0)
{
  int x0;
  int32_t result;

  x0 = _cffi_to_c_int(arg0, int);
  if (x0 == (int)-1 && PyErr_Occurred())
    return NULL;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_fixed_from_int(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int32_t);
}

static PyObject *
_cffi_f_wl_fixed_to_double(PyObject *self, PyObject *arg0)
{
  int32_t x0;
  double result;

  x0 = _cffi_to_c_int(arg0, int32_t);
  if (x0 == (int32_t)-1 && PyErr_Occurred())
    return NULL;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_fixed_to_double(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_double(result);
}

static PyObject *
_cffi_f_wl_global_create(PyObject *self, PyObject *args)
{
  struct wl_display * x0;
  struct wl_interface const * x1;
  int x2;
  void * x3;
  void(* x4)(struct wl_client *, void *, uint32_t, uint32_t);
  Py_ssize_t datasize;
  struct wl_global * result;
  PyObject *arg0;
  PyObject *arg1;
  PyObject *arg2;
  PyObject *arg3;
  PyObject *arg4;

  if (!PyArg_ParseTuple(args, "OOOOO:wl_global_create", &arg0, &arg1, &arg2, &arg3, &arg4))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(14), arg1, (char **)&x1);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x1 = alloca((size_t)datasize);
    memset((void *)x1, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x1, _cffi_type(14), arg1) < 0)
      return NULL;
  }

  x2 = _cffi_to_c_int(arg2, int);
  if (x2 == (int)-1 && PyErr_Occurred())
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(9), arg3, (char **)&x3);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x3 = alloca((size_t)datasize);
    memset((void *)x3, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x3, _cffi_type(9), arg3) < 0)
      return NULL;
  }

  x4 = (void(*)(struct wl_client *, void *, uint32_t, uint32_t))_cffi_to_c_pointer(arg4, _cffi_type(15));
  if (x4 == (void(*)(struct wl_client *, void *, uint32_t, uint32_t))NULL && PyErr_Occurred())
    return NULL;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_global_create(x0, x1, x2, x3, x4); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(16));
}

static PyObject *
_cffi_f_wl_global_destroy(PyObject *self, PyObject *arg0)
{
  struct wl_global * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(16), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(16), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_global_destroy(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_list_remove(PyObject *self, PyObject *arg0)
{
  struct wl_list * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(17), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(17), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_list_remove(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_proxy_add_dispatcher(PyObject *self, PyObject *args)
{
  struct wl_proxy * x0;
  int(* x1)(void const *, void *, uint32_t, struct wl_message const *, union wl_argument *);
  void const * x2;
  void * x3;
  Py_ssize_t datasize;
  int result;
  PyObject *arg0;
  PyObject *arg1;
  PyObject *arg2;
  PyObject *arg3;

  if (!PyArg_ParseTuple(args, "OOOO:wl_proxy_add_dispatcher", &arg0, &arg1, &arg2, &arg3))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(18), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(18), arg0) < 0)
      return NULL;
  }

  x1 = (int(*)(void const *, void *, uint32_t, struct wl_message const *, union wl_argument *))_cffi_to_c_pointer(arg1, _cffi_type(19));
  if (x1 == (int(*)(void const *, void *, uint32_t, struct wl_message const *, union wl_argument *))NULL && PyErr_Occurred())
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(20), arg2, (char **)&x2);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x2 = alloca((size_t)datasize);
    memset((void *)x2, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x2, _cffi_type(20), arg2) < 0)
      return NULL;
  }

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(9), arg3, (char **)&x3);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x3 = alloca((size_t)datasize);
    memset((void *)x3, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x3, _cffi_type(9), arg3) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_proxy_add_dispatcher(x0, x1, x2, x3); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int);
}

static PyObject *
_cffi_f_wl_proxy_create(PyObject *self, PyObject *args)
{
  struct wl_proxy * x0;
  struct wl_interface const * x1;
  Py_ssize_t datasize;
  struct wl_proxy * result;
  PyObject *arg0;
  PyObject *arg1;

  if (!PyArg_ParseTuple(args, "OO:wl_proxy_create", &arg0, &arg1))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(18), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(18), arg0) < 0)
      return NULL;
  }

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(14), arg1, (char **)&x1);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x1 = alloca((size_t)datasize);
    memset((void *)x1, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x1, _cffi_type(14), arg1) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_proxy_create(x0, x1); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(18));
}

static PyObject *
_cffi_f_wl_proxy_destroy(PyObject *self, PyObject *arg0)
{
  struct wl_proxy * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(18), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(18), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_proxy_destroy(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_proxy_get_user_data(PyObject *self, PyObject *arg0)
{
  struct wl_proxy * x0;
  Py_ssize_t datasize;
  void * result;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(18), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(18), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_proxy_get_user_data(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(9));
}

static PyObject *
_cffi_f_wl_proxy_marshal_array(PyObject *self, PyObject *args)
{
  struct wl_proxy * x0;
  uint32_t x1;
  union wl_argument * x2;
  Py_ssize_t datasize;
  PyObject *arg0;
  PyObject *arg1;
  PyObject *arg2;

  if (!PyArg_ParseTuple(args, "OOO:wl_proxy_marshal_array", &arg0, &arg1, &arg2))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(18), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(18), arg0) < 0)
      return NULL;
  }

  x1 = _cffi_to_c_int(arg1, uint32_t);
  if (x1 == (uint32_t)-1 && PyErr_Occurred())
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(21), arg2, (char **)&x2);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x2 = alloca((size_t)datasize);
    memset((void *)x2, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x2, _cffi_type(21), arg2) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_proxy_marshal_array(x0, x1, x2); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_proxy_marshal_array_constructor(PyObject *self, PyObject *args)
{
  struct wl_proxy * x0;
  uint32_t x1;
  union wl_argument * x2;
  struct wl_interface const * x3;
  Py_ssize_t datasize;
  struct wl_proxy * result;
  PyObject *arg0;
  PyObject *arg1;
  PyObject *arg2;
  PyObject *arg3;

  if (!PyArg_ParseTuple(args, "OOOO:wl_proxy_marshal_array_constructor", &arg0, &arg1, &arg2, &arg3))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(18), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(18), arg0) < 0)
      return NULL;
  }

  x1 = _cffi_to_c_int(arg1, uint32_t);
  if (x1 == (uint32_t)-1 && PyErr_Occurred())
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(21), arg2, (char **)&x2);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x2 = alloca((size_t)datasize);
    memset((void *)x2, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x2, _cffi_type(21), arg2) < 0)
      return NULL;
  }

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(14), arg3, (char **)&x3);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x3 = alloca((size_t)datasize);
    memset((void *)x3, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x3, _cffi_type(14), arg3) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_proxy_marshal_array_constructor(x0, x1, x2, x3); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(18));
}

static PyObject *
_cffi_f_wl_proxy_set_user_data(PyObject *self, PyObject *args)
{
  struct wl_proxy * x0;
  void * x1;
  Py_ssize_t datasize;
  PyObject *arg0;
  PyObject *arg1;

  if (!PyArg_ParseTuple(args, "OO:wl_proxy_set_user_data", &arg0, &arg1))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(18), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(18), arg0) < 0)
      return NULL;
  }

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(9), arg1, (char **)&x1);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x1 = alloca((size_t)datasize);
    memset((void *)x1, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x1, _cffi_type(9), arg1) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_proxy_set_user_data(x0, x1); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_resource_add_destroy_listener(PyObject *self, PyObject *args)
{
  struct wl_resource * x0;
  struct wl_listener * x1;
  Py_ssize_t datasize;
  PyObject *arg0;
  PyObject *arg1;

  if (!PyArg_ParseTuple(args, "OO:wl_resource_add_destroy_listener", &arg0, &arg1))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(4), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(4), arg0) < 0)
      return NULL;
  }

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(1), arg1, (char **)&x1);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x1 = alloca((size_t)datasize);
    memset((void *)x1, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x1, _cffi_type(1), arg1) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_resource_add_destroy_listener(x0, x1); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_resource_create(PyObject *self, PyObject *args)
{
  struct wl_client * x0;
  struct wl_interface const * x1;
  int x2;
  uint32_t x3;
  Py_ssize_t datasize;
  struct wl_resource * result;
  PyObject *arg0;
  PyObject *arg1;
  PyObject *arg2;
  PyObject *arg3;

  if (!PyArg_ParseTuple(args, "OOOO:wl_resource_create", &arg0, &arg1, &arg2, &arg3))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(0), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(0), arg0) < 0)
      return NULL;
  }

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(14), arg1, (char **)&x1);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x1 = alloca((size_t)datasize);
    memset((void *)x1, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x1, _cffi_type(14), arg1) < 0)
      return NULL;
  }

  x2 = _cffi_to_c_int(arg2, int);
  if (x2 == (int)-1 && PyErr_Occurred())
    return NULL;

  x3 = _cffi_to_c_int(arg3, uint32_t);
  if (x3 == (uint32_t)-1 && PyErr_Occurred())
    return NULL;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_resource_create(x0, x1, x2, x3); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(4));
}

static PyObject *
_cffi_f_wl_resource_destroy(PyObject *self, PyObject *arg0)
{
  struct wl_resource * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(4), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(4), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_resource_destroy(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_resource_get_id(PyObject *self, PyObject *arg0)
{
  struct wl_resource * x0;
  Py_ssize_t datasize;
  uint32_t result;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(4), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(4), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_resource_get_id(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, uint32_t);
}

static PyObject *
_cffi_f_wl_resource_get_user_data(PyObject *self, PyObject *arg0)
{
  struct wl_resource * x0;
  Py_ssize_t datasize;
  void * result;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(4), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(4), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_resource_get_user_data(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(9));
}

static PyObject *
_cffi_f_wl_resource_get_version(PyObject *self, PyObject *arg0)
{
  struct wl_resource * x0;
  Py_ssize_t datasize;
  int result;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(4), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(4), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = wl_resource_get_version(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int);
}

static PyObject *
_cffi_f_wl_resource_post_event_array(PyObject *self, PyObject *args)
{
  struct wl_resource * x0;
  uint32_t x1;
  union wl_argument * x2;
  Py_ssize_t datasize;
  PyObject *arg0;
  PyObject *arg1;
  PyObject *arg2;

  if (!PyArg_ParseTuple(args, "OOO:wl_resource_post_event_array", &arg0, &arg1, &arg2))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(4), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(4), arg0) < 0)
      return NULL;
  }

  x1 = _cffi_to_c_int(arg1, uint32_t);
  if (x1 == (uint32_t)-1 && PyErr_Occurred())
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(21), arg2, (char **)&x2);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x2 = alloca((size_t)datasize);
    memset((void *)x2, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x2, _cffi_type(21), arg2) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_resource_post_event_array(x0, x1, x2); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_wl_resource_set_dispatcher(PyObject *self, PyObject *args)
{
  struct wl_resource * x0;
  int(* x1)(void const *, void *, uint32_t, struct wl_message const *, union wl_argument *);
  void const * x2;
  void * x3;
  void(* x4)(struct wl_resource *);
  Py_ssize_t datasize;
  PyObject *arg0;
  PyObject *arg1;
  PyObject *arg2;
  PyObject *arg3;
  PyObject *arg4;

  if (!PyArg_ParseTuple(args, "OOOOO:wl_resource_set_dispatcher", &arg0, &arg1, &arg2, &arg3, &arg4))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(4), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(4), arg0) < 0)
      return NULL;
  }

  x1 = (int(*)(void const *, void *, uint32_t, struct wl_message const *, union wl_argument *))_cffi_to_c_pointer(arg1, _cffi_type(19));
  if (x1 == (int(*)(void const *, void *, uint32_t, struct wl_message const *, union wl_argument *))NULL && PyErr_Occurred())
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(20), arg2, (char **)&x2);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x2 = alloca((size_t)datasize);
    memset((void *)x2, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x2, _cffi_type(20), arg2) < 0)
      return NULL;
  }

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(9), arg3, (char **)&x3);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x3 = alloca((size_t)datasize);
    memset((void *)x3, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x3, _cffi_type(9), arg3) < 0)
      return NULL;
  }

  x4 = (void(*)(struct wl_resource *))_cffi_to_c_pointer(arg4, _cffi_type(22));
  if (x4 == (void(*)(struct wl_resource *))NULL && PyErr_Occurred())
    return NULL;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { wl_resource_set_dispatcher(x0, x1, x2, x3, x4); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static int _cffi_const_WAYLAND_VERSION_MAJOR(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(WAYLAND_VERSION_MAJOR);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "WAYLAND_VERSION_MAJOR", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return ((void)lib,0);
}

static int _cffi_const_WAYLAND_VERSION_MICRO(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(WAYLAND_VERSION_MICRO);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "WAYLAND_VERSION_MICRO", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_WAYLAND_VERSION_MAJOR(lib);
}

static int _cffi_const_WAYLAND_VERSION_MINOR(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(WAYLAND_VERSION_MINOR);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "WAYLAND_VERSION_MINOR", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_WAYLAND_VERSION_MICRO(lib);
}

static void _cffi_check_struct_wl_interface(struct wl_interface *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  { char const * *tmp = &p->name; (void)tmp; }
  (void)((p->version) << 1);
  (void)((p->method_count) << 1);
  { struct wl_message const * *tmp = &p->methods; (void)tmp; }
  (void)((p->event_count) << 1);
  { struct wl_message const * *tmp = &p->events; (void)tmp; }
}
static PyObject *
_cffi_layout_struct_wl_interface(PyObject *self, PyObject *noarg)
{
  struct _cffi_aligncheck { char x; struct wl_interface y; };
  static Py_ssize_t nums[] = {
    sizeof(struct wl_interface),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct wl_interface, name),
    sizeof(((struct wl_interface *)0)->name),
    offsetof(struct wl_interface, version),
    sizeof(((struct wl_interface *)0)->version),
    offsetof(struct wl_interface, method_count),
    sizeof(((struct wl_interface *)0)->method_count),
    offsetof(struct wl_interface, methods),
    sizeof(((struct wl_interface *)0)->methods),
    offsetof(struct wl_interface, event_count),
    sizeof(((struct wl_interface *)0)->event_count),
    offsetof(struct wl_interface, events),
    sizeof(((struct wl_interface *)0)->events),
    -1
  };
  (void)self; /* unused */
  (void)noarg; /* unused */
  return _cffi_get_struct_layout(nums);
  /* the next line is not executed, but compiled */
  _cffi_check_struct_wl_interface(0);
}

static void _cffi_check_struct_wl_list(struct wl_list *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  { struct wl_list * *tmp = &p->prev; (void)tmp; }
  { struct wl_list * *tmp = &p->next; (void)tmp; }
}
static PyObject *
_cffi_layout_struct_wl_list(PyObject *self, PyObject *noarg)
{
  struct _cffi_aligncheck { char x; struct wl_list y; };
  static Py_ssize_t nums[] = {
    sizeof(struct wl_list),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct wl_list, prev),
    sizeof(((struct wl_list *)0)->prev),
    offsetof(struct wl_list, next),
    sizeof(((struct wl_list *)0)->next),
    -1
  };
  (void)self; /* unused */
  (void)noarg; /* unused */
  return _cffi_get_struct_layout(nums);
  /* the next line is not executed, but compiled */
  _cffi_check_struct_wl_list(0);
}

static void _cffi_check_struct_wl_listener(struct wl_listener *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  { struct wl_list *tmp = &p->link; (void)tmp; }
  { void(* *tmp)(struct wl_listener *, void *) = &p->notify; (void)tmp; }
}
static PyObject *
_cffi_layout_struct_wl_listener(PyObject *self, PyObject *noarg)
{
  struct _cffi_aligncheck { char x; struct wl_listener y; };
  static Py_ssize_t nums[] = {
    sizeof(struct wl_listener),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct wl_listener, link),
    sizeof(((struct wl_listener *)0)->link),
    offsetof(struct wl_listener, notify),
    sizeof(((struct wl_listener *)0)->notify),
    -1
  };
  (void)self; /* unused */
  (void)noarg; /* unused */
  return _cffi_get_struct_layout(nums);
  /* the next line is not executed, but compiled */
  _cffi_check_struct_wl_listener(0);
}

static void _cffi_check_struct_wl_message(struct wl_message *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  { char const * *tmp = &p->name; (void)tmp; }
  { char const * *tmp = &p->signature; (void)tmp; }
  { struct wl_interface const * * *tmp = &p->types; (void)tmp; }
}
static PyObject *
_cffi_layout_struct_wl_message(PyObject *self, PyObject *noarg)
{
  struct _cffi_aligncheck { char x; struct wl_message y; };
  static Py_ssize_t nums[] = {
    sizeof(struct wl_message),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct wl_message, name),
    sizeof(((struct wl_message *)0)->name),
    offsetof(struct wl_message, signature),
    sizeof(((struct wl_message *)0)->signature),
    offsetof(struct wl_message, types),
    sizeof(((struct wl_message *)0)->types),
    -1
  };
  (void)self; /* unused */
  (void)noarg; /* unused */
  return _cffi_get_struct_layout(nums);
  /* the next line is not executed, but compiled */
  _cffi_check_struct_wl_message(0);
}

static void _cffi_check_union_wl_argument(union wl_argument *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  (void)((p->i) << 1);
  (void)((p->u) << 1);
  (void)((p->f) << 1);
  { char const * *tmp = &p->s; (void)tmp; }
  { struct wl_object * *tmp = &p->o; (void)tmp; }
  (void)((p->n) << 1);
  { struct wl_array * *tmp = &p->a; (void)tmp; }
  (void)((p->h) << 1);
}
static PyObject *
_cffi_layout_union_wl_argument(PyObject *self, PyObject *noarg)
{
  struct _cffi_aligncheck { char x; union wl_argument y; };
  static Py_ssize_t nums[] = {
    sizeof(union wl_argument),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(union wl_argument, i),
    sizeof(((union wl_argument *)0)->i),
    offsetof(union wl_argument, u),
    sizeof(((union wl_argument *)0)->u),
    offsetof(union wl_argument, f),
    sizeof(((union wl_argument *)0)->f),
    offsetof(union wl_argument, s),
    sizeof(((union wl_argument *)0)->s),
    offsetof(union wl_argument, o),
    sizeof(((union wl_argument *)0)->o),
    offsetof(union wl_argument, n),
    sizeof(((union wl_argument *)0)->n),
    offsetof(union wl_argument, a),
    sizeof(((union wl_argument *)0)->a),
    offsetof(union wl_argument, h),
    sizeof(((union wl_argument *)0)->h),
    -1
  };
  (void)self; /* unused */
  (void)noarg; /* unused */
  return _cffi_get_struct_layout(nums);
  /* the next line is not executed, but compiled */
  _cffi_check_union_wl_argument(0);
}

static int _cffi_setup_custom(PyObject *lib)
{
  return _cffi_const_WAYLAND_VERSION_MINOR(lib);
}

static PyMethodDef _cffi_methods[] = {
  {"wl_client_add_destroy_listener", _cffi_f_wl_client_add_destroy_listener, METH_VARARGS, NULL},
  {"wl_client_create", _cffi_f_wl_client_create, METH_VARARGS, NULL},
  {"wl_client_destroy", _cffi_f_wl_client_destroy, METH_O, NULL},
  {"wl_client_flush", _cffi_f_wl_client_flush, METH_O, NULL},
  {"wl_client_get_object", _cffi_f_wl_client_get_object, METH_VARARGS, NULL},
  {"wl_display_add_socket", _cffi_f_wl_display_add_socket, METH_VARARGS, NULL},
  {"wl_display_connect", _cffi_f_wl_display_connect, METH_O, NULL},
  {"wl_display_connect_to_fd", _cffi_f_wl_display_connect_to_fd, METH_O, NULL},
  {"wl_display_create", _cffi_f_wl_display_create, METH_NOARGS, NULL},
  {"wl_display_create_queue", _cffi_f_wl_display_create_queue, METH_O, NULL},
  {"wl_display_destroy", _cffi_f_wl_display_destroy, METH_O, NULL},
  {"wl_display_disconnect", _cffi_f_wl_display_disconnect, METH_O, NULL},
  {"wl_display_dispatch", _cffi_f_wl_display_dispatch, METH_O, NULL},
  {"wl_display_dispatch_pending", _cffi_f_wl_display_dispatch_pending, METH_O, NULL},
  {"wl_display_dispatch_queue", _cffi_f_wl_display_dispatch_queue, METH_VARARGS, NULL},
  {"wl_display_flush", _cffi_f_wl_display_flush, METH_O, NULL},
  {"wl_display_get_event_loop", _cffi_f_wl_display_get_event_loop, METH_O, NULL},
  {"wl_display_get_fd", _cffi_f_wl_display_get_fd, METH_O, NULL},
  {"wl_display_get_serial", _cffi_f_wl_display_get_serial, METH_O, NULL},
  {"wl_display_next_serial", _cffi_f_wl_display_next_serial, METH_O, NULL},
  {"wl_display_roundtrip", _cffi_f_wl_display_roundtrip, METH_O, NULL},
  {"wl_display_run", _cffi_f_wl_display_run, METH_O, NULL},
  {"wl_display_terminate", _cffi_f_wl_display_terminate, METH_O, NULL},
  {"wl_event_loop_add_destroy_listener", _cffi_f_wl_event_loop_add_destroy_listener, METH_VARARGS, NULL},
  {"wl_event_loop_add_fd", _cffi_f_wl_event_loop_add_fd, METH_VARARGS, NULL},
  {"wl_event_loop_add_idle", _cffi_f_wl_event_loop_add_idle, METH_VARARGS, NULL},
  {"wl_event_loop_add_signal", _cffi_f_wl_event_loop_add_signal, METH_VARARGS, NULL},
  {"wl_event_loop_add_timer", _cffi_f_wl_event_loop_add_timer, METH_VARARGS, NULL},
  {"wl_event_loop_create", _cffi_f_wl_event_loop_create, METH_NOARGS, NULL},
  {"wl_event_loop_destroy", _cffi_f_wl_event_loop_destroy, METH_O, NULL},
  {"wl_event_loop_dispatch", _cffi_f_wl_event_loop_dispatch, METH_VARARGS, NULL},
  {"wl_event_loop_dispatch_idle", _cffi_f_wl_event_loop_dispatch_idle, METH_O, NULL},
  {"wl_event_loop_get_fd", _cffi_f_wl_event_loop_get_fd, METH_O, NULL},
  {"wl_event_queue_destroy", _cffi_f_wl_event_queue_destroy, METH_O, NULL},
  {"wl_event_source_check", _cffi_f_wl_event_source_check, METH_O, NULL},
  {"wl_event_source_fd_update", _cffi_f_wl_event_source_fd_update, METH_VARARGS, NULL},
  {"wl_event_source_remove", _cffi_f_wl_event_source_remove, METH_O, NULL},
  {"wl_event_source_timer_update", _cffi_f_wl_event_source_timer_update, METH_VARARGS, NULL},
  {"wl_fixed_from_double", _cffi_f_wl_fixed_from_double, METH_O, NULL},
  {"wl_fixed_from_int", _cffi_f_wl_fixed_from_int, METH_O, NULL},
  {"wl_fixed_to_double", _cffi_f_wl_fixed_to_double, METH_O, NULL},
  {"wl_global_create", _cffi_f_wl_global_create, METH_VARARGS, NULL},
  {"wl_global_destroy", _cffi_f_wl_global_destroy, METH_O, NULL},
  {"wl_list_remove", _cffi_f_wl_list_remove, METH_O, NULL},
  {"wl_proxy_add_dispatcher", _cffi_f_wl_proxy_add_dispatcher, METH_VARARGS, NULL},
  {"wl_proxy_create", _cffi_f_wl_proxy_create, METH_VARARGS, NULL},
  {"wl_proxy_destroy", _cffi_f_wl_proxy_destroy, METH_O, NULL},
  {"wl_proxy_get_user_data", _cffi_f_wl_proxy_get_user_data, METH_O, NULL},
  {"wl_proxy_marshal_array", _cffi_f_wl_proxy_marshal_array, METH_VARARGS, NULL},
  {"wl_proxy_marshal_array_constructor", _cffi_f_wl_proxy_marshal_array_constructor, METH_VARARGS, NULL},
  {"wl_proxy_set_user_data", _cffi_f_wl_proxy_set_user_data, METH_VARARGS, NULL},
  {"wl_resource_add_destroy_listener", _cffi_f_wl_resource_add_destroy_listener, METH_VARARGS, NULL},
  {"wl_resource_create", _cffi_f_wl_resource_create, METH_VARARGS, NULL},
  {"wl_resource_destroy", _cffi_f_wl_resource_destroy, METH_O, NULL},
  {"wl_resource_get_id", _cffi_f_wl_resource_get_id, METH_O, NULL},
  {"wl_resource_get_user_data", _cffi_f_wl_resource_get_user_data, METH_O, NULL},
  {"wl_resource_get_version", _cffi_f_wl_resource_get_version, METH_O, NULL},
  {"wl_resource_post_event_array", _cffi_f_wl_resource_post_event_array, METH_VARARGS, NULL},
  {"wl_resource_set_dispatcher", _cffi_f_wl_resource_set_dispatcher, METH_VARARGS, NULL},
  {"_cffi_layout_struct_wl_interface", _cffi_layout_struct_wl_interface, METH_NOARGS, NULL},
  {"_cffi_layout_struct_wl_list", _cffi_layout_struct_wl_list, METH_NOARGS, NULL},
  {"_cffi_layout_struct_wl_listener", _cffi_layout_struct_wl_listener, METH_NOARGS, NULL},
  {"_cffi_layout_struct_wl_message", _cffi_layout_struct_wl_message, METH_NOARGS, NULL},
  {"_cffi_layout_union_wl_argument", _cffi_layout_union_wl_argument, METH_NOARGS, NULL},
  {"_cffi_setup", _cffi_setup, METH_VARARGS, NULL},
  {NULL, NULL, 0, NULL}    /* Sentinel */
};

#if PY_MAJOR_VERSION >= 3

static struct PyModuleDef _cffi_module_def = {
  PyModuleDef_HEAD_INIT,
  "_pywayland_cffi_3b32c43dx6c4732eb",
  NULL,
  -1,
  _cffi_methods,
  NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC
PyInit__pywayland_cffi_3b32c43dx6c4732eb(void)
{
  PyObject *lib;
  lib = PyModule_Create(&_cffi_module_def);
  if (lib == NULL)
    return NULL;
  if (_cffi_const_WL_EVENT_ERROR(lib) < 0 || _cffi_init() < 0) {
    Py_DECREF(lib);
    return NULL;
  }
  return lib;
}

#else

PyMODINIT_FUNC
init_pywayland_cffi_3b32c43dx6c4732eb(void)
{
  PyObject *lib;
  lib = Py_InitModule("_pywayland_cffi_3b32c43dx6c4732eb", _cffi_methods);
  if (lib == NULL)
    return;
  if (_cffi_const_WL_EVENT_ERROR(lib) < 0 || _cffi_init() < 0)
    return;
  return;
}

#endif
