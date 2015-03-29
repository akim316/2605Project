from numpy import *
import Determinant as dt

def inverse(A):
    if A.shape[0] == 1:
        return A
    if A.shape[0] == 2:
        detA = dt.det(A)
        invA = matrix([[A[1,1], -1 * A[0,1]],[-1 * A[1,0], A[0,0]]])
        if detA == 0:
            return "Not invertible"
        return (1 / detA) * invA
    sign = -1
    invA = zeros((A.shape[0], A.shape[1]))
    for x in range(A.shape[1]):
        for y in range(A.shape[0]):
            B = zeros((A.shape[0] - 1, A.shape[1] - 1))
            i = 0
            j = 0
            for row in range(A.shape[0]):
                for col in range(A.shape[1]):
                    if row != x and col != y:
                        if j >= B.shape[1]:
                            j = 0
                            i += 1
                        B[i,j] = A[row,col]
                        j += 1
            invA[y,x] = (sign)**(x + y) * dt.det(B)
    detA = dt.det(A)
    if detA == 0:
        return "Not invertible"
    return (1.0 / detA) * invA

A = matrix([[1,1,1,1],[6,1,1,1],[1,7,1,1],[1,1,1,0]])
print inverse(A)
