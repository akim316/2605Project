## from __future__ import division
from numpy import *

originalA = matrix([[1.,0.5,0.333333,0.25],[0.5,0.333333,0.25,0.2],[0.333333,0.25,0.2,0.166667],[0.25,0.2,0.166667,0.142857]], dtype='f')
A = copy(originalA)
gMatrices = []
print A
for x in range(A.shape[1]):
    for y in range(1, A.shape[0]):
        if y > x:
            for z in range(1,y+1):
                if A[y,x] != 0 and A[y-z,x] != 0:
                    newRowValue = A[y-z]*(A[y,x] / A[y-z,x])
                    print newRowValue
                    factor = (A[y,x] / A[y-z,x])
                    print factor
                    if A[y,x]*newRowValue[x] < 0:
                        A[y] = sum([newRowValue, A[y]], axis = 0)
                        print A[y]
                        print A
                        zeroVector = zeros((1, A.shape[1]))
                        zeroVector[0,x] = factor
                        newGMatrix = eye(A.shape[0])
                        newGMatrix[y] = eye(A.shape[0])[y] + zeroVector
                        gMatrices.append(newGMatrix)
                    elif A[y,x]*newRowValue[x] > 0:

                        A[y] = sum([-1*newRowValue, A[y]], axis = 0)
                        print A[y]
                        print A
                        zeroVector = zeros((1, A.shape[1]))
                        zeroVector[0,x] = -1*factor
                        newGMatrix = eye(A.shape[0])
                        newGMatrix[y] = newGMatrix[y] + zeroVector
                        gMatrices.append(newGMatrix)
print A
print gMatrices