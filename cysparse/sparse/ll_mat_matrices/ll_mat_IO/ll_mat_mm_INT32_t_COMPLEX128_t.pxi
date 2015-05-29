"""
Matrix Market IO

See http://math.nist.gov/MatrixMarket/ .

"""



cdef LLSparseMatrix_INT32_t_COMPLEX128_t MakeLLSparseMatrixFromMMFile_INT32_t_COMPLEX128_t(str mm_filename, bint store_zeros=False, bint test_bounds=True):
    cdef:
        str line
        list token_list
        str token
        char data_type
        char storage_scheme
        INT32_t nrow
        INT32_t ncol
        INT32_t nnz
        INT32_t nnz_read

    cdef:
        bint sparse
        bint is_symmetric
        bint is_complex
        list sparse_dense_list = [MM_ARRAY_STR, MM_COORDINATE_STR]
        list data_type_list = [MM_COMPLEX_STR, MM_REAL_STR, MM_INT_STR, MM_PATTERN_STR]
        dict data_type_dict = {MM_COMPLEX_STR : MM_COMPLEX, MM_REAL_STR : MM_REAL, MM_INT_STR : MM_INTEGER, MM_PATTERN_STR : MM_PATTERN}
        list storage_scheme_list = [MM_GENERAL_STR, MM_SYMM_STR, MM_HERM_STR, MM_SKEW_STR]
        dict storage_scheme_dict = {MM_GENERAL_STR : MM_GENERAL, MM_SYMM_STR : MM_SYMMETRIC, MM_HERM_STR : MM_HERMITIAN, MM_SKEW_STR : MM_SKEW}

        COMPLEX128_t z, w

    cdef LLSparseMatrix_INT32_t_COMPLEX128_t A

    with open(mm_filename, 'r') as f:
        print "je ne sais pas"

        # read banner
        line = f.readline()
        token_list = line.split()

        if len(token_list) != 5:
            raise IOError('Matrix format not recognized as Matrix Market format: not the right number of tokens in the Matrix Market banner')

        # MATRIX MARKET BANNER START
        if token_list[0] != MM_MATRIX_MARKET_BANNER_STR:
            raise IOError('Matrix format not recognized as Matrix Market format: zeroth token in the Matrix Market banner is not "%s"' % MM_MATRIX_MARKET_BANNER_STR)

        # OBJECT
        if token_list[1].lower() != MM_MTX_STR:
            raise IOError('Matrix format not recognized as Matrix Market format: first token in the Matrix Market banner is not "%s"' % MM_MTX_STR)

        # SPARSE/DENSE
        token = token_list[2].lower()
        if token not in sparse_dense_list:
            raise IOError('Matrix format not recognized as Matrix Market format: third token in the Matrix Market banner is not in "%s"' % sparse_dense_list)

        # TODO: test when matrix is NOT sparse??? what to do?
        if token == MM_ARRAY_STR:
            sparse = False
        else:
            sparse = True


        # DATA TYPE
        token = token_list[3].lower()
        if token not in data_type_list:
            raise IOError('Matrix format not recognized as Matrix Market format: fourth token in the Matrix Market banner is not in "%s"' % data_type_list)
        data_type = data_type_dict[token]
        is_complex = data_type == MM_COMPLEX


        # STORAGE SCHEME
        token = token_list[4].lower()
        if token not in storage_scheme_list:
            raise IOError('Matrix format not recognized as Matrix Market format: fourth token in the Matrix Market banner is not in "%s"' % storage_scheme_list)
        storage_scheme = storage_scheme_dict[token]
        is_symmetric = storage_scheme == MM_SYMMETRIC

        # SKIP COMMENTS
        line = f.readline()
        while line[0] == '%':
            line = f.readline()

        # READ DATA SPECIFICATION
        token_list = line.split()
        if len(token_list) != 3:
            raise IOError('Matrix format not recognized as Matrix Market format: line right after comments must contain (nrow, ncol, nnz)')

        nrow = atoi(token_list[0])
        ncol = atoi(token_list[1])
        nnz = atoi(token_list[2])

        if data_type == MM_PATTERN:
            raise IOError('Matrix Market format not supported for PATTERN')

        A = LLSparseMatrix_INT32_t_COMPLEX128_t(control_object=unexposed_value, nrow=nrow, ncol=ncol, size_hint=nnz, is_symmetric=is_symmetric, is_complex=is_complex, store_zeros=store_zeros)


        line = f.readline()
        nnz_read = 0
        if test_bounds:
            while line:
                nnz_read += 1
                token_list = line.split()


                z.real = <FLOAT64_t> atof(token_list[2])
                z.imag = <FLOAT64_t> atof(token_list[3])
                A.safe_put(atoi(token_list[0])-1, atoi(token_list[1]) - 1, z)

                line = f.readline()

        else: # don't test bounds
            print "in the else"
            while line:
                print "reading line in the else"
                nnz_read += 1
                token_list = line.split()


                print token_list[3]
                w.real = <FLOAT64_t> atof(token_list[2])
                w.imag = <FLOAT64_t> atof(token_list[3])
                A.put(atoi(token_list[0])-1, atoi(token_list[1]) - 1, w)
                #pass

                line = f.readline()

        if nnz != nnz_read:
            raise IOError('Matrix Market file contains %d data lines instead of %d' % (nnz_read, nnz))

    return A