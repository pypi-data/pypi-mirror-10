
#cython: boundscheck=False
#cython: wraparound=False
#cython: nonecheck=False
#cython: language_level=3
#cython: embedsignature=True

cimport cython

#from cython.view cimport memoryview

cdef extern from "stdlib.h":
    void *malloc(size_t) nogil
    void free(void *) nogil
    void *memcpy(void *dest, void *src, size_t n) nogil
    void *memset(void *dest, int c, size_t n)
    void *strcpy(char *dest, char *src) nogil

cdef extern from "Python.h":
    ctypedef struct PyObject
    #ctypedef struct Py_buffer
    #ctypedef Py_ssize_t

    int PyObject_GetBuffer(object, Py_buffer *, int) except -1
    void PyObject_ReleaseBuffer(Py_buffer *)

    PyObject *Py_None
    
    void Py_INCREF(PyObject *)
    void Py_DECREF(PyObject *)
    
    char* PyBytes_AS_STRING(object)

    void* PyMem_Malloc(size_t)
    void PyMem_Free(void *)
    void* PyMem_MALLOC(size_t)
    void PyMem_FREE(void *)

    cdef enum:
        PyBUF_C_CONTIGUOUS,
        PyBUF_F_CONTIGUOUS,
        PyBUF_ANY_CONTIGUOUS
        PyBUF_FORMAT
        PyBUF_WRITABLE
        PyBUF_STRIDES
        PyBUF_INDIRECT
        PyBUF_RECORDS

cdef dict dtype2size = {
    b'c': int(sizeof(cython.char)),
    b'B': int(sizeof(cython.uchar)),
    b'h': int(sizeof(cython.short)),
    b'H': int(sizeof(cython.ushort)),
    b'i': int(sizeof(cython.int)),
    b'I': int(sizeof(cython.uint)),
    b'l': int(sizeof(cython.long)),
    b'L': int(sizeof(cython.ulong)),
    b'n': int(sizeof(cython.Py_ssize_t)),
    b'N': int(sizeof(cython.size_t)),
    b'q': int(sizeof(cython.longlong)),
    b'Q': int(sizeof(cython.ulonglong)),
    b'd': int(sizeof(cython.double)),
    b'D': int(sizeof(cython.longdouble)),
    b'f': int(sizeof(cython.float)),
    b'P': int(sizeof(cython.pvoid)),
    b'O': int(sizeof(cython.pvoid)),
}

cdef dict dtype2typechar = {
    b'c': 'i',
    b'B': 'u',
    b'h': 'i',
    b'H': 'u',
    b'i': 'i',
    b'I': 'u',
    b'l': 'i',
    b'L': 'u',
    b'n': 'i',
    b'N': 'i',
    b'q': 'i',
    b'Q': 'u',
    b'd': 'f',
    b'D': 'f',
    b'f': 'f',
    b'P': 'O',
    b'O': 'O',
}

cdef public class arraybuffer_dsc[object arraybuffer_dscObject, type arraybuffer_dscType]:

    property shape:
        def __get__(self):
            cdef arraybuffer_dsc dsc
            cdef int i
            
            if type(self) is arraybuffer_dsc:
                dsc = <arraybuffer_dsc>self
                return tuple(dsc.shape[i] for i in range(dsc.ndim))
            else:
                return self

    property format:
        def __get__(self):
            cdef arraybuffer_dsc dsc
            
            if type(self) is arraybuffer_dsc:
                dsc = <arraybuffer_dsc>self
                return dsc.format
            else:
                return self

    property order:
        def __get__(self):
            cdef arraybuffer_dsc dsc
            
            if type(self) is arraybuffer_dsc:
                dsc = <arraybuffer_dsc>self
                if dsc.order == 1:
                    return b'C'
                elif dsc.order == 2:
                    return b'F'
                else:
                    return None
            else:
                return self

    property itemsize:
        def __get__(self):
            cdef arraybuffer_dsc dsc
            
            if type(self) is arraybuffer_dsc:
                dsc = <arraybuffer_dsc>self
                return dsc.itemsize
            else:
                return self
                
    def __cinit__(arraybuffer_dsc dsc, shape, format, order=b'C'):
        cdef Py_ssize_t i, dim
        cdef Py_ssize_t *_shape
        cdef Py_ssize_t *_strides
        cdef Py_ssize_t _stride

        if shape is None or len(shape) == 0:
            raise ValueError("Invalid shape: %s" % shape)
        elif type(shape) is not tuple:
            shape = tuple(shape)

        dsc.ndim = <int>len(shape)

        if type(format) is unicode:
            format = (<unicode>format).encode('ASCII')

        if format is not None:
            dtype = format[0:1]

            dsc.itemsize = dtype2size.get(dtype, -1)

            if dsc.itemsize < 0:
                raise ValueError("Invalid data type in format: " + dtype)

            if dtype == b'O':
                dsc.dtype_is_object = 1
            else:
                dsc.dtype_is_object = 0

            dsc.format = format
        else:
            raise ValueError("Invalid format: " + format)        

        if not dsc.ndim:
            raise ValueError("Empty shape tuple for arraybuffer_dsc")

        _shape = <Py_ssize_t *> PyMem_Malloc(sizeof(Py_ssize_t)*dsc.ndim*2)
        _strides = _shape + dsc.ndim

        if not _shape:
            raise MemoryError("Unable to allocate shape and strides.")

        for i, dim in enumerate(shape):
            if dim <= 0:
                raise ValueError("Invalid shape in axis %d: %d." % (i, dim))
            _shape[i] = dim

        if type(order) is unicode:
            order = (<unicode>order).encode('ASCII')
        if order == b"F":
            dsc.order = 2
            _stride = dsc.itemsize
            for i in range(dsc.ndim):
                _strides[i] = _stride
                _stride *= _shape[i]
            dsc.len = _stride
        elif order == b"C":
            dsc.order = 1
            _stride = dsc.itemsize
            for i in range(dsc.ndim - 1, -1, -1):
                _strides[i] = _stride
                _stride *= _shape[i]
            dsc.len = _stride
        else:
            raise ValueError("Invalid order, expected 'C' or 'F', got %r" % order)

        dsc.shape = _shape
        dsc.strides = _strides

    def __repr__(self):
        text =  '<arraybuffer_dsc ndim=%s itemsize=%s shape=(' % (self.ndim, self.itemsize)
        for i in range(self.ndim):
            text += str(self.shape[i]) + ','
        text += ') format="%s"' % self.format
        if self.order == 1:
            text += ' order="C"'
        elif self.order == 2:
            text += ' order="F"'
        text += '>'
        return text
        
    def __dealloc__(self):
        PyMem_Free(self.shape)
        
    def clone(self):
        cdef Py_ssize_t nw
        cdef PyObject **p
        cdef Py_ssize_t *_shape
        cdef Py_ssize_t *_strides

        cdef arraybuffer_dsc dsc = <arraybuffer_dsc>arraybuffer_dsc.__new__(arraybuffer_dsc)
    
        dsc.ndim = self.ndim
        dsc.format = self.format
        dsc.itemsize = self.itemsize
    
        nw = sizeof(Py_ssize_t)*self.ndim*2
        _shape = <Py_ssize_t *> PyMem_Malloc(nw)

        if not _shape:
            raise MemoryError("Unable to allocate shape and strides.")

        _strides = _shape + self.ndim
        memcpy(_shape, &self.shape, nw)

        dsc.order = self.order
        dsc.len = self.len        

        dsc.shape = _shape
        dsc.strides = _strides
        
        dsc.dtype_is_object = self.dtype_is_object
        return dsc
        
    cpdef arraybuffer arraybuffer(self, bint zero=0):
        return arraybuffer(self, zero)
                            
cdef public class arraybuffer[object arraybufferObject, type arraybufferType]:

    property shape:
        def __get__(self):
            cdef arraybuffer_dsc dsc
            cdef int i
            
            if type(self) is arraybuffer:
                dsc = (<arraybuffer>self).dsc
                return tuple(dsc.shape[i] for i in range(dsc.ndim))
            else:
                return self

    property format:
        def __get__(self):
            cdef arraybuffer_dsc dsc
            
            if type(self) is arraybuffer:
                dsc = (<arraybuffer>self).dsc
                return dsc.format
            else:
                return self

    property order:
        def __get__(self):
            cdef arraybuffer_dsc dsc
            
            if type(self) is arraybuffer:
                dsc = (<arraybuffer>self).dsc
                if dsc.order == 1:
                    return b'C'
                elif dsc.order == 2:
                    return b'F'
                else:
                    None
            else:
                return self

    property itemsize:
        def __get__(self):
            cdef arraybuffer_dsc dsc
            
            if type(self) is arraybuffer:
                dsc = (<arraybuffer>self).dsc
                return dsc.itemsize
            else:
                return self

    def __cinit__(arraybuffer ab, arraybuffer_dsc dsc, bint zero=0):
        cdef Py_ssize_t i, n
        cdef PyObject **p

        ab.dsc = dsc

        ab.data.char = <char *>malloc(dsc.len)
        if not ab.data.char:
            raise MemoryError("Unable to allocate array data.")

        if dsc.dtype_is_object:
            p = <PyObject **>ab.data.char
            n = dsc.len / dsc.itemsize
            for i in range(n):
                p[i] = Py_None
                Py_INCREF(Py_None)
        elif zero:
            memset(<void*>ab.data.char, dsc.len, 0)

    def __getbuffer__(self, Py_buffer *info, int flags):
        cdef int bufmode = -1
        cdef arraybuffer_dsc dsc = self.dsc
        
        if dsc.order == 1:
            bufmode = PyBUF_C_CONTIGUOUS | PyBUF_ANY_CONTIGUOUS
        elif dsc.order == 2:
            bufmode = PyBUF_F_CONTIGUOUS | PyBUF_ANY_CONTIGUOUS
        if not (flags & bufmode):
            raise ValueError("Can only create a buffer that is contiguous in memory.")

        info.ndim = dsc.ndim
        info.shape = dsc.shape
        info.strides = dsc.strides
        info.len = dsc.len
        info.itemsize = dsc.itemsize

        info.suboffsets = NULL

        info.format = PyBytes_AS_STRING(<object>dsc.format)

        info.buf = self.data.char
        info.readonly = 0

        info.obj = self
        
    def __dealloc__(self):
        cdef Py_ssize_t i, n
        cdef PyObject **p
        
        if self.dsc.dtype_is_object:            
            p = <PyObject **>self.data.char
            n = self.dsc.len / self.dsc.itemsize
            for i in range(n):
                Py_DECREF(p[i])
                
        free(self.data.char)

    def __repr__(self):
        text =  '<arraybuffer ndim=%s itemsize=%s shape=(' % (self.dsc.ndim, self.dsc.itemsize)
        for i in range(self.dsc.ndim):
            text += str(self.dsc.shape[i]) + ','
        text += ') format="%s" len=%s' % (self.dsc.format, self.dsc.len)
        if self.dsc.order == 1:
            text += ' order="C"'
        elif self.dsc.order == 2:
            text += ' order="F"'
        text += '>'
        return text

    def clone(self):
        cdef int i
        cdef Py_ssize_t n
        cdef PyObject **p
    
        cdef arraybuffer ab = arraybuffer(self.dsc, 0)

        memcpy(ab.data.char, self.data.char, self.dsc.len)
        
        if ab.dsc.dtype_is_object:
            p = <PyObject **>ab.data.char
            n = ab.dsc.len / sizeof(PyObject*)
            for i in range(n):
                Py_INCREF(p[i])

        return ab

    def clear(self):        
        memset(self.data.char, 0, self.dsc.len)
        
    def __array_interface__(self):
        cdef char dt_char
        dt_char = self.dsc.format[0]        
        d =  { 'shape': self.shape, 
               'typestr': '|'+dtype2typechar(dt_char)+dtype2size(dt_char),
               'version': 3,
               'strides': self.strides,
               'data': (<unsigned int>self.data.char, False)
             }
        return d


