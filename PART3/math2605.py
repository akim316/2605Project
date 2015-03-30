from numpy.linalg import *
from numpy import *

def matrixMult(A,B):
    D = zeros((A.shape[0],B.shape[1]))
    for x in range(A.shape[0]):
        for y in range(B.shape[1]):
            leftRows = A[x,:]
            rightCols = B[:,y]
            c = dot(leftRows, rightCols)
            D[x,y] = c
    return D
def mag(aVector):
    sum = 0
    for element in aVector[0]:
        sum += element**2
    mag = sum**(1.0/2)
    return mag
def solve_lu_b(L, U, b):
    y = zeros((L.shape[0], 1))
    x = zeros((L.shape[0], 1))
    for i in range (L.shape[0]):
        added = 0
        for j in range (L.shape[1]):
            if i == 0:
                y[i,0] = b[0,0]
            else:
                if i != j:
                    added = L[i,j]*y[j,0] + added
                else:
                    y[i,0] = b[i,0] - added
    for i in xrange(U.shape[0]-1, -1, -1):
        added = 0
        current = 0
        for j in xrange (U.shape[1]-1, -1, -1):
            if i == L.shape[0]-1:
                x[i,0] = y[i,0] / U[U.shape[0]-1,U.shape[1]-1]
            else:
                if j > i:
                    added = U[i,j]*x[j,0] + added
                elif j == i:
                    current = U[i,j]
                    x[i,0] = (y[i,0] - added) / current
                    break
    return x
