from numpy import *
from numpy.linalg import *
from math2605 import matrixMult
A = matrix([[0, 1.2, 1.1, .9, .1, 0, 0, 0, 0],
            [.7, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, .85, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, .9, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, .9, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, .88, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, .8, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, .77, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, .40, 0]])
tol = 0.000000001
initEig = matrix([[2.1e5],[1.9e5],[1.8e5],[2.1e5],[2.0e5],
                  [1.7e5],[1.2e5],[0.9e5],[0.5e5]])
def power_method(A, tol, initEig):
    vals = power_method_calculations(A, tol, initEig, 0)
    return vals
def power_method_calculations(A, tol, initEig, iters):
    ## Ax0
    result = matrixMult(A, initEig)
    ## x1
    nextEig = result / result[0,0]
    calcTol = norm(nextEig) - norm(initEig)
    calcTol = abs(calcTol)
    if calcTol > tol:
        iters += 1
        return power_method_calculations(A, tol, nextEig, iters)
    else:
        return iters, result[0,0], nextEig

print power_method(A, tol, initEig)
