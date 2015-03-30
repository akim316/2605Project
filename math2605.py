from numpy.linalg import *
from numpy import *
mat = matrix([[10,22,39],[49,81,21],[1,-11,35]])
lower = matrix([[1, 0, 0, 0], [0.5, 1, 0, 0], [0.3333333333333, 1, 1, 0], [0.25, 9, 1.5, 1]])
upper = matrix([[1,1,1,1],[0,1,1,1],[0,0,1,1],[0,0,0,1]])
be = matrix([[2],[2],[2],[2]])

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
def LUfact():
    print ("LU factor")
def QRfact():
    print("QR factor")
def determinant():
    print("determinant")
def trace():
    print("trace")
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

print solve_lu_b(lower, upper, be)
