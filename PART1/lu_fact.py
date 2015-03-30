from numpy import *
from math2605 import *
originalA = matrix([[1.,0.5,0.333333,0.25],[0.5,0.333333,0.25,0.2],[0.333333,0.25,0.2,0.166667],[0.25,0.2,0.166667,0.142857]], dtype='f')
B = matrix([[2,-1,1], [3,3,9], [3,3,5]], dtype='f')
C = matrix([[2,1,1], [4,-6,0], [-2,7,2]], dtype='f')
A = copy(originalA)
# print "A = ", A
gMatrices = []
for x in range(A.shape[1]):
    for y in range(1, A.shape[0]):
        if y > x:
            if A[y,x] != 0 and A[x,x] != 0:
                newRowValue = A[x]*(float(A[y,x]) / A[x,x])
                factor = (float(A[y,x]) / A[x,x])
                # print "factor = ", factor
                if A[y,x]*newRowValue[x] < 0:
                    # print "Row = ", A[y]
                    # print "addition = ", newRowValue + A[y]
                    #A[y] = newRowValue + A[y]
                    # print "newRowValue = ", newRowValue
                    # print "New A = ", A
                    zeroVector = zeros((1, A.shape[1]))
                    zeroVector[0,x] = factor
                    newGMatrix = eye(A.shape[0])
                    newGMatrix[y] = eye(A.shape[0])[y] + zeroVector
                    A = matrixMult(newGMatrix, A)
                    gMatrices.append(newGMatrix)
                elif A[y,x]*newRowValue[x] > 0:
                    # print "Row = ", A[y]
                    # print "addition = ", -1*newRowValue + A[y]
                    #A[y] = -1*newRowValue + A[y]
                    zeroVector = zeros((1, A.shape[1]))
                    zeroVector[0,x] = -1*factor
                    newGMatrix = eye(A.shape[0])
                    newGMatrix[y] = newGMatrix[y] + zeroVector
                    A = matrixMult(newGMatrix, A)
                    gMatrices.append(newGMatrix)
U = A
print "U = ", A
# print "G ARRAY = ", gMatrices
L = eye(A.shape[0])
for g in gMatrices:
    L = matrixMult(L, g)

for y in range(L.shape[1]):
    for x in range(y+1,L.shape[0]):
        L[x,y] = -1*L[x,y]
print "L = ", L

errorMatrix = matrixMult(L, U) - originalA
print "error matrix =", errorMatrix
maximum = 0
for y in range(errorMatrix.shape[0]):
    for x in range(errorMatrix.shape[1]):
        if abs(errorMatrix[x,y]) > maximum:
            maximum = abs(errorMatrix[x,y])
print "max =", maximum

b = matrix([[0.0464159],[0.0464159],[0.0464159],[0.0464159]])

print solve_lu_b(L, U, b)
