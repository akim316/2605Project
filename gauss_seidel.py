from numpy import *

def matrixMult(A,B): 
    D = zeros((A.shape[0], B.shape[1]))
    for x in range(A.shape[0]):
        for y in range(B.shape[1]):
            leftRows = A[x,:]
            rightCols = B[:,y]
            c = dot(leftRows, rightCols)
            D[x,y] = c
    return D

def gauss(A, b, x_old, tol):

    tolerance = float(tol)
    x_k = copy(x_old)
    error = []

    for i in range(A.shape[0]):
        error.append(0)
    
    maxE = 1000
    count = 0

    while maxE > tolerance and count < 50:
        for i in range(A.shape[0]):
            total = 0
            for j in range(A.shape[1]):
                if i == j:
                    continue
                total += float(A[i, j]) * x_k[j, 0]
            x_old = copy(x_k)
            x_k[i, 0] = ((b[i, 0] - total) / A[i, i])
            error[i] = abs((x_k[i, 0] - x_old[i, 0]))
        print "Iteration %d:" % (count + 1)
        print x_k
        maxE = error[0]
        for i in range(A.shape[0]):
            if error[i] > maxE:
                maxE = error[i]
        count += 1
 
    if count >= 50:
        print "does not converge"
    else:
        print "x_k ="
        print x_k
        print "\n%d iteration(s)" % count

# b = matrix([[1],[0],[0],[0],[0],[0],[1],[0],[0],[0],[0],[1],[1],[0],[1],[1],[0]])

# n = b.shape[0]

# ## creates A0 and A1 matrices and fills them with 0's
# A0 = zeros((n, n))
# A1 = zeros((n, n))

# ## fills in A0 matrix
# for i in range(n):
#     A0[i, i] = 1
#     if i - 2 >= 0:
#         A0[i, i - 2] = 1
#         if i - 3 >= 0:
#             A0[i, i - 3] = 1

# x_initial = zeros([b.shape[0], 1])
# tol = .000000000000000001

# x0_gauss = gauss(A0, b, x_initial, tol)
