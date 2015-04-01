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
            D[x,y] = abs(c % 2) # modified region
    return D
def encoding(n):
# print "\nEncoding Problem"
# n = int(raw_input("\nDesired length of x   ")) # takes in the desired length of n
    x = zeros((n, 1)) # creates the x matrix and fills it with 0's

    ## fills in x with random integers from 0 to 1 inclusive
    for i in range(n):
        x[i, 0] = int(random.random() + .5)
        
    print "\nrandom x ="
    print x

    x.resize(n + 3, 1) # resizes x in order to find y

    ## creates A0 and A1 matrices and fills them with 0's
    A0 = zeros((n + 3, n + 3))
    A1 = zeros((n + 3, n + 3))

    ## fills in A0 matrix
    for i in range(n + 3):
        A0[i, i] = 1
        if i - 2 >= 0:
            A0[i, i - 2] = 1
            if i - 3 >= 0:
                A0[i, i - 3] = 1

    ## fills in A1 matrix
    for i in range(n + 3):
        A1[i, i] = 1
        if i - 1 >= 0:
            A1[i, i - 1] = 1
            if i - 3 >= 0:
                A1[i, i - 3] = 1

    print "\nA0 ="
    print A0

    print "\nA1 ="
    print A1

    ## creates y
    y0 = matrixMult(A0, x)
    y1 = matrixMult(A1, x)

    print "\ny =",
    for i in range(y1.shape[0]):
        string = str(y0[i]).replace("[", "").replace(".]", "")
        string = int(string)
        print string,
        string = str(y1[i]).replace("[", "").replace(".]", "")
        string = int(string)
        print string,
