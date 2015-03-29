from numpy import *
import random

## matrix multiplication modified for binary use
def matrixMult(A,B): 
    D = zeros((A.shape[0], B.shape[1]))
    for x in range(A.shape[0]):
        for y in range(B.shape[1]):
            leftRows = A[x,:]
            rightCols = B[:,y]
            c = dot(leftRows, rightCols)
            D[x,y] = c % 2 # modified region
    return D

n = int(raw_input("\nDesired length of x\n")) # takes in the desired length of n
x = zeros((n, 1)) # creates the x matrix and fills it with 0's

## fills in x with random integers from 0 to 1 inclusive
for i in range(n):
    x[i, 0] = int(random.random() + .5)

## outputs x
print "\nx ="
print x

x.resize(n + 3, 1) # resizes x in order to find y

## creates A0 and A1 matrices and fills them with 0's
A0 = zeros((n + 3, n + 3))
A1 = zeros((n + 3, n + 3))

num = int(1)

## fills in A0 matrix
for i in range(n + 3):
    A0[i, i] = num
    if i - 2 >= 0:
        A0[i, i - 2] = num
        if i - 3 >= 0:
            A0[i, i - 3] = num

## outputs A0
print "\nA0 ="
print A0

## fills in A1 matrix
for i in range(n + 3):
    A1[i, i] = num
    if i - 1 >= 0:
        A1[i, i - 1] = num
        if i - 3 >= 0:
            A1[i, i - 3] = num

## outputs A1 matrix
print "\nA1 ="
print A1

## outputs y0
y0 = matrixMult(A0, x)
print "\ny0 ="
print y0

## outputs y1
y1 = matrixMult(A1, x)
print "\ny1 ="
print y1

## creates y
y = []

## fills in y with y0 and y1
for i in range(y1.shape[0]):
    j0 = '0'
    j1 = '0'
    if y0[i] == 1:
        j0 = '1'
    if y1[i] == 1:
        j1 = '1'
    y.append(j0 + j1)

## outputs y
print y

##############################################################################################################
##
## testing x from project description
##
##############################################################################################################

x0 = matrix([[1],[0],[1],[1],[0],[0],[0],[0]])
print "\nThis is the test case from the project description"
print "\ny0 ="
print matrixMult(A0, x0)
print "\ny1 ="
print matrixMult(A1, x0)