from numpy.linalg import *
from numpy import *
mat = matrix([[1,1,-2]])
B = matrix([[1],[1],[-2]])

def matrixMult(A,B):
    D = zeros((A.shape[0],B.shape[1]))
    for x in range(A.shape[0]):
        for y in range(B.shape[1]):
            leftRows = A[x,:]
            rightCols = B[:,y]
            c = dot(leftRows, rightCols)
            D[x,y] = c
    return D
print matrixMult(B,mat)
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
def solve_lu_b(): 
    print "hi"
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

print power_method(mat, 0.00001, matrix([[2],[2],[2]]))
