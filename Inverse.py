from numpy import *
import Determinant as dt

def inverse(A):
    A = 1.0 * A
    B = matrix(identity(A.shape[0]))
    for i in range(A.shape[0]):
        if A[i,i] == 0:
            return "Cannot be Inverted"
        mult = A[i,i]
        for j in range(A.shape[1]):
            A[i,j] = float(A[i,j]) / mult
            B[i,j] = float(B[i,j]) / mult
        for j in range(A.shape[0]):
            if j == i:
                continue
            div = float(A[j,i]) / A[i,i]
            for k in range(A.shape[0]):
                A[j,k] -= div * A[i,k]
                B[j,k] -= div * B[i,k]
    return B
