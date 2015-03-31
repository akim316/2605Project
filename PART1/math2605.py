from numpy.linalg import *
from numpy import *
import numpy.matlib as nm
mat = matrix([[10,22,39],[49,81,21],[1,-11,35]])
lower = matrix([[1, 0, 0, 0], [0.5, 1, 0, 0], [0.3333333333333, 1, 1, 0], [0.25, 9, 1.5, 1]])
upper = matrix([[1,1,1,1],[0,1,1,1],[0,0,1,1],[0,0,0,1]])
be = matrix([[0.0464159],[0.0464159],[0.0464159],[0.0464159]])
Q = matrix([[0.838116, -0.522648, 0.153973, 0.0263067],
            [0.419058, 0.441713, -0.727754, -0.31568],
            [0.279372, 0.528821, 0.139506, 0.7892],
            [0.209529, 0.502072, 0.653609, -0.526134]])
R = matrix([[1.19315, 0.670493, 0.474933, 0.369835],
            [0, 0.118533, 0.125655, 0.117542],
            [0, 0, 0.00622177, 0.00956609],
            [0, 0, 0, -0.000187905]])

def hilbertMat(n):
    mat = eye(n)
    for y in range(mat.shape[0]):
        for x in range(mat.shape[1]):
            mat[y,x] = 1.0/((y+1)+(x+1)-1)
    a = array(1)
    b = (0.1**(n/3.0))*nm.repmat(a,n,1)
    return mat, b


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

def power_method(A, tol, initEig):
    vals = power_method_calculations(A, tol, initEig, 0)
    return vals
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
def solve_qr_b(Q, R, b):
    y = matrixMult(Q.transpose(),b)
    x = zeros((R.shape[0], 1))
    for i in xrange(R.shape[0]-1, -1, -1):
        added = 0
        current = 0
        for j in xrange (R.shape[1]-1, -1, -1):
            if i == Q.shape[0]-1:
                x[i,0] = y[i,0] / R[R.shape[0]-1,R.shape[1]-1]
            else:
                if j > i:
                    added = R[i,j]*x[j,0] + added
                elif j == i:
                    current = R[i,j]
                    x[i,0] = (y[i,0] - added) / current
                    break
    return x
def power_method_calculations(A, tol, initEig, iters):
    ## Ax0
    result = matrixMult(A, initEig)
    ## x1
    nextEig = result / max(result)
    calcTol = norm(nextEig) - norm(initEig)
    calcTol = abs(calcTol)
    if calcTol > tol:
        iters += 1
        return power_method_calculations(A, tol, nextEig, iters)
    else:
        return iters, norm(max(result)), nextEig

#print hilbertMat(5)
