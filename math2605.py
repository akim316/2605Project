from numpy.linalg import *
from numpy import *
i = matrix([[3],[4]])
j = matrix([[3, 4]])

def matrixMult(A,B):
    D = zeros((A.shape[0],B.shape[1]))
    for x in range(A.shape[0]):
        for y in range(B.shape[1]):
            leftRows = A[x,:]
            rightCols = B[:,y]
            c = dot(leftRows, rightCols)
            D[x,y] = c
    print D
def LUfact():
    print ("LU factor")
def QRfact():
    print("QR factor")
def determinant():
    print("determinant")
def trace():
    print("trace")
def eigenVals():
    print("eigenvals")
def eigenVect():
    print("eigenvects")

matrixMult(i,j)
