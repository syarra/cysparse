from cysparse.sparse.ll_mat import *
import cysparse.common_types.cysparse_types as types
import numpy as np

import sys

l1 = NewLLSparseMatrix(nrow=10, ncol=10, size_hint=40)
print l1
print type(l1)             # lots of classes are used internally...

# all memories given in bits
print l1.memory_element()  # memory for one element
print l1.memory_virtual()  # memory needed if a dense matrix was used
print l1.memory_real()     # memory used internally for the C-arrays

l1.compress()              # shrink the matrix as much as possible
print l1.memory_real()

l1[2, 2] = 450000000000000000000  # huge number
l1[9, 9] = np.inf
l1[0, 0] = np.nan

l1.put_triplet([1,1], [1, 2], [5.6, 6.7])  # i, j, val
print l1

print l1[2, 2]
print l1[0, 0]             # was not assigned -> 0.0 by default

# like a dict
print l1.keys()            # (i, j)
print l1.values()          # val
print l1.items()           # ((i,j), val)

# returns 3 NumPy arrays with **corresponding** types!
print l1.find()

l1[4, 5] = 98374983.093843483

l1.print_to(sys.stdout)

########################################################################################################################
print "=" * 80

csr = l1.to_csr()
print l1.nnz
print csr.nnz
csr.print_to(sys.stdout)

print type(csr)

########################################################################################################################
print "=" * 80

csc = l1.to_csc()
print l1.nnz
print csc.nnz
csc.print_to(sys.stdout)

print type(csc)

print csc.diag()

ww =  csc.get_numpy_arrays()

print ww

csc.debug_print()

########################################################################################################################
print "=" * 80

csc.get_c_pointers()