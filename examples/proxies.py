from cysparse.sparse.ll_mat import *
import cysparse.types.cysparse_types as types
import numpy as np

import sys

l1 = NewLLSparseMatrix(nrow=2, ncol=3, size_hint=10, dtype=COMPLEX64_T)

l1.put_triplet([1, 1, 1], [0, 1, 2], [1+1j, 1-1.0j, 2+1j])  # i, j, val

print "Original matrix:"
l1.print_to(sys.stdout)
print "Transposed matrix"
l1_T = l1.create_transpose()
l1_T.print_to(sys.stdout)

b2 = np.array([1+1j, 1+1j], dtype=np.complex64)
b3 = np.array([1+1j, 1+1j, -1j], dtype=np.complex64)

########################################################################################################################
print "=" * 80
print "Proxies"
T = l1.T
print T
print T.matvec(b2)

H = l1.H
print H
print H.matvec(b2)

conj = l1.conj
print conj
try:
    print conj.matvec(b3)
except:
    print "Not implemented yet..."

########################################################################################################################
print "=" * 80
print "T for all proxies"
TT = T.T
print TT
print TT.matvec(b3)

HT = H.T
print HT
try:
    print HT.matvec(b3)
except:
    print "Not implemented yet..."

conjT = conj.T
print conjT
print conjT.matvec(b2)

########################################################################################################################
print "=" * 80
print "H for all proxies"
TH = T.H
print TH
try:
    print TH.matvec(b3)
except:
    print "Not implemented yet..."

HH = H.H
print HH
print HH.matvec(b3)

conjH = conj.H
print conjH
print conjH.matvec(b2)

########################################################################################################################
print "=" * 80
print "conj for all proxies"
Tconj = T.conj
print Tconj
print Tconj.matvec(b2)

Hconj = H.conj
print Hconj
print Hconj.matvec(b2)

conjconj = conj.conj
print conjconj
print conjconj.matvec(b3)