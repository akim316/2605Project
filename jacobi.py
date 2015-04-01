from numpy import *
import Inverse as inv

def matrixMult(A,B): 
    D = zeros((A.shape[0], B.shape[1]))
    for x in range(A.shape[0]):
        for y in range(B.shape[1]):
            leftRows = A[x,:]
            rightCols = B[:,y]
            c = dot(leftRows, rightCols)
            D[x,y] = c
    return D

def jacobi(A, b, x_initial, tol):
    tolerance = float(tol)    
    
    D = zeros(([A.shape[0], A.shape[1]]))
    U = zeros(([A.shape[0], A.shape[1]]))
    L = zeros(([A.shape[0], A.shape[1]]))

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if i == j:
                D[i, j] = A[i, j]
            elif i < j:
                U[i, j] = A[i, j]
            else:
                L[i, j] = A[i, j]

    print D
    print U
    print L

    maxE = 1000
    count = 0

    x_old = zeros(([A.shape[0], 1]))
    x_k = x_old[:]

    count = 0

    while maxE > tolerance and count < 50:
        print "Iteration %d:" % (count + 1)
        x_old = copy(x_k)
        x_k = matrixMult(inv.inverse(D), (matrixMult(-1 * (L + U), x_old) + b))
        maxE = abs(x_k[i, 0] - x_old[i, 0])
        for i in range(x_k.shape[0]):
            error = abs((x_k[i, 0] - x_old[i, 0]))
            if error > maxE:
                maxE = error
        print x_k
        count += 1
    
    print "\nx_k ="
    print x_k
    print "\n%d iteration(s)" % count

y0 = matrix([[1],[0],[0],[0],[0],[0],[1],[0],[0],[0],[0],[1],[1],[0],[1],[1],[0]])
n = y0.shape[0]

## creates A0 and A1 matrices and fills them with 0's
A0 = zeros((n, n))
A1 = zeros((n, n))

## fills in A0 matrix
for i in range(n):
    A0[i, i] = 1
    if i - 2 >= 0:
        A0[i, i - 2] = 1
        if i - 3 >= 0:
            A0[i, i - 3] = 1

x_initial = zeros([y0.shape[0], 1])
tol = .01

x1_jacobi = jacobi(A0, y0, x_initial, tol)

