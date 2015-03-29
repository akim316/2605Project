from numpy import *

def det(A):
    if A.shape[0] == 1:
        return A[0,0]
    if A.shape[0] == 2:
        return float(A[0,0]) * A[1,1] - float(A[0,1]) * A[1,0]
    sign = -1
    total = 0
    for coef in range(A.shape[1]):
        B = zeros((A.shape[0] - 1, A.shape[1] - 1))
        i = 0
        j = 0
        for row in range(A.shape[0]):
            for col in range(A.shape[1]):
                if row != 0 and col != coef:
                    if j >= B.shape[1]:
                        j = 0
                        i += 1
                    B[i,j] = A[row,col]
                    j += 1
        sign *= -1
        detB = A[0, coef] * det(B)
        total = total + sign * detB
    return total
