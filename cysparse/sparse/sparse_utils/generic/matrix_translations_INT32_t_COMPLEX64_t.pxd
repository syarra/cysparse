"""
Diverse utilities to translate one matrix format into another.

"""
from cysparse.types.cysparse_types cimport *

cdef csr_to_csc_kernel_INT32_t_COMPLEX64_t(INT32_t nrow, INT32_t ncol, INT32_t nnz,
                                      INT32_t * csr_ind, INT32_t * csr_col, COMPLEX64_t * csr_val,
                                      INT32_t * csc_ind, INT32_t * csc_row, COMPLEX64_t * csc_val)

cdef csc_to_csr_kernel_INT32_t_COMPLEX64_t(INT32_t nrow, INT32_t ncol, INT32_t nnz,
                                      INT32_t * csc_ind, INT32_t * csc_row, COMPLEX64_t * csc_val,
                                      INT32_t * csr_ind, INT32_t * csr_col, COMPLEX64_t * csr_val)