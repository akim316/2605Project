from numpy import*
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

def GaussSeidel(A, b, tolerance):
    print "Gauss-Seidel Iteration"
    x_old = zeros(([A.shape[0], 1]))
    x_k = x_old[:]
    error = []
    for i in range(A.shape[0]):
        error.append(0)
    maxE = 1000
    count = 0
    tolerance = float(tolerance)
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
        print "%d iteration(s)" % count
    print matrixMult(inv.inverse(A), b)
