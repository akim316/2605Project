from numpy import *
from numpy.linalg import *
from math2605 import *
import sys
## Test Leslie matrix
A = matrix([[0, 1.2, 1.1, .9, .1, 0, 0, 0, 0],
            [.7, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, .85, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, .9, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, .9, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, .88, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, .8, 0, 0, 0],   
            [0, 0, 0, 0, 0, 0, .77, 0, 0],  
            [0, 0, 0, 0, 0, 0, 0, .40, 0]])
## Test tolerance value
tol = 0.001
## Starting eigenvalue
initEig = array([[2.1],[1.9],[1.8],[2.1],[2.0],
                 [1.7],[1.2],[0.9],[0.5]])
## Finds the maximum value in a matrix/vector
def find_max(K):
    A = K[0,0]
    for i in range (K.shape[0]):
        for j in range (K.shape[1]):
            if K[i,j] > A:
                A = K[i,j]
    return A

## Power method 
def power_method(A, tol, initEig):
    return power_method_calculations(A, tol, initEig, initEig[0,0], 0)

## Recursive power method function that performs all the calculations
## and increments an iterator
def power_method_calculations(A, tol, initVect, initVal, iters):
    iters += 1
    if iters >= 100:
        sys.exit("Matrix does not converge to a specific eigenvalue. Exiting.")
    ## x_k+1 = Ax(k)
    result = matrixMult(A, initVect)
    ## Scaled eigenvector used for calculating tolerance
    nextVect = result / initVect[0,0]
    vect = initVect / initVal
    ## Tolerance calculated with ||e-vector_k+1 - e-vector_k||
    calcTol = find_max(nextVect) - find_max(vect)
    calcTol = abs(calcTol)
    ## Checks to see if the calculated tolerance has reached or is greater than
    ## the given tolerance
    if calcTol > tol:
        return power_method_calculations(A, tol, result, initVect[0,0], iters)
    ## If it hasn't, then simply return the iterations and the max eigenvalue
    else:
        return iters, find_max(nextVect)
print power_method(A, tol, initEig)
