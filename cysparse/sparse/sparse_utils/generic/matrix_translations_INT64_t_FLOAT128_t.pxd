"""
Diverse utilities to translate one matrix format into another.

"""
from cysparse.cysparse_types.cysparse_types cimport *

cdef csr_to_csc_kernel_INT64_t_FLOAT128_t(INT64_t nrow, INT64_t ncol, INT64_t nnz,
                                      INT64_t * csr_ind, INT64_t * csr_col, FLOAT128_t * csr_val,
                                      INT64_t * csc_ind, INT64_t * csc_row, FLOAT128_t * csc_val)

cdef csc_to_csr_kernel_INT64_t_FLOAT128_t(INT64_t nrow, INT64_t ncol, INT64_t nnz,
                                      INT64_t * csc_ind, INT64_t * csc_row, FLOAT128_t * csc_val,
                                      INT64_t * csr_ind, INT64_t * csr_col, FLOAT128_t * csr_val)