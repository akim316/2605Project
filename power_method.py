from numpy import *
from numpy.linalg import *
from math2605 import *
A = matrix([[0, 1.2, 1.1, .9, .1, 0, 0, 0, 0],
            [.7, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, .85, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, .9, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, .9, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, .88, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, .8, 0, 0, 0],   
            [0, 0, 0, 0, 0, 0, .77, 0, 0],  
            [0, 0, 0, 0, 0, 0, 0, .40, 0]]) 
K = matrix([[1, 2, 0],[-2,1,2],[1,3,1]])
init = matrix([[1],[1],[1]])
tol = 0.0001
initEig = array([[2.1],[1.9],[1.8],[2.1],[2.0],
                  [1.7],[1.2],[0.9],[0.5]])
def find_max(K):
    A = K[0,0]
    for i in range (K.shape[0]):
        for j in range (K.shape[1]):
            if K[i,j] > A:
                A = K[i,j]
    return A
def power_method(A, tol, initEig):
    vals = power_method_calculations(A, tol, initEig, 0)
    return vals
def power_method_calculations(A, tol, initEig, iters):
    ## Ax0
    result = matrixMult(A, initEig)
    ## x1
    nextEig = result / initEig[0,0]
    calcTol = find_max(nextEig) - find_max(initEig)
    calcTol = abs(calcTol)
    if calcTol > tol:
        iters += 1
        return power_method_calculations(A, tol, nextEig, iters)
    else:
        return "given tolerance: " + str(tol) + ", iterations: " + str(iters) + ", max eigenvalue: " + str(find_max(nextEig.transpose()))
def differ_pow_meth(A):
    x = 0
    x_0 = array([[2.1],[1.9],[1.8],[2.1],[2.0],
                  [1.7],[1.2],[0.9],[0.5]])
    x_k = zeros((x_0.shape[0], 1))
    while x <= 60:
        m = find_max(x_k)
        oldxkEig = max(x_k)
        x_k = matrixMult(A**x, x_0)
        newxkEig = max(x_k)
        tol = newxkEig - oldxkEig
        x += 1
    return x_k / m, tol
print power_method(A, tol, initEig)
