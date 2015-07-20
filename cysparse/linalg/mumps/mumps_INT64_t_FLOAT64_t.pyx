from cysparse.sparse.ll_mat_matrices.ll_mat_INT64_t_FLOAT64_t cimport LLSparseMatrix_INT64_t_FLOAT64_t
from cysparse.sparse.csc_mat_matrices.csc_mat_INT64_t_FLOAT64_t cimport CSCSparseMatrix_INT64_t_FLOAT64_t

from cpython.mem cimport PyMem_Malloc, PyMem_Realloc, PyMem_Free
from cpython cimport Py_INCREF, Py_DECREF

import numpy as np
cimport numpy as cnp

from libc.stdint cimport int64_t
from libc.string cimport strncpy

cnp.import_array()


cdef extern from "mumps_c_types.h":

    ctypedef int        MUMPS_INT
    ctypedef int64_t  MUMPS_INT8 # warning: mumps uses "stdint.h" which might define int64_t as long long...

    ctypedef float      SMUMPS_COMPLEX
    ctypedef float      SMUMPS_REAL

    ctypedef double     DMUMPS_COMPLEX
    ctypedef double     DMUMPS_REAL

    ctypedef struct mumps_complex:
        float r,i

    ctypedef mumps_complex  CMUMPS_COMPLEX
    ctypedef float          CMUMPS_REAL

    ctypedef struct mumps_double_complex:
        double r, i

    ctypedef mumps_double_complex  ZMUMPS_COMPLEX
    ctypedef double                ZMUMPS_REAL

cdef extern from "dmumps_c.h":
    ctypedef struct DMUMPS_STRUC_C:
        MUMPS_INT      sym, par, job
        MUMPS_INT      comm_fortran    # Fortran communicator
        MUMPS_INT      icntl[40]
        MUMPS_INT      keep[500]
        DMUMPS_REAL    cntl[15]
        DMUMPS_REAL    dkeep[130];
        MUMPS_INT8     keep8[150];
        MUMPS_INT      n

        # used in matlab interface to decide if we
        # free + malloc when we have large variation
        MUMPS_INT      nz_alloc

        # Assembled entry
        MUMPS_INT      nz
        MUMPS_INT      *irn
        MUMPS_INT      *jcn
        DMUMPS_COMPLEX *a

        # Distributed entry
        MUMPS_INT      nz_loc
        MUMPS_INT      *irn_loc
        MUMPS_INT      *jcn_loc
        DMUMPS_COMPLEX *a_loc

        # Element entry
        MUMPS_INT      nelt
        MUMPS_INT      *eltptr
        MUMPS_INT      *eltvar
        DMUMPS_COMPLEX *a_elt

        # Ordering, if given by user
        MUMPS_INT      *perm_in

        # Orderings returned to user
        MUMPS_INT      *sym_perm    # symmetric permutation
        MUMPS_INT      *uns_perm    # column permutation

        # Scaling (input only in this version)
        DMUMPS_REAL    *colsca
        DMUMPS_REAL    *rowsca
        MUMPS_INT colsca_from_mumps;
        MUMPS_INT rowsca_from_mumps;


        # RHS, solution, ouptput data and statistics
        DMUMPS_COMPLEX *rhs
        DMUMPS_COMPLEX *redrhs
        DMUMPS_COMPLEX *rhs_sparse
        DMUMPS_COMPLEX *sol_loc
        MUMPS_INT      *irhs_sparse
        MUMPS_INT      *irhs_ptr
        MUMPS_INT      *isol_loc
        MUMPS_INT      nrhs, lrhs, lredrhs, nz_rhs, lsol_loc
        MUMPS_INT      schur_mloc, schur_nloc, schur_lld
        MUMPS_INT      mblock, nblock, nprow, npcol
        MUMPS_INT      info[40]
        MUMPS_INT      infog[40]
        DMUMPS_REAL    rinfo[40]
        DMUMPS_REAL    rinfog[40]

        # Null space
        MUMPS_INT      deficiency
        MUMPS_INT      *pivnul_list
        MUMPS_INT      *mapping

        # Schur
        MUMPS_INT      size_schur
        MUMPS_INT      *listvar_schur
        DMUMPS_COMPLEX *schur

        # Internal parameters
        MUMPS_INT      instance_number
        DMUMPS_COMPLEX *wk_user

        char *version_number
        # For out-of-core
        char *ooc_tmpdir
        char *ooc_prefix
        # To save the matrix in matrix market format
        char *write_problem
        MUMPS_INT      lwk_user

    cdef void dmumps_c(DMUMPS_STRUC_C *)






cdef class MumpsContext_INT64_t_FLOAT64_t:
    """
    Mumps Context.

    This version **only** deals with ``LLSparseMatrix_INT64_t_FLOAT64_t`` objects.

    We follow the common use of Mumps. In particular, we use the same names for the methods of this
    class as their corresponding counter-parts in Mumps.
    """

    def __cinit__(self, LLSparseMatrix_INT64_t_FLOAT64_t A, comm_fortran=-987654):
        """
        Args:
            A: A :class:`LLSparseMatrix_INT64_t_FLOAT64_t` object.

        Warning:
            The solver takes a "snapshot" of the matrix ``A``, i.e. the results given by the solver are only
            valid for the matrix given. If the matrix ``A`` changes aferwards, the results given by the solver won't
            reflect this change.

        """
        self.A = A
        Py_INCREF(self.A)  # increase ref to object to avoid the user deleting it explicitly or implicitly

        self.nrow = A.nrow
        self.ncol = A.ncol

        self.nnz = self.A.nnz

        # MUMPS
        self.ob.job = -1
        self.ob.sym = self.A.is_symmetric
        self.ob.par = 1

        self.ob.comm_fortran = comm_fortran

        dmumps_c(&self.ob)


    def __dealloc__(self):
        pass

    ####################################################################################################################
    # Properties
    ####################################################################################################################
    ######################################### COMMON Properties ########################################################
    property sym:
        def __get__(self): return self.ob.sym
        def __set__(self, value): self.ob.sym = value
    property par:
        def __get__(self): return self.ob.par
        def __set__(self, value): self.ob.par = value
    property job:
        def __get__(self): return self.ob.job
        def __set__(self, value): self.ob.job = value

    property comm_fortran:
        def __get__(self): return self.ob.comm_fortran
        def __set__(self, value): self.ob.comm_fortran = value

    property icntl:
        def __get__(self):
            cdef MUMPS_INT[::1] view = <MUMPS_INT[::1]> self.ob.icntl
            return view

    property n:
        def __get__(self): return self.ob.n
        def __set__(self, value): self.ob.n = value
    property nz_alloc:
        def __get__(self): return self.ob.nz_alloc
        def __set__(self, value): self.ob.nz_alloc = value

    property nz:
        def __get__(self): return self.ob.nz
        def __set__(self, value): self.ob.nz = value
    property irn:
        def __get__(self): return <long> self.ob.irn
        def __set__(self, long value): self.ob.irn = <MUMPS_INT*> value
    property jcn:
        def __get__(self): return <long> self.ob.jcn
        def __set__(self, long value): self.ob.jcn = <MUMPS_INT*> value

    property nz_loc:
        def __get__(self): return self.ob.nz_loc
        def __set__(self, value): self.ob.nz_loc = value
    property irn_loc:
        def __get__(self): return <long> self.ob.irn_loc
        def __set__(self, long value): self.ob.irn_loc = <MUMPS_INT*> value
    property jcn_loc:
        def __get__(self): return <long> self.ob.jcn_loc
        def __set__(self, long value): self.ob.jcn_loc = <MUMPS_INT*> value

    property nelt:
        def __get__(self): return self.ob.nelt
        def __set__(self, value): self.ob.nelt = value
    property eltptr:
        def __get__(self): return <long> self.ob.eltptr
        def __set__(self, long value): self.ob.eltptr = <MUMPS_INT*> value
    property eltvar:
        def __get__(self): return <long> self.ob.eltvar
        def __set__(self, long value): self.ob.eltvar = <MUMPS_INT*> value

    property perm_in:
        def __get__(self): return <long> self.ob.perm_in
        def __set__(self, long value): self.ob.perm_in = <MUMPS_INT*> value

    property sym_perm:
        def __get__(self): return <long> self.ob.sym_perm
        def __set__(self, long value): self.ob.sym_perm = <MUMPS_INT*> value
    property uns_perm:
        def __get__(self): return <long> self.ob.uns_perm
        def __set__(self, long value): self.ob.uns_perm = <MUMPS_INT*> value

    property irhs_sparse:
        def __get__(self): return <long> self.ob.irhs_sparse
        def __set__(self, long value): self.ob.irhs_sparse = <MUMPS_INT*> value
    property irhs_ptr:
        def __get__(self): return <long> self.ob.irhs_ptr
        def __set__(self, long value): self.ob.irhs_ptr = <MUMPS_INT*> value
    property isol_loc:
        def __get__(self): return <long> self.ob.isol_loc
        def __set__(self, long value): self.ob.isol_loc = <MUMPS_INT*> value

    property nrhs:
        def __get__(self): return self.ob.nrhs
        def __set__(self, value): self.ob.nrhs = value
    property lrhs:
        def __get__(self): return self.ob.lrhs
        def __set__(self, value): self.ob.lrhs = value
    property lredrhs:
        def __get__(self): return self.ob.lredrhs
        def __set__(self, value): self.ob.lredrhs = value
    property nz_rhs:
        def __get__(self): return self.ob.nz_rhs
        def __set__(self, value): self.ob.nz_rhs = value
    property lsol_loc:
        def __get__(self): return self.ob.lsol_loc
        def __set__(self, value): self.ob.lsol_loc = value

    property schur_mloc:
        def __get__(self): return self.ob.schur_mloc
        def __set__(self, value): self.ob.schur_mloc = value
    property schur_nloc:
        def __get__(self): return self.ob.schur_nloc
        def __set__(self, value): self.ob.schur_nloc = value
    property schur_lld:
        def __get__(self): return self.ob.schur_lld
        def __set__(self, value): self.ob.schur_lld = value


    property mblock:
        def __get__(self): return self.ob.mblock
        def __set__(self, value): self.ob.mblock = value
    property nblock:
        def __get__(self): return self.ob.nblock
        def __set__(self, value): self.ob.nblock = value
    property nprow:
        def __get__(self): return self.ob.nprow
        def __set__(self, value): self.ob.nprow = value
    property npcol:
        def __get__(self): return self.ob.npcol
        def __set__(self, value): self.ob.npcol = value

    property info:
        def __get__(self):
            cdef MUMPS_INT[::1] view = <MUMPS_INT[::1]> self.ob.info
            return view
    property infog:
        def __get__(self):
            cdef MUMPS_INT[::1] view = <MUMPS_INT[::1]> self.ob.infog
            return view

    property deficiency:
        def __get__(self): return self.ob.deficiency
        def __set__(self, value): self.ob.deficiency = value
    property pivnul_list:
        def __get__(self): return <long> self.ob.pivnul_list
        def __set__(self, long value): self.ob.pivnul_list = <MUMPS_INT*> value
    property mapping:
        def __get__(self): return <long> self.ob.mapping
        def __set__(self, long value): self.ob.mapping = <MUMPS_INT*> value

    property size_schur:
        def __get__(self): return self.ob.size_schur
        def __set__(self, value): self.ob.size_schur = value
    property listvar_schur:
        def __get__(self): return <long> self.ob.listvar_schur
        def __set__(self, long value): self.ob.listvar_schur = <MUMPS_INT*> value

    property instance_number:
        def __get__(self): return self.ob.instance_number
        def __set__(self, value): self.ob.instance_number = value

    property version_number:
        def __get__(self):
            return (<bytes> self.ob.version_number).decode('ascii')

    property ooc_tmpdir:
        def __get__(self):
            return (<bytes> self.ob.ooc_tmpdir).decode('ascii')
        def __set__(self, char *value):
            strncpy(self.ob.ooc_tmpdir, value, sizeof(self.ob.ooc_tmpdir))
    property ooc_prefix:
        def __get__(self):
            return (<bytes> self.ob.ooc_prefix).decode('ascii')
        def __set__(self, char *value):
            strncpy(self.ob.ooc_prefix, value, sizeof(self.ob.ooc_prefix))

    property write_problem:
        def __get__(self):
            return (<bytes> self.ob.write_problem).decode('ascii')
        def __set__(self, char *value):
            strncpy(self.ob.write_problem, value, sizeof(self.ob.write_problem))

    property lwk_user:
        def __get__(self): return self.ob.lwk_user
        def __set__(self, value): self.ob.lwk_user = value

    ######################################### TYPED Properties #########################################################
    property cntl:
        def __get__(self):
            cdef DMUMPS_REAL[::1] view = <DMUMPS_REAL[::1]> self.ob.cntl
            return view

    property a:
        def __get__(self): return <long> self.ob.a
        def __set__(self, long value): self.ob.a = <DMUMPS_COMPLEX*> value

    property a_loc:
        def __get__(self): return <long> self.ob.a_loc
        def __set__(self, long value): self.ob.a_loc = <DMUMPS_COMPLEX*> value

    property a_elt:
        def __get__(self): return <long> self.ob.a_elt
        def __set__(self, long value): self.ob.a_elt = <DMUMPS_COMPLEX*> value

    property colsca:
        def __get__(self): return <long> self.ob.colsca
        def __set__(self, long value): self.ob.colsca = <DMUMPS_REAL*> value
    property rowsca:
        def __get__(self): return <long> self.ob.rowsca
        def __set__(self, long value): self.ob.rowsca = <DMUMPS_REAL*> value

    property rhs:
        def __get__(self): return <long> self.ob.rhs
        def __set__(self, long value): self.ob.rhs = <DMUMPS_COMPLEX*> value
    property redrhs:
        def __get__(self): return <long> self.ob.redrhs
        def __set__(self, long value): self.ob.redrhs = <DMUMPS_COMPLEX*> value
    property rhs_sparse:
        def __get__(self): return <long> self.ob.rhs_sparse
        def __set__(self, long value): self.ob.rhs_sparse = <DMUMPS_COMPLEX*> value
    property sol_loc:
        def __get__(self): return <long> self.ob.sol_loc
        def __set__(self, long value): self.ob.sol_loc = <DMUMPS_COMPLEX*> value

    property rinfo:
        def __get__(self):
            cdef DMUMPS_REAL[::1] view = <DMUMPS_REAL[::1]> self.ob.rinfo
            return view
    property rinfog:
        def __get__(self):
            cdef DMUMPS_REAL[::1] view = <DMUMPS_REAL[::1]> self.ob.rinfog
            return view

    property schur:
        def __get__(self): return <long> self.ob.schur
        def __set__(self, long value): self.ob.schur = <DMUMPS_COMPLEX*> value

    property wk_user:
        def __get__(self): return <long> self.ob.wk_user
        def __set__(self, long value): self.ob.wk_user = <DMUMPS_COMPLEX*> value

    ####################################################################################################################
    #
    ####################################################################################################################