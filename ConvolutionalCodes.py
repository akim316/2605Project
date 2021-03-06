from numpy import *
import Determinant as dt
import Inverse as inv
import random

print "\n\n********************************************************************"
print "\n************************** Program Start ***************************\n"
print "********************************************************************"

## matrix multiplication modified for binary use
def matrixMult(A,B): 
    D = zeros((A.shape[0], B.shape[1]))
    for x in range(A.shape[0]):
        for y in range(B.shape[1]):
            leftRows = A[x,:]
            rightCols = B[:,y]
            c = dot(leftRows, rightCols)
            D[x,y] = abs(c % 2) # modified region
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
print "\ny ="
print y

##############################################################################################################
##
## Jacobi Iteration
##
##############################################################################################################

print "\n\n********************************************************************"
print "\n************************* Jacobi Iteration *************************\n"
print "********************************************************************"

## create D0, U0, and L0 matrices
D0 = zeros((A0.shape[0], A0.shape[1]))
L0 = zeros((A0.shape[0], A0.shape[1]))
U0 = zeros((A0.shape[0], A0.shape[1]))

## fills in matrices
for i in range(A0.shape[0]):
    for j in range(A0.shape[1]):
        if i == j:
            D0[i, j] = A0[i, j]
        elif i < j:
            U0[i, j] = A0[i, j]
        else:
            L0[i, j] = A0[i, j]
 
## outputs D0, U0, and L0
print "\nD0 ="
print D0
print "\nU0 ="
print U0
print "\nL0 ="
print L0

x0j_k = zeros((A0.shape[0], 1))
b0j = y0

for i in range(n):
    print "\nIteration: %d:" % (i + 1)
    x0j_k = (matrixMult(-1 * (L0), x0j_k) + b0j) % 2
    print x0j_k

print "\nx0_k from iteration ="
print x0j_k

print "x0j_real"
print matrixMult(inv.inverse(A0), b0j)

## create D1, U1, and L1 matrices
D1 = zeros((A1.shape[0], A1.shape[1]))
L1 = zeros((A1.shape[0], A1.shape[1]))
U1 = zeros((A1.shape[0], A1.shape[1]))

## fills in matrices
for i in range(A1.shape[0]):
    for j in range(A1.shape[1]):
        if i == j:
            D1[i, j] = A1[i, j]
        elif i < j:
            U1[i, j] = A1[i, j]
        else:
            L1[i, j] = A1[i, j]
    
## outputs D1, U1, and L1
print "\nD1 ="
print D1
print "\nU1 ="
print U1
print "\nL1 ="
print L1

x1j_k = zeros((A1.shape[0], 1))
b1j = y1

for i in range(n):
    print "\nIteration: %d:" % (i + 1)
    x1j_k = (matrixMult(-1 * (L1), x1j_k) + b1j) % 2
    print x1j_k

print "\nx1_k from iteration ="
print x1j_k

print "\nx1j_real"
print matrixMult(inv.inverse(A1), b1j)

#############################################################################################################
##
## Gauss-Seidel Iteration
##
#############################################################################################################

print "\n\n********************************************************************"
print "\n********************** Gauss-Seidel Iteration **********************\n"
print "********************************************************************"
x0g_k = zeros((A0.shape[0], 1))
b0g = y0

print matrixMult(inv.inverse(L0 + D0), b0g)
for i in range(n):
    print "\nIteration: %d:" % (i + 1)
    x0j_k = matrixMult(inv.inverse(L0 + D0), b0g)
    print x0j_k
print "\nx0j_k ="
print x0j_k

'''
x_test = matrix([[1],[0],[1],[1],[0],[0],[0],[0]])
print matrixMult(A0,x_test)
print matrixMult(A1,x_test)
'''
