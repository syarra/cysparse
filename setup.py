#!/usr/bin/env python

# THIS FILE (setup.py) IS AUTOMATICALLY GENERATED
# Generate it with
# python generate_code -s

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

import ConfigParser
import io
import os
import re

####################################################################s####################################################
# HELPERS
########################################################################################################################

# Versioning: from https://packaging.python.org/en/latest/single_source_version.html#single-sourcing-the-version
# (see also https://github.com/pypa/pip)
def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# Grab paths
def get_path_option(config, section, option):
    """
    Get path(s) from an option in a section of a ``ConfigParser``.

    Args:
        config (ConfigParser): Configuration.
        section (str): Section ``[section]`` in the ``config`` configuration.
        option (str): Option ``option`` key.

    Returns:
        One or several paths ``str``\s in a ``list``.
    """
    import os
    try:
        val = config.get(section,option).split(os.pathsep)
    except:
        val = None
    return val

####################################################################s####################################################
# INIT
########################################################################################################################
cysparse_config = ConfigParser.SafeConfigParser()
cysparse_config.read('cysparse.cfg')

numpy_include = np.get_include()

# SUITESPARSE
# Do we use it or not?
use_suitesparse = cysparse_config.getboolean('SUITESPARSE', 'use_suitesparse')

# find user defined directories
if use_suitesparse:
    suitesparse_include_dirs = get_path_option(cysparse_config, 'SUITESPARSE', 'include_dirs')
    suitesparse_library_dirs = get_path_option(cysparse_config, 'SUITESPARSE', 'library_dirs')

########################################################################################################################
# EXTENSIONS
########################################################################################################################
include_dirs = [numpy_include, '.']

ext_params = {}
ext_params['include_dirs'] = include_dirs
# -Wno-unused-function is potentially dangerous... use with care!
ext_params['extra_compile_args'] = ["-O2", '-std=c99', '-Wno-unused-function']
ext_params['extra_link_args'] = []


########################################################################################################################
#                                                *** types ***
base_ext_params = ext_params.copy()
base_ext = [
    Extension(name="cysparse.types.cysparse_types",
              sources=["cysparse/types/cysparse_types.pxd", "cysparse/types/cysparse_types.pyx"]),
    Extension(name="cysparse.types.cysparse_numpy_types",
              sources=["cysparse/types/cysparse_numpy_types.pxd", "cysparse/types/cysparse_numpy_types.pyx"],
              **base_ext_params),
    Extension(name="cysparse.types.cysparse_generic_types",
              sources=["cysparse/types/cysparse_generic_types.pxd", "cysparse/types/cysparse_generic_types.pyx"]),
    ]

########################################################################################################################
#                                                *** sparse ***
sparse_ext_params = ext_params.copy()

sparse_ext = [
  ######################
  # ### Sparse ###
  ######################

  Extension(name="cysparse.sparse.sparse_utils.generic.generate_indices_INT32_t",
            sources=["cysparse/sparse/sparse_utils/generic/generate_indices_INT32_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/generate_indices_INT32_t.pyx"],
            **sparse_ext_params),
  Extension(name="cysparse.sparse.sparse_utils.generic.sort_indices_INT32_t",
            sources=["cysparse/sparse/sparse_utils/generic/sort_indices_INT32_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/sort_indices_INT32_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.generate_indices_INT64_t",
            sources=["cysparse/sparse/sparse_utils/generic/generate_indices_INT64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/generate_indices_INT64_t.pyx"],
            **sparse_ext_params),
  Extension(name="cysparse.sparse.sparse_utils.generic.sort_indices_INT64_t",
            sources=["cysparse/sparse/sparse_utils/generic/sort_indices_INT64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/sort_indices_INT64_t.pyx"],
            **sparse_ext_params),



  Extension(name="cysparse.sparse.sparse_utils.generic.print_INT32_t",
            sources=["cysparse/sparse/sparse_utils/generic/print_INT32_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/print_INT32_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.print_INT64_t",
            sources=["cysparse/sparse/sparse_utils/generic/print_INT64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/print_INT64_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.print_FLOAT32_t",
            sources=["cysparse/sparse/sparse_utils/generic/print_FLOAT32_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/print_FLOAT32_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.print_FLOAT64_t",
            sources=["cysparse/sparse/sparse_utils/generic/print_FLOAT64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/print_FLOAT64_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.print_FLOAT128_t",
            sources=["cysparse/sparse/sparse_utils/generic/print_FLOAT128_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/print_FLOAT128_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.print_COMPLEX64_t",
            sources=["cysparse/sparse/sparse_utils/generic/print_COMPLEX64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/print_COMPLEX64_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.print_COMPLEX128_t",
            sources=["cysparse/sparse/sparse_utils/generic/print_COMPLEX128_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/print_COMPLEX128_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.print_COMPLEX256_t",
            sources=["cysparse/sparse/sparse_utils/generic/print_COMPLEX256_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/print_COMPLEX256_t.pyx"],
            **sparse_ext_params),



    
  Extension(name="cysparse.sparse.sparse_utils.generic.find_INT32_t_INT32_t",
            sources=["cysparse/sparse/sparse_utils/generic/find_INT32_t_INT32_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/find_INT32_t_INT32_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.matrix_translations_INT32_t_INT32_t",
            sources=["cysparse/sparse/sparse_utils/generic/matrix_translations_INT32_t_INT32_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/matrix_translations_INT32_t_INT32_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.sparse_utils.generic.find_INT32_t_INT64_t",
            sources=["cysparse/sparse/sparse_utils/generic/find_INT32_t_INT64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/find_INT32_t_INT64_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.matrix_translations_INT32_t_INT64_t",
            sources=["cysparse/sparse/sparse_utils/generic/matrix_translations_INT32_t_INT64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/matrix_translations_INT32_t_INT64_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.sparse_utils.generic.find_INT32_t_FLOAT32_t",
            sources=["cysparse/sparse/sparse_utils/generic/find_INT32_t_FLOAT32_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/find_INT32_t_FLOAT32_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.matrix_translations_INT32_t_FLOAT32_t",
            sources=["cysparse/sparse/sparse_utils/generic/matrix_translations_INT32_t_FLOAT32_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/matrix_translations_INT32_t_FLOAT32_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.sparse_utils.generic.find_INT32_t_FLOAT64_t",
            sources=["cysparse/sparse/sparse_utils/generic/find_INT32_t_FLOAT64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/find_INT32_t_FLOAT64_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.matrix_translations_INT32_t_FLOAT64_t",
            sources=["cysparse/sparse/sparse_utils/generic/matrix_translations_INT32_t_FLOAT64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/matrix_translations_INT32_t_FLOAT64_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.sparse_utils.generic.find_INT32_t_FLOAT128_t",
            sources=["cysparse/sparse/sparse_utils/generic/find_INT32_t_FLOAT128_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/find_INT32_t_FLOAT128_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.matrix_translations_INT32_t_FLOAT128_t",
            sources=["cysparse/sparse/sparse_utils/generic/matrix_translations_INT32_t_FLOAT128_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/matrix_translations_INT32_t_FLOAT128_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.sparse_utils.generic.find_INT32_t_COMPLEX64_t",
            sources=["cysparse/sparse/sparse_utils/generic/find_INT32_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/find_INT32_t_COMPLEX64_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.matrix_translations_INT32_t_COMPLEX64_t",
            sources=["cysparse/sparse/sparse_utils/generic/matrix_translations_INT32_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/matrix_translations_INT32_t_COMPLEX64_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.sparse_utils.generic.find_INT32_t_COMPLEX128_t",
            sources=["cysparse/sparse/sparse_utils/generic/find_INT32_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/find_INT32_t_COMPLEX128_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.matrix_translations_INT32_t_COMPLEX128_t",
            sources=["cysparse/sparse/sparse_utils/generic/matrix_translations_INT32_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/matrix_translations_INT32_t_COMPLEX128_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.sparse_utils.generic.find_INT32_t_COMPLEX256_t",
            sources=["cysparse/sparse/sparse_utils/generic/find_INT32_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/find_INT32_t_COMPLEX256_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.matrix_translations_INT32_t_COMPLEX256_t",
            sources=["cysparse/sparse/sparse_utils/generic/matrix_translations_INT32_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/matrix_translations_INT32_t_COMPLEX256_t.pyx"],
            **sparse_ext_params),
    

    
  Extension(name="cysparse.sparse.sparse_utils.generic.find_INT64_t_INT32_t",
            sources=["cysparse/sparse/sparse_utils/generic/find_INT64_t_INT32_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/find_INT64_t_INT32_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.matrix_translations_INT64_t_INT32_t",
            sources=["cysparse/sparse/sparse_utils/generic/matrix_translations_INT64_t_INT32_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/matrix_translations_INT64_t_INT32_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.sparse_utils.generic.find_INT64_t_INT64_t",
            sources=["cysparse/sparse/sparse_utils/generic/find_INT64_t_INT64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/find_INT64_t_INT64_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.matrix_translations_INT64_t_INT64_t",
            sources=["cysparse/sparse/sparse_utils/generic/matrix_translations_INT64_t_INT64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/matrix_translations_INT64_t_INT64_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.sparse_utils.generic.find_INT64_t_FLOAT32_t",
            sources=["cysparse/sparse/sparse_utils/generic/find_INT64_t_FLOAT32_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/find_INT64_t_FLOAT32_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.matrix_translations_INT64_t_FLOAT32_t",
            sources=["cysparse/sparse/sparse_utils/generic/matrix_translations_INT64_t_FLOAT32_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/matrix_translations_INT64_t_FLOAT32_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.sparse_utils.generic.find_INT64_t_FLOAT64_t",
            sources=["cysparse/sparse/sparse_utils/generic/find_INT64_t_FLOAT64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/find_INT64_t_FLOAT64_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.matrix_translations_INT64_t_FLOAT64_t",
            sources=["cysparse/sparse/sparse_utils/generic/matrix_translations_INT64_t_FLOAT64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/matrix_translations_INT64_t_FLOAT64_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.sparse_utils.generic.find_INT64_t_FLOAT128_t",
            sources=["cysparse/sparse/sparse_utils/generic/find_INT64_t_FLOAT128_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/find_INT64_t_FLOAT128_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.matrix_translations_INT64_t_FLOAT128_t",
            sources=["cysparse/sparse/sparse_utils/generic/matrix_translations_INT64_t_FLOAT128_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/matrix_translations_INT64_t_FLOAT128_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.sparse_utils.generic.find_INT64_t_COMPLEX64_t",
            sources=["cysparse/sparse/sparse_utils/generic/find_INT64_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/find_INT64_t_COMPLEX64_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.matrix_translations_INT64_t_COMPLEX64_t",
            sources=["cysparse/sparse/sparse_utils/generic/matrix_translations_INT64_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/matrix_translations_INT64_t_COMPLEX64_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.sparse_utils.generic.find_INT64_t_COMPLEX128_t",
            sources=["cysparse/sparse/sparse_utils/generic/find_INT64_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/find_INT64_t_COMPLEX128_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.matrix_translations_INT64_t_COMPLEX128_t",
            sources=["cysparse/sparse/sparse_utils/generic/matrix_translations_INT64_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/matrix_translations_INT64_t_COMPLEX128_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.sparse_utils.generic.find_INT64_t_COMPLEX256_t",
            sources=["cysparse/sparse/sparse_utils/generic/find_INT64_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/find_INT64_t_COMPLEX256_t.pyx"],
            **sparse_ext_params),

  Extension(name="cysparse.sparse.sparse_utils.generic.matrix_translations_INT64_t_COMPLEX256_t",
            sources=["cysparse/sparse/sparse_utils/generic/matrix_translations_INT64_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/sparse_utils/generic/matrix_translations_INT64_t_COMPLEX256_t.pyx"],
            **sparse_ext_params),
    




  ######################
  # ### SparseMatrix ###
  ######################
  Extension(name="cysparse.sparse.s_mat",
            sources=["cysparse/sparse/s_mat.pxd",
                     "cysparse/sparse/s_mat.pyx"],
            **sparse_ext_params),


    
  Extension(name="cysparse.sparse.s_mat_matrices.s_mat_INT32_t_INT32_t",
            sources=["cysparse/sparse/s_mat_matrices/s_mat_INT32_t_INT32_t.pxd",
                     "cysparse/sparse/s_mat_matrices/s_mat_INT32_t_INT32_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.s_mat_matrices.s_mat_INT32_t_INT64_t",
            sources=["cysparse/sparse/s_mat_matrices/s_mat_INT32_t_INT64_t.pxd",
                     "cysparse/sparse/s_mat_matrices/s_mat_INT32_t_INT64_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.s_mat_matrices.s_mat_INT32_t_FLOAT32_t",
            sources=["cysparse/sparse/s_mat_matrices/s_mat_INT32_t_FLOAT32_t.pxd",
                     "cysparse/sparse/s_mat_matrices/s_mat_INT32_t_FLOAT32_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.s_mat_matrices.s_mat_INT32_t_FLOAT64_t",
            sources=["cysparse/sparse/s_mat_matrices/s_mat_INT32_t_FLOAT64_t.pxd",
                     "cysparse/sparse/s_mat_matrices/s_mat_INT32_t_FLOAT64_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.s_mat_matrices.s_mat_INT32_t_FLOAT128_t",
            sources=["cysparse/sparse/s_mat_matrices/s_mat_INT32_t_FLOAT128_t.pxd",
                     "cysparse/sparse/s_mat_matrices/s_mat_INT32_t_FLOAT128_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.s_mat_matrices.s_mat_INT32_t_COMPLEX64_t",
            sources=["cysparse/sparse/s_mat_matrices/s_mat_INT32_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/s_mat_matrices/s_mat_INT32_t_COMPLEX64_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.s_mat_matrices.s_mat_INT32_t_COMPLEX128_t",
            sources=["cysparse/sparse/s_mat_matrices/s_mat_INT32_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/s_mat_matrices/s_mat_INT32_t_COMPLEX128_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.s_mat_matrices.s_mat_INT32_t_COMPLEX256_t",
            sources=["cysparse/sparse/s_mat_matrices/s_mat_INT32_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/s_mat_matrices/s_mat_INT32_t_COMPLEX256_t.pyx"],
            **sparse_ext_params),
    

    
  Extension(name="cysparse.sparse.s_mat_matrices.s_mat_INT64_t_INT32_t",
            sources=["cysparse/sparse/s_mat_matrices/s_mat_INT64_t_INT32_t.pxd",
                     "cysparse/sparse/s_mat_matrices/s_mat_INT64_t_INT32_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.s_mat_matrices.s_mat_INT64_t_INT64_t",
            sources=["cysparse/sparse/s_mat_matrices/s_mat_INT64_t_INT64_t.pxd",
                     "cysparse/sparse/s_mat_matrices/s_mat_INT64_t_INT64_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.s_mat_matrices.s_mat_INT64_t_FLOAT32_t",
            sources=["cysparse/sparse/s_mat_matrices/s_mat_INT64_t_FLOAT32_t.pxd",
                     "cysparse/sparse/s_mat_matrices/s_mat_INT64_t_FLOAT32_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.s_mat_matrices.s_mat_INT64_t_FLOAT64_t",
            sources=["cysparse/sparse/s_mat_matrices/s_mat_INT64_t_FLOAT64_t.pxd",
                     "cysparse/sparse/s_mat_matrices/s_mat_INT64_t_FLOAT64_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.s_mat_matrices.s_mat_INT64_t_FLOAT128_t",
            sources=["cysparse/sparse/s_mat_matrices/s_mat_INT64_t_FLOAT128_t.pxd",
                     "cysparse/sparse/s_mat_matrices/s_mat_INT64_t_FLOAT128_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.s_mat_matrices.s_mat_INT64_t_COMPLEX64_t",
            sources=["cysparse/sparse/s_mat_matrices/s_mat_INT64_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/s_mat_matrices/s_mat_INT64_t_COMPLEX64_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.s_mat_matrices.s_mat_INT64_t_COMPLEX128_t",
            sources=["cysparse/sparse/s_mat_matrices/s_mat_INT64_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/s_mat_matrices/s_mat_INT64_t_COMPLEX128_t.pyx"],
            **sparse_ext_params),
    
  Extension(name="cysparse.sparse.s_mat_matrices.s_mat_INT64_t_COMPLEX256_t",
            sources=["cysparse/sparse/s_mat_matrices/s_mat_INT64_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/s_mat_matrices/s_mat_INT64_t_COMPLEX256_t.pyx"],
            **sparse_ext_params),
    


  ######################
  # ### LLSparseMatrix ###
  ######################
  Extension(name="cysparse.sparse.ll_mat",
            sources=["cysparse/sparse/ll_mat.pxd",
                     "cysparse/sparse/ll_mat.pyx"],
            **sparse_ext_params),

# TODO: add the possibility to **not** use tabu combinations...

  
  Extension(name="cysparse.sparse.ll_mat_matrices.ll_mat_INT32_t_INT32_t",
            sources=["cysparse/sparse/ll_mat_matrices/ll_mat_INT32_t_INT32_t.pxd",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_INT32_t_INT32_t.pyx",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_addition_INT32_t_INT32_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_multiplication_INT32_t_INT32_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_assignment_kernel_INT32_t_INT32_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_multiplication_by_numpy_vector_kernel_INT32_t_INT32_t.pxi",
  
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_matrices.ll_mat_INT32_t_INT64_t",
            sources=["cysparse/sparse/ll_mat_matrices/ll_mat_INT32_t_INT64_t.pxd",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_INT32_t_INT64_t.pyx",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_addition_INT32_t_INT64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_multiplication_INT32_t_INT64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_assignment_kernel_INT32_t_INT64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_multiplication_by_numpy_vector_kernel_INT32_t_INT64_t.pxi",
  
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_matrices.ll_mat_INT32_t_FLOAT32_t",
            sources=["cysparse/sparse/ll_mat_matrices/ll_mat_INT32_t_FLOAT32_t.pxd",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_INT32_t_FLOAT32_t.pyx",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_addition_INT32_t_FLOAT32_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_multiplication_INT32_t_FLOAT32_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_assignment_kernel_INT32_t_FLOAT32_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_multiplication_by_numpy_vector_kernel_INT32_t_FLOAT32_t.pxi",
  
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_matrices.ll_mat_INT32_t_FLOAT64_t",
            sources=["cysparse/sparse/ll_mat_matrices/ll_mat_INT32_t_FLOAT64_t.pxd",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_INT32_t_FLOAT64_t.pyx",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_addition_INT32_t_FLOAT64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_multiplication_INT32_t_FLOAT64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_assignment_kernel_INT32_t_FLOAT64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_multiplication_by_numpy_vector_kernel_INT32_t_FLOAT64_t.pxi",
  
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_matrices.ll_mat_INT32_t_FLOAT128_t",
            sources=["cysparse/sparse/ll_mat_matrices/ll_mat_INT32_t_FLOAT128_t.pxd",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_INT32_t_FLOAT128_t.pyx",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_addition_INT32_t_FLOAT128_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_multiplication_INT32_t_FLOAT128_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_assignment_kernel_INT32_t_FLOAT128_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_multiplication_by_numpy_vector_kernel_INT32_t_FLOAT128_t.pxi",
  
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_matrices.ll_mat_INT32_t_COMPLEX64_t",
            sources=["cysparse/sparse/ll_mat_matrices/ll_mat_INT32_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_INT32_t_COMPLEX64_t.pyx",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_addition_INT32_t_COMPLEX64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_multiplication_INT32_t_COMPLEX64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_assignment_kernel_INT32_t_COMPLEX64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_multiplication_by_numpy_vector_kernel_INT32_t_COMPLEX64_t.pxi",
  
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_matrices.ll_mat_INT32_t_COMPLEX128_t",
            sources=["cysparse/sparse/ll_mat_matrices/ll_mat_INT32_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_INT32_t_COMPLEX128_t.pyx",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_addition_INT32_t_COMPLEX128_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_multiplication_INT32_t_COMPLEX128_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_assignment_kernel_INT32_t_COMPLEX128_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_multiplication_by_numpy_vector_kernel_INT32_t_COMPLEX128_t.pxi",
  
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_matrices.ll_mat_INT32_t_COMPLEX256_t",
            sources=["cysparse/sparse/ll_mat_matrices/ll_mat_INT32_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_INT32_t_COMPLEX256_t.pyx",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_addition_INT32_t_COMPLEX256_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_multiplication_INT32_t_COMPLEX256_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_assignment_kernel_INT32_t_COMPLEX256_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_multiplication_by_numpy_vector_kernel_INT32_t_COMPLEX256_t.pxi",
  
                     ],
            **sparse_ext_params),
  

  
  Extension(name="cysparse.sparse.ll_mat_matrices.ll_mat_INT64_t_INT32_t",
            sources=["cysparse/sparse/ll_mat_matrices/ll_mat_INT64_t_INT32_t.pxd",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_INT64_t_INT32_t.pyx",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_addition_INT64_t_INT32_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_multiplication_INT64_t_INT32_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_assignment_kernel_INT64_t_INT32_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_multiplication_by_numpy_vector_kernel_INT64_t_INT32_t.pxi",
  
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_matrices.ll_mat_INT64_t_INT64_t",
            sources=["cysparse/sparse/ll_mat_matrices/ll_mat_INT64_t_INT64_t.pxd",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_INT64_t_INT64_t.pyx",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_addition_INT64_t_INT64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_multiplication_INT64_t_INT64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_assignment_kernel_INT64_t_INT64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_multiplication_by_numpy_vector_kernel_INT64_t_INT64_t.pxi",
  
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_matrices.ll_mat_INT64_t_FLOAT32_t",
            sources=["cysparse/sparse/ll_mat_matrices/ll_mat_INT64_t_FLOAT32_t.pxd",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_INT64_t_FLOAT32_t.pyx",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_addition_INT64_t_FLOAT32_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_multiplication_INT64_t_FLOAT32_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_assignment_kernel_INT64_t_FLOAT32_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_multiplication_by_numpy_vector_kernel_INT64_t_FLOAT32_t.pxi",
  
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_matrices.ll_mat_INT64_t_FLOAT64_t",
            sources=["cysparse/sparse/ll_mat_matrices/ll_mat_INT64_t_FLOAT64_t.pxd",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_INT64_t_FLOAT64_t.pyx",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_addition_INT64_t_FLOAT64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_multiplication_INT64_t_FLOAT64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_assignment_kernel_INT64_t_FLOAT64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_multiplication_by_numpy_vector_kernel_INT64_t_FLOAT64_t.pxi",
  
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_matrices.ll_mat_INT64_t_FLOAT128_t",
            sources=["cysparse/sparse/ll_mat_matrices/ll_mat_INT64_t_FLOAT128_t.pxd",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_INT64_t_FLOAT128_t.pyx",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_addition_INT64_t_FLOAT128_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_multiplication_INT64_t_FLOAT128_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_assignment_kernel_INT64_t_FLOAT128_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_multiplication_by_numpy_vector_kernel_INT64_t_FLOAT128_t.pxi",
  
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_matrices.ll_mat_INT64_t_COMPLEX64_t",
            sources=["cysparse/sparse/ll_mat_matrices/ll_mat_INT64_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_INT64_t_COMPLEX64_t.pyx",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_addition_INT64_t_COMPLEX64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_multiplication_INT64_t_COMPLEX64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_assignment_kernel_INT64_t_COMPLEX64_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_multiplication_by_numpy_vector_kernel_INT64_t_COMPLEX64_t.pxi",
  
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_matrices.ll_mat_INT64_t_COMPLEX128_t",
            sources=["cysparse/sparse/ll_mat_matrices/ll_mat_INT64_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_INT64_t_COMPLEX128_t.pyx",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_addition_INT64_t_COMPLEX128_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_multiplication_INT64_t_COMPLEX128_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_assignment_kernel_INT64_t_COMPLEX128_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_multiplication_by_numpy_vector_kernel_INT64_t_COMPLEX128_t.pxi",
  
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_matrices.ll_mat_INT64_t_COMPLEX256_t",
            sources=["cysparse/sparse/ll_mat_matrices/ll_mat_INT64_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_INT64_t_COMPLEX256_t.pyx",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_addition_INT64_t_COMPLEX256_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_helpers/ll_mat_multiplication_INT64_t_COMPLEX256_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_assignment_kernel_INT64_t_COMPLEX256_t.pxi",
                     "cysparse/sparse/ll_mat_matrices/ll_mat_kernel/ll_mat_multiplication_by_numpy_vector_kernel_INT64_t_COMPLEX256_t.pxi",
  
                     ],
            **sparse_ext_params),
  


  ######################
  # ### CSRSparseMatrix ###
  ######################

  
  Extension(name="cysparse.sparse.csr_mat_matrices.csr_mat_INT32_t_INT32_t",
            sources=["cysparse/sparse/csr_mat_matrices/csr_mat_INT32_t_INT32_t.pxd",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_INT32_t_INT32_t.pyx",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_helpers/csr_mat_multiplication_INT32_t_INT32_t.pxi",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_kernel/csr_mat_multiplication_by_numpy_vector_kernel_INT32_t_INT32_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csr_mat_matrices.csr_mat_INT32_t_INT64_t",
            sources=["cysparse/sparse/csr_mat_matrices/csr_mat_INT32_t_INT64_t.pxd",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_INT32_t_INT64_t.pyx",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_helpers/csr_mat_multiplication_INT32_t_INT64_t.pxi",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_kernel/csr_mat_multiplication_by_numpy_vector_kernel_INT32_t_INT64_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csr_mat_matrices.csr_mat_INT32_t_FLOAT32_t",
            sources=["cysparse/sparse/csr_mat_matrices/csr_mat_INT32_t_FLOAT32_t.pxd",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_INT32_t_FLOAT32_t.pyx",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_helpers/csr_mat_multiplication_INT32_t_FLOAT32_t.pxi",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_kernel/csr_mat_multiplication_by_numpy_vector_kernel_INT32_t_FLOAT32_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csr_mat_matrices.csr_mat_INT32_t_FLOAT64_t",
            sources=["cysparse/sparse/csr_mat_matrices/csr_mat_INT32_t_FLOAT64_t.pxd",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_INT32_t_FLOAT64_t.pyx",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_helpers/csr_mat_multiplication_INT32_t_FLOAT64_t.pxi",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_kernel/csr_mat_multiplication_by_numpy_vector_kernel_INT32_t_FLOAT64_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csr_mat_matrices.csr_mat_INT32_t_FLOAT128_t",
            sources=["cysparse/sparse/csr_mat_matrices/csr_mat_INT32_t_FLOAT128_t.pxd",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_INT32_t_FLOAT128_t.pyx",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_helpers/csr_mat_multiplication_INT32_t_FLOAT128_t.pxi",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_kernel/csr_mat_multiplication_by_numpy_vector_kernel_INT32_t_FLOAT128_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csr_mat_matrices.csr_mat_INT32_t_COMPLEX64_t",
            sources=["cysparse/sparse/csr_mat_matrices/csr_mat_INT32_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_INT32_t_COMPLEX64_t.pyx",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_helpers/csr_mat_multiplication_INT32_t_COMPLEX64_t.pxi",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_kernel/csr_mat_multiplication_by_numpy_vector_kernel_INT32_t_COMPLEX64_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csr_mat_matrices.csr_mat_INT32_t_COMPLEX128_t",
            sources=["cysparse/sparse/csr_mat_matrices/csr_mat_INT32_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_INT32_t_COMPLEX128_t.pyx",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_helpers/csr_mat_multiplication_INT32_t_COMPLEX128_t.pxi",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_kernel/csr_mat_multiplication_by_numpy_vector_kernel_INT32_t_COMPLEX128_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csr_mat_matrices.csr_mat_INT32_t_COMPLEX256_t",
            sources=["cysparse/sparse/csr_mat_matrices/csr_mat_INT32_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_INT32_t_COMPLEX256_t.pyx",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_helpers/csr_mat_multiplication_INT32_t_COMPLEX256_t.pxi",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_kernel/csr_mat_multiplication_by_numpy_vector_kernel_INT32_t_COMPLEX256_t.pxi",
                     ],
            **sparse_ext_params),
  

  
  Extension(name="cysparse.sparse.csr_mat_matrices.csr_mat_INT64_t_INT32_t",
            sources=["cysparse/sparse/csr_mat_matrices/csr_mat_INT64_t_INT32_t.pxd",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_INT64_t_INT32_t.pyx",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_helpers/csr_mat_multiplication_INT64_t_INT32_t.pxi",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_kernel/csr_mat_multiplication_by_numpy_vector_kernel_INT64_t_INT32_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csr_mat_matrices.csr_mat_INT64_t_INT64_t",
            sources=["cysparse/sparse/csr_mat_matrices/csr_mat_INT64_t_INT64_t.pxd",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_INT64_t_INT64_t.pyx",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_helpers/csr_mat_multiplication_INT64_t_INT64_t.pxi",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_kernel/csr_mat_multiplication_by_numpy_vector_kernel_INT64_t_INT64_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csr_mat_matrices.csr_mat_INT64_t_FLOAT32_t",
            sources=["cysparse/sparse/csr_mat_matrices/csr_mat_INT64_t_FLOAT32_t.pxd",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_INT64_t_FLOAT32_t.pyx",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_helpers/csr_mat_multiplication_INT64_t_FLOAT32_t.pxi",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_kernel/csr_mat_multiplication_by_numpy_vector_kernel_INT64_t_FLOAT32_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csr_mat_matrices.csr_mat_INT64_t_FLOAT64_t",
            sources=["cysparse/sparse/csr_mat_matrices/csr_mat_INT64_t_FLOAT64_t.pxd",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_INT64_t_FLOAT64_t.pyx",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_helpers/csr_mat_multiplication_INT64_t_FLOAT64_t.pxi",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_kernel/csr_mat_multiplication_by_numpy_vector_kernel_INT64_t_FLOAT64_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csr_mat_matrices.csr_mat_INT64_t_FLOAT128_t",
            sources=["cysparse/sparse/csr_mat_matrices/csr_mat_INT64_t_FLOAT128_t.pxd",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_INT64_t_FLOAT128_t.pyx",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_helpers/csr_mat_multiplication_INT64_t_FLOAT128_t.pxi",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_kernel/csr_mat_multiplication_by_numpy_vector_kernel_INT64_t_FLOAT128_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csr_mat_matrices.csr_mat_INT64_t_COMPLEX64_t",
            sources=["cysparse/sparse/csr_mat_matrices/csr_mat_INT64_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_INT64_t_COMPLEX64_t.pyx",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_helpers/csr_mat_multiplication_INT64_t_COMPLEX64_t.pxi",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_kernel/csr_mat_multiplication_by_numpy_vector_kernel_INT64_t_COMPLEX64_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csr_mat_matrices.csr_mat_INT64_t_COMPLEX128_t",
            sources=["cysparse/sparse/csr_mat_matrices/csr_mat_INT64_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_INT64_t_COMPLEX128_t.pyx",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_helpers/csr_mat_multiplication_INT64_t_COMPLEX128_t.pxi",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_kernel/csr_mat_multiplication_by_numpy_vector_kernel_INT64_t_COMPLEX128_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csr_mat_matrices.csr_mat_INT64_t_COMPLEX256_t",
            sources=["cysparse/sparse/csr_mat_matrices/csr_mat_INT64_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_INT64_t_COMPLEX256_t.pyx",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_helpers/csr_mat_multiplication_INT64_t_COMPLEX256_t.pxi",
                     "cysparse/sparse/csr_mat_matrices/csr_mat_kernel/csr_mat_multiplication_by_numpy_vector_kernel_INT64_t_COMPLEX256_t.pxi",
                     ],
            **sparse_ext_params),
  


  ######################
  # ### CSCSparseMatrix ###
  ######################

  
  Extension(name="cysparse.sparse.csc_mat_matrices.csc_mat_INT32_t_INT32_t",
            sources=["cysparse/sparse/csc_mat_matrices/csc_mat_INT32_t_INT32_t.pxd",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_INT32_t_INT32_t.pyx",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_helpers/csc_mat_multiplication_INT32_t_INT32_t.pxi",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_kernel/csc_mat_multiplication_by_numpy_vector_kernel_INT32_t_INT32_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csc_mat_matrices.csc_mat_INT32_t_INT64_t",
            sources=["cysparse/sparse/csc_mat_matrices/csc_mat_INT32_t_INT64_t.pxd",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_INT32_t_INT64_t.pyx",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_helpers/csc_mat_multiplication_INT32_t_INT64_t.pxi",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_kernel/csc_mat_multiplication_by_numpy_vector_kernel_INT32_t_INT64_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csc_mat_matrices.csc_mat_INT32_t_FLOAT32_t",
            sources=["cysparse/sparse/csc_mat_matrices/csc_mat_INT32_t_FLOAT32_t.pxd",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_INT32_t_FLOAT32_t.pyx",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_helpers/csc_mat_multiplication_INT32_t_FLOAT32_t.pxi",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_kernel/csc_mat_multiplication_by_numpy_vector_kernel_INT32_t_FLOAT32_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csc_mat_matrices.csc_mat_INT32_t_FLOAT64_t",
            sources=["cysparse/sparse/csc_mat_matrices/csc_mat_INT32_t_FLOAT64_t.pxd",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_INT32_t_FLOAT64_t.pyx",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_helpers/csc_mat_multiplication_INT32_t_FLOAT64_t.pxi",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_kernel/csc_mat_multiplication_by_numpy_vector_kernel_INT32_t_FLOAT64_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csc_mat_matrices.csc_mat_INT32_t_FLOAT128_t",
            sources=["cysparse/sparse/csc_mat_matrices/csc_mat_INT32_t_FLOAT128_t.pxd",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_INT32_t_FLOAT128_t.pyx",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_helpers/csc_mat_multiplication_INT32_t_FLOAT128_t.pxi",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_kernel/csc_mat_multiplication_by_numpy_vector_kernel_INT32_t_FLOAT128_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csc_mat_matrices.csc_mat_INT32_t_COMPLEX64_t",
            sources=["cysparse/sparse/csc_mat_matrices/csc_mat_INT32_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_INT32_t_COMPLEX64_t.pyx",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_helpers/csc_mat_multiplication_INT32_t_COMPLEX64_t.pxi",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_kernel/csc_mat_multiplication_by_numpy_vector_kernel_INT32_t_COMPLEX64_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csc_mat_matrices.csc_mat_INT32_t_COMPLEX128_t",
            sources=["cysparse/sparse/csc_mat_matrices/csc_mat_INT32_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_INT32_t_COMPLEX128_t.pyx",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_helpers/csc_mat_multiplication_INT32_t_COMPLEX128_t.pxi",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_kernel/csc_mat_multiplication_by_numpy_vector_kernel_INT32_t_COMPLEX128_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csc_mat_matrices.csc_mat_INT32_t_COMPLEX256_t",
            sources=["cysparse/sparse/csc_mat_matrices/csc_mat_INT32_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_INT32_t_COMPLEX256_t.pyx",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_helpers/csc_mat_multiplication_INT32_t_COMPLEX256_t.pxi",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_kernel/csc_mat_multiplication_by_numpy_vector_kernel_INT32_t_COMPLEX256_t.pxi",
                     ],
            **sparse_ext_params),
  

  
  Extension(name="cysparse.sparse.csc_mat_matrices.csc_mat_INT64_t_INT32_t",
            sources=["cysparse/sparse/csc_mat_matrices/csc_mat_INT64_t_INT32_t.pxd",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_INT64_t_INT32_t.pyx",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_helpers/csc_mat_multiplication_INT64_t_INT32_t.pxi",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_kernel/csc_mat_multiplication_by_numpy_vector_kernel_INT64_t_INT32_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csc_mat_matrices.csc_mat_INT64_t_INT64_t",
            sources=["cysparse/sparse/csc_mat_matrices/csc_mat_INT64_t_INT64_t.pxd",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_INT64_t_INT64_t.pyx",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_helpers/csc_mat_multiplication_INT64_t_INT64_t.pxi",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_kernel/csc_mat_multiplication_by_numpy_vector_kernel_INT64_t_INT64_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csc_mat_matrices.csc_mat_INT64_t_FLOAT32_t",
            sources=["cysparse/sparse/csc_mat_matrices/csc_mat_INT64_t_FLOAT32_t.pxd",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_INT64_t_FLOAT32_t.pyx",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_helpers/csc_mat_multiplication_INT64_t_FLOAT32_t.pxi",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_kernel/csc_mat_multiplication_by_numpy_vector_kernel_INT64_t_FLOAT32_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csc_mat_matrices.csc_mat_INT64_t_FLOAT64_t",
            sources=["cysparse/sparse/csc_mat_matrices/csc_mat_INT64_t_FLOAT64_t.pxd",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_INT64_t_FLOAT64_t.pyx",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_helpers/csc_mat_multiplication_INT64_t_FLOAT64_t.pxi",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_kernel/csc_mat_multiplication_by_numpy_vector_kernel_INT64_t_FLOAT64_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csc_mat_matrices.csc_mat_INT64_t_FLOAT128_t",
            sources=["cysparse/sparse/csc_mat_matrices/csc_mat_INT64_t_FLOAT128_t.pxd",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_INT64_t_FLOAT128_t.pyx",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_helpers/csc_mat_multiplication_INT64_t_FLOAT128_t.pxi",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_kernel/csc_mat_multiplication_by_numpy_vector_kernel_INT64_t_FLOAT128_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csc_mat_matrices.csc_mat_INT64_t_COMPLEX64_t",
            sources=["cysparse/sparse/csc_mat_matrices/csc_mat_INT64_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_INT64_t_COMPLEX64_t.pyx",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_helpers/csc_mat_multiplication_INT64_t_COMPLEX64_t.pxi",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_kernel/csc_mat_multiplication_by_numpy_vector_kernel_INT64_t_COMPLEX64_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csc_mat_matrices.csc_mat_INT64_t_COMPLEX128_t",
            sources=["cysparse/sparse/csc_mat_matrices/csc_mat_INT64_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_INT64_t_COMPLEX128_t.pyx",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_helpers/csc_mat_multiplication_INT64_t_COMPLEX128_t.pxi",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_kernel/csc_mat_multiplication_by_numpy_vector_kernel_INT64_t_COMPLEX128_t.pxi",
                     ],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.csc_mat_matrices.csc_mat_INT64_t_COMPLEX256_t",
            sources=["cysparse/sparse/csc_mat_matrices/csc_mat_INT64_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_INT64_t_COMPLEX256_t.pyx",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_helpers/csc_mat_multiplication_INT64_t_COMPLEX256_t.pxi",
                     "cysparse/sparse/csc_mat_matrices/csc_mat_kernel/csc_mat_multiplication_by_numpy_vector_kernel_INT64_t_COMPLEX256_t.pxi",
                     ],
            **sparse_ext_params),
  


  ######################
  # ### LLSparseMatrixView ###
  ######################


  
  Extension(name="cysparse.sparse.ll_mat_views.ll_mat_view_INT32_t_INT32_t",
            sources=["cysparse/sparse/ll_mat_views/ll_mat_view_INT32_t_INT32_t.pxd",
                     "cysparse/sparse/ll_mat_views/ll_mat_view_INT32_t_INT32_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_views.ll_mat_view_INT32_t_INT64_t",
            sources=["cysparse/sparse/ll_mat_views/ll_mat_view_INT32_t_INT64_t.pxd",
                     "cysparse/sparse/ll_mat_views/ll_mat_view_INT32_t_INT64_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_views.ll_mat_view_INT32_t_FLOAT32_t",
            sources=["cysparse/sparse/ll_mat_views/ll_mat_view_INT32_t_FLOAT32_t.pxd",
                     "cysparse/sparse/ll_mat_views/ll_mat_view_INT32_t_FLOAT32_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_views.ll_mat_view_INT32_t_FLOAT64_t",
            sources=["cysparse/sparse/ll_mat_views/ll_mat_view_INT32_t_FLOAT64_t.pxd",
                     "cysparse/sparse/ll_mat_views/ll_mat_view_INT32_t_FLOAT64_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_views.ll_mat_view_INT32_t_FLOAT128_t",
            sources=["cysparse/sparse/ll_mat_views/ll_mat_view_INT32_t_FLOAT128_t.pxd",
                     "cysparse/sparse/ll_mat_views/ll_mat_view_INT32_t_FLOAT128_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_views.ll_mat_view_INT32_t_COMPLEX64_t",
            sources=["cysparse/sparse/ll_mat_views/ll_mat_view_INT32_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/ll_mat_views/ll_mat_view_INT32_t_COMPLEX64_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_views.ll_mat_view_INT32_t_COMPLEX128_t",
            sources=["cysparse/sparse/ll_mat_views/ll_mat_view_INT32_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/ll_mat_views/ll_mat_view_INT32_t_COMPLEX128_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_views.ll_mat_view_INT32_t_COMPLEX256_t",
            sources=["cysparse/sparse/ll_mat_views/ll_mat_view_INT32_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/ll_mat_views/ll_mat_view_INT32_t_COMPLEX256_t.pyx"],
            **sparse_ext_params),
  

  
  Extension(name="cysparse.sparse.ll_mat_views.ll_mat_view_INT64_t_INT32_t",
            sources=["cysparse/sparse/ll_mat_views/ll_mat_view_INT64_t_INT32_t.pxd",
                     "cysparse/sparse/ll_mat_views/ll_mat_view_INT64_t_INT32_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_views.ll_mat_view_INT64_t_INT64_t",
            sources=["cysparse/sparse/ll_mat_views/ll_mat_view_INT64_t_INT64_t.pxd",
                     "cysparse/sparse/ll_mat_views/ll_mat_view_INT64_t_INT64_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_views.ll_mat_view_INT64_t_FLOAT32_t",
            sources=["cysparse/sparse/ll_mat_views/ll_mat_view_INT64_t_FLOAT32_t.pxd",
                     "cysparse/sparse/ll_mat_views/ll_mat_view_INT64_t_FLOAT32_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_views.ll_mat_view_INT64_t_FLOAT64_t",
            sources=["cysparse/sparse/ll_mat_views/ll_mat_view_INT64_t_FLOAT64_t.pxd",
                     "cysparse/sparse/ll_mat_views/ll_mat_view_INT64_t_FLOAT64_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_views.ll_mat_view_INT64_t_FLOAT128_t",
            sources=["cysparse/sparse/ll_mat_views/ll_mat_view_INT64_t_FLOAT128_t.pxd",
                     "cysparse/sparse/ll_mat_views/ll_mat_view_INT64_t_FLOAT128_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_views.ll_mat_view_INT64_t_COMPLEX64_t",
            sources=["cysparse/sparse/ll_mat_views/ll_mat_view_INT64_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/ll_mat_views/ll_mat_view_INT64_t_COMPLEX64_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_views.ll_mat_view_INT64_t_COMPLEX128_t",
            sources=["cysparse/sparse/ll_mat_views/ll_mat_view_INT64_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/ll_mat_views/ll_mat_view_INT64_t_COMPLEX128_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.ll_mat_views.ll_mat_view_INT64_t_COMPLEX256_t",
            sources=["cysparse/sparse/ll_mat_views/ll_mat_view_INT64_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/ll_mat_views/ll_mat_view_INT64_t_COMPLEX256_t.pyx"],
            **sparse_ext_params),
  


  ######################
  # ### TransposedSparseMatrix ###
  ######################
  Extension(name="cysparse.sparse.sparse_proxies.t_mat",
            sources=["cysparse/sparse/sparse_proxies/t_mat.pxd",
                     "cysparse/sparse/sparse_proxies/t_mat.pyx"],
            **sparse_ext_params),
  ######################
  # ### ConjugateTransposedSparseMatrix ###
  ######################

  
  Extension(name="cysparse.sparse.sparse_proxies.complex_generic.h_mat_INT32_t_COMPLEX64_t",
            sources=["cysparse/sparse/sparse_proxies/complex_generic/h_mat_INT32_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/sparse_proxies/complex_generic/h_mat_INT32_t_COMPLEX64_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.sparse_proxies.complex_generic.h_mat_INT32_t_COMPLEX128_t",
            sources=["cysparse/sparse/sparse_proxies/complex_generic/h_mat_INT32_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/sparse_proxies/complex_generic/h_mat_INT32_t_COMPLEX128_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.sparse_proxies.complex_generic.h_mat_INT32_t_COMPLEX256_t",
            sources=["cysparse/sparse/sparse_proxies/complex_generic/h_mat_INT32_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/sparse_proxies/complex_generic/h_mat_INT32_t_COMPLEX256_t.pyx"],
            **sparse_ext_params),
  

  
  Extension(name="cysparse.sparse.sparse_proxies.complex_generic.h_mat_INT64_t_COMPLEX64_t",
            sources=["cysparse/sparse/sparse_proxies/complex_generic/h_mat_INT64_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/sparse_proxies/complex_generic/h_mat_INT64_t_COMPLEX64_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.sparse_proxies.complex_generic.h_mat_INT64_t_COMPLEX128_t",
            sources=["cysparse/sparse/sparse_proxies/complex_generic/h_mat_INT64_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/sparse_proxies/complex_generic/h_mat_INT64_t_COMPLEX128_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.sparse_proxies.complex_generic.h_mat_INT64_t_COMPLEX256_t",
            sources=["cysparse/sparse/sparse_proxies/complex_generic/h_mat_INT64_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/sparse_proxies/complex_generic/h_mat_INT64_t_COMPLEX256_t.pyx"],
            **sparse_ext_params),
  


  ######################
  # ### ConjugatedSparseMatrix ###
  ######################

  
  Extension(name="cysparse.sparse.sparse_proxies.complex_generic.conj_mat_INT32_t_COMPLEX64_t",
            sources=["cysparse/sparse/sparse_proxies/complex_generic/conj_mat_INT32_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/sparse_proxies/complex_generic/conj_mat_INT32_t_COMPLEX64_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.sparse_proxies.complex_generic.conj_mat_INT32_t_COMPLEX128_t",
            sources=["cysparse/sparse/sparse_proxies/complex_generic/conj_mat_INT32_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/sparse_proxies/complex_generic/conj_mat_INT32_t_COMPLEX128_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.sparse_proxies.complex_generic.conj_mat_INT32_t_COMPLEX256_t",
            sources=["cysparse/sparse/sparse_proxies/complex_generic/conj_mat_INT32_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/sparse_proxies/complex_generic/conj_mat_INT32_t_COMPLEX256_t.pyx"],
            **sparse_ext_params),
  

  
  Extension(name="cysparse.sparse.sparse_proxies.complex_generic.conj_mat_INT64_t_COMPLEX64_t",
            sources=["cysparse/sparse/sparse_proxies/complex_generic/conj_mat_INT64_t_COMPLEX64_t.pxd",
                     "cysparse/sparse/sparse_proxies/complex_generic/conj_mat_INT64_t_COMPLEX64_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.sparse_proxies.complex_generic.conj_mat_INT64_t_COMPLEX128_t",
            sources=["cysparse/sparse/sparse_proxies/complex_generic/conj_mat_INT64_t_COMPLEX128_t.pxd",
                     "cysparse/sparse/sparse_proxies/complex_generic/conj_mat_INT64_t_COMPLEX128_t.pyx"],
            **sparse_ext_params),
  
  Extension(name="cysparse.sparse.sparse_proxies.complex_generic.conj_mat_INT64_t_COMPLEX256_t",
            sources=["cysparse/sparse/sparse_proxies/complex_generic/conj_mat_INT64_t_COMPLEX256_t.pxd",
                     "cysparse/sparse/sparse_proxies/complex_generic/conj_mat_INT64_t_COMPLEX256_t.pyx"],
            **sparse_ext_params),
  

]
########################################################################################################################
#                                                *** utils ***
utils_ext = [
    Extension("cysparse.utils.equality", ["cysparse/utils/equality.pxd", "cysparse/utils/equality.pyx"], **sparse_ext_params),
]

########################################################################################################################
#                                                *** umfpack ***
if use_suitesparse:
    umfpack_ext_params = ext_params.copy()
    umfpack_ext_params['include_dirs'].extend(suitesparse_include_dirs)
    #umfpack_ext_params['include_dirs'] = suitesparse_include_dirs
    umfpack_ext_params['library_dirs'] = suitesparse_library_dirs
    umfpack_ext_params['libraries'] = ['umfpack', 'amd']

    umfpack_ext = [

  
        Extension(name="cysparse.linalg.suitesparse.umfpack.umfpack_INT32_t_FLOAT64_t",
                  sources=['cysparse/linalg/suitesparse/umfpack/umfpack_INT32_t_FLOAT64_t.pxd',
                           'cysparse/linalg/suitesparse/umfpack/umfpack_INT32_t_FLOAT64_t.pyx'], **umfpack_ext_params),
    
        Extension(name="cysparse.linalg.suitesparse.umfpack.umfpack_INT32_t_COMPLEX128_t",
                  sources=['cysparse/linalg/suitesparse/umfpack/umfpack_INT32_t_COMPLEX128_t.pxd',
                           'cysparse/linalg/suitesparse/umfpack/umfpack_INT32_t_COMPLEX128_t.pyx'], **umfpack_ext_params),
    

  
        Extension(name="cysparse.linalg.suitesparse.umfpack.umfpack_INT64_t_FLOAT64_t",
                  sources=['cysparse/linalg/suitesparse/umfpack/umfpack_INT64_t_FLOAT64_t.pxd',
                           'cysparse/linalg/suitesparse/umfpack/umfpack_INT64_t_FLOAT64_t.pyx'], **umfpack_ext_params),
    
        Extension(name="cysparse.linalg.suitesparse.umfpack.umfpack_INT64_t_COMPLEX128_t",
                  sources=['cysparse/linalg/suitesparse/umfpack/umfpack_INT64_t_COMPLEX128_t.pxd',
                           'cysparse/linalg/suitesparse/umfpack/umfpack_INT64_t_COMPLEX128_t.pyx'], **umfpack_ext_params),
    

        ]


########################################################################################################################
# SETUP
########################################################################################################################
packages_list = ['cysparse',
            'cysparse.types',
            'cysparse.sparse',
            'cysparse.sparse.sparse_proxies',
            'cysparse.sparse.sparse_proxies.complex_generic',
            'cysparse.sparse.sparse_utils',
            'cysparse.sparse.sparse_utils.generic',
            'cysparse.sparse.s_mat_matrices',
            'cysparse.sparse.ll_mat_matrices',
            'cysparse.sparse.csr_mat_matrices',
            'cysparse.sparse.csc_mat_matrices',
            'cysparse.sparse.ll_mat_views',
            'cysparse.utils',
            'cysparse.linalg',
            #'cysparse.sparse.IO'
            ]

ext_modules = base_ext + sparse_ext

if use_suitesparse:
    # add suitsparse package
    ext_modules += umfpack_ext
    packages_list.append('cysparse.linalg.suitesparse')

setup(name=  'CySparse',
  version=find_version('cysparse', '__init__.py'),
  #ext_package='cysparse', <- doesn't work with pxd files...
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
  package_dir = {"cysparse": "cysparse"},
  packages=packages_list

)
