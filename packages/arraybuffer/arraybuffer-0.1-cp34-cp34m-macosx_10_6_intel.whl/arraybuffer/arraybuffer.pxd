cimport cython

ctypedef union data_ptr:
    char *char
    short *short
    int *int
    long *long
    float *float
    double *double
    long double *ldouble
    unsigned char *uchar
    unsigned short *ushort
    unsigned int *uint
    unsigned long *ulong


@cython.final
cdef public class arraybuffer_dsc[object arraybuffer_dscObject, type arraybuffer_dscType]:
    cdef int ndim
    cdef Py_ssize_t len
    cdef Py_ssize_t *shape
    cdef Py_ssize_t *strides
    cdef Py_ssize_t itemsize
    cdef int order
    cdef bytes format
    cdef bint dtype_is_object
    
    cpdef arraybuffer arraybuffer(self, bint zero=*)
    

@cython.final
cdef public class arraybuffer[object arraybufferObject, type arraybufferType]:
    cdef arraybuffer_dsc dsc
    cdef data_ptr data

