cdef extern from * nogil:

    ctypedef char* SlepcPEPType "const char*"
    SlepcPEPType PEPLINEAR
    SlepcPEPType PEPQARNOLDI
    SlepcPEPType PEPTOAR
    SlepcPEPType PEPSTOAR
    SlepcPEPType PEPJD

    ctypedef enum SlepcPEPProblemType "PEPProblemType":
        PEP_GENERAL
        PEP_HERMITIAN
        PEP_GYROSCOPIC

    ctypedef enum SlepcPEPRefine "PEPRefine":
        PEP_REFINE_NONE
        PEP_REFINE_SIMPLE
        PEP_REFINE_MULTIPLE

    ctypedef enum SlepcPEPErrorType "PEPErrorType":
        PEP_ERROR_ABSOLUTE
        PEP_ERROR_RELATIVE
        PEP_ERROR_BACKWARD

    ctypedef enum SlepcPEPWhich "PEPWhich":
        PEP_LARGEST_MAGNITUDE
        PEP_SMALLEST_MAGNITUDE
        PEP_LARGEST_REAL
        PEP_SMALLEST_REAL
        PEP_LARGEST_IMAGINARY
        PEP_SMALLEST_IMAGINARY
        PEP_TARGET_MAGNITUDE
        PEP_TARGET_REAL
        PEP_TARGET_IMAGINARY

    ctypedef enum SlepcPEPBasis "PEPBasis":
        PEP_BASIS_MONOMIAL
        PEP_BASIS_CHEBYSHEV1
        PEP_BASIS_CHEBYSHEV2
        PEP_BASIS_LEGENDRE
        PEP_BASIS_LAGUERRE
        PEP_BASIS_HERMITE

    ctypedef enum SlepcPEPScale "PEPScale":
        PEP_SCALE_NONE
        PEP_SCALE_SCALAR
        PEP_SCALE_DIAGONAL
        PEP_SCALE_BOTH

    ctypedef enum SlepcPEPConv "PEPConv":
        PEP_CONV_ABS
        PEP_CONV_EIG
        PEP_CONV_NORM
        PEP_CONV_USER

    ctypedef enum SlepcPEPConvergedReason "PEPConvergedReason":
        PEP_CONVERGED_TOL
        PEP_DIVERGED_ITS
        PEP_DIVERGED_BREAKDOWN
        PEP_CONVERGED_ITERATING

    int PEPCreate(MPI_Comm,SlepcPEP*)
    int PEPDestroy(SlepcPEP*)
    int PEPReset(SlepcPEP)
    int PEPView(SlepcPEP,PetscViewer)

    int PEPSetType(SlepcPEP,SlepcPEPType)
    int PEPGetType(SlepcPEP,SlepcPEPType*)
    int PEPSetBasis(SlepcPEP,SlepcPEPBasis)
    int PEPGetBasis(SlepcPEP,SlepcPEPBasis*)
    int PEPSetProblemType(SlepcPEP,SlepcPEPProblemType)
    int PEPGetProblemType(SlepcPEP,SlepcPEPProblemType*)
    int PEPSetOperators(SlepcPEP,PetscInt,PetscMat*)
    int PEPGetOperators(SlepcPEP,PetscInt,PetscMat*)
    int PEPGetNumMatrices(SlepcPEP,PetscInt*)
    int PEPSetOptionsPrefix(SlepcPEP,char*)
    int PEPGetOptionsPrefix(SlepcPEP,char*[])
    int PEPSetFromOptions(SlepcPEP)
    int PEPAppendOptionsPrefix(SlepcPEP,char*)
    int PEPSetUp(SlepcPEP)
    int PEPSolve(SlepcPEP)

    int PEPSetBV(SlepcPEP,SlepcBV)
    int PEPGetBV(SlepcPEP,SlepcBV*)
    int PEPSetTolerances(SlepcPEP,PetscReal,PetscInt)
    int PEPGetTolerances(SlepcPEP,PetscReal*,PetscInt*)
    int PEPSetST(SlepcPEP,SlepcST)
    int PEPGetST(SlepcPEP,SlepcST*)

    int PEPSetTrackAll(SlepcPEP,PetscBool)
    int PEPGetTrackAll(SlepcPEP,PetscBool*)

    int PEPSetDimensions(SlepcPEP,PetscInt,PetscInt,PetscInt)
    int PEPGetDimensions(SlepcPEP,PetscInt*,PetscInt*,PetscInt*)
    int PEPSetScale(SlepcPEP,SlepcPEPScale,PetscReal,PetscVec,PetscVec,PetscInt,PetscReal)
    int PEPGetScale(SlepcPEP,SlepcPEPScale*,PetscReal*,PetscVec*,PetscVec*,PetscInt*,PetscReal*)

    int PEPGetConverged(SlepcPEP,PetscInt*)
    int PEPGetEigenpair(SlepcPEP,PetscInt,PetscScalar*,PetscScalar*,PetscVec,PetscVec)
    int PEPComputeError(SlepcPEP,PetscInt,SlepcPEPErrorType,PetscReal*)
    int PEPGetErrorEstimate(SlepcPEP,PetscInt,PetscReal*)

    int PEPSetConvergenceTest(SlepcPEP,SlepcPEPConv)
    int PEPGetConvergenceTest(SlepcPEP,SlepcPEPConv*)
    int PEPSetRefine(SlepcPEP,SlepcPEPRefine,PetscInt,PetscReal,PetscInt,PetscBool)
    int PEPGetRefine(SlepcPEP,SlepcPEPRefine*,PetscInt*,PetscReal*,PetscInt*,PetscBool*)

    int PEPMonitorCancel(SlepcPEP)
    int PEPGetIterationNumber(SlepcPEP,PetscInt*)

    int PEPSetInitialSpace(SlepcPEP,PetscInt,PetscVec*)
    int PEPSetWhichEigenpairs(SlepcPEP,SlepcPEPWhich)
    int PEPGetWhichEigenpairs(SlepcPEP,SlepcPEPWhich*)
    int PEPGetConvergedReason(SlepcPEP,SlepcPEPConvergedReason*)

    int PEPLinearSetCompanionForm(SlepcPEP,PetscInt)
    int PEPLinearGetCompanionForm(SlepcPEP,PetscInt*)
    int PEPLinearSetExplicitMatrix(SlepcPEP,PetscBool)
    int PEPLinearGetExplicitMatrix(SlepcPEP,PetscBool*)
    int PEPLinearSetEPS(SlepcPEP,SlepcEPS)
    int PEPLinearGetEPS(SlepcPEP,SlepcEPS*)

cdef extern from * nogil:
    int VecCopy(PetscVec,PetscVec)
    int VecSet(PetscVec,PetscScalar)
    int VecDestroy(PetscVec*)

