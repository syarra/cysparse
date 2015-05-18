"""
This file contains the basic types used in CySparse.

CySparse allows you to dynamically type your matrices. This is not obvious to code in C or Cython. We do this by
generating different source code files for the different types. Sometimes, we need to test at compile time what type
we use (for instance to generate the right type of NumPy matrices). These tests are hard-coded.

You can find such places in the template files by looking for the comment '# EXPLICIT TYPE TESTS'.

Types are given by XXX_t.

For each type XXX_t, there is a corresponding:

 - XXX_T : an enum constant
 - XXX_t_BIT : numbers of bits for this type

Although we use NumPy compatible types, this will is not and should not be dependent on NumPy.

"""

#################################################################################################
#                                 *** BASIC ABSOLUTE TYPES ***
#
# INT32_t
# UINT32_t
# INT64_t
# UINT64_t
# FLOAT32_t
# FLOAT64_t
# COMPLEX64_t
# COMPLEX128_t
#
# DO NOT CHANGE THIS (except if you **really** know what you are doing)
#
# We bring your attention to the following points:
#
# 1. A complex type that is at the same type fully compatible with NumPy, Python and Cython doesn't exist yet.
# 2. For the complex types, we use C99. These types are compatible with NumPy and we cast them for Python.
# 3. The code is specialized at some place. You can track those places by looking for the comment '# EXPLICIT TYPE TESTS'
#    If you want to remove or add a new type, you'll have to manually change the code at those places.
#    In short: DON'T CHANGE THE BASIC TYPES.
#
#################################################################################################

cpdef enum CySparseType:
    INT32_T = 0
    UINT32_T = 1
    INT64_T = 2
    UINT64_T = 3
    FLOAT32_T = 4
    FLOAT64_T = 5
    COMPLEX64_T = 6
    COMPLEX128_T = 7

ctypedef int INT32_t
ctypedef unsigned int UINT32_t
ctypedef long INT64_t
ctypedef unsigned long UINT64_t

ctypedef float FLOAT32_t
ctypedef double FLOAT64_t

ctypedef float complex COMPLEX64_t
ctypedef double complex COMPLEX128_t

# elements that behave like integers
INTEGER_ELEMENT_TYPES = [INT32_T, UINT32_T, INT64_T, UINT64_T]
# elements that behave like floats
FLOAT_ELEMENT_TYPES = [FLOAT32_T, FLOAT64_T]
# elements that behave like complex numbers (we only consider complex floats)
COMPLEX_ELEMENT_TYPES = [COMPLEX64_T, COMPLEX128_T]

#################################################################################################
#                                 *** BASIC TYPES SIZES ***
#################################################################################################
cdef extern from "limits.h":
    enum:
        CHAR_BIT

# in bits
cdef enum CySparseTypeBitSize:
    INT32_t_BIT = sizeof(INT32_t) * CHAR_BIT
    UINT32_t_BIT = sizeof(INT32_t) * CHAR_BIT
    INT64_t_BIT = sizeof(INT64_t) * CHAR_BIT
    UINT64_t_BIT = sizeof(UINT64_t) * CHAR_BIT
    FLOAT32_t_BIT = sizeof(FLOAT32_t) * CHAR_BIT
    FLOAT64_t_BIT = sizeof(FLOAT64_t) * CHAR_BIT
    COMPLEX64_t_BIT = sizeof(COMPLEX64_t) * CHAR_BIT
    COMPLEX128_t_BIT = sizeof(COMPLEX128_t) * CHAR_BIT

#################################################################################################
#                                 *** SPARSE MATRIX TYPES ***
#################################################################################################
cdef struct CPType:
    CySparseType dtype
    CySparseType itype