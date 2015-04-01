from numpy import *
#import testing as test

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
    
def jacobi(A, b, x_old, tol):

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

    maxE = 1000
    count = 0
    
    x_k = copy(x_old)
    
    count = 0
    
    tolerance = float(tol)

    while maxE > tolerance and count < 50:
        x_old = copy(x_k)
        x_k = (matrixMult(-1 * L, x_old) + b) % 2
        maxE = abs(x_k[i, 0] - x_old[i, 0])
        for i in range(x_k.shape[0]):
            error = abs((x_k[i, 0] - x_old[i, 0]))
            if error > maxE:
                maxE = error
        count += 1
    return x_k
    
def gauss(A, b, x_old, tol):
    x_k = copy(x_old)
    error = []
    
    for i in range(A.shape[0]):
        error.append(0)
    maxE = 1000
    count = 0
    tolerance = float(tol)
    
    while maxE > tolerance and count < 50:
        for i in range(A.shape[0]):
            total = 0
            for j in range(A.shape[1]):
                if i == j:
                    continue
                total += float(A[i, j]) * x_k[j, 0]
            x_old = copy(x_k)
            x_k[i, 0] = abs((b[i, 0] - total) / A[i, i])
            error[i] = abs((x_k[i, 0] - x_old[i, 0]))
        maxE = error[0]
        for i in range(A.shape[0]):
            if error[i] > maxE:
                maxE = error[i]
        count += 1
    return x_k

y = array([1,1,0,1,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,1,1,1,0,1,1,0,1,1,0,0])

y0 = zeros([len(y) / 2, 1])
y1 = zeros([len(y) / 2, 1])

count = 0
for element in y:
    if count % 2 == 0:
        y0[count / 2, 0] = element
    else:
        y1[count / 2, 0] = element
    count += 1

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

x0_jacobi = jacobi(A0, y0, x_initial, tol)
x0_gauss = gauss(A0, y0, x_initial, tol)

## fills in A1 matrix
for i in range(n):
    A1[i, i] = 1
    if i - 1 >= 0:
        A1[i, i - 1] = 1
        if i - 3 >= 0:
            A1[i, i - 3] = 1

x1_jacobi = jacobi(A1, y1, x_initial, tol)
x1_gauss = gauss(A1, y1, x_initial, tol)

x0_jacobi.resize(n - 3, 1)
x0_gauss.resize(n - 3, 1)
x1_jacobi.resize(n - 3, 1)
x1_gauss.resize(n - 3, 1)

print x0_jacobi % 2
print x1_jacobi % 2
print x0_gauss % 2
print x1_gauss % 2
