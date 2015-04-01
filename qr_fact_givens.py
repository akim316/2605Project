from numpy import *
from math2605 import *
A = matrix([[1.,0.5,0.333333,0.25],[0.5,0.333333,0.25,0.2],[0.333333,0.25,0.2,0.166667],[0.25,0.2,0.166667,0.142857]], dtype='f')
def qr_fact_givens(A, b):
    copyA = copy(A)
    gList = []
    G = 0
    for y in range(copyA.shape[0]):
        columnList = copyA[:,y].tolist()
        counter = 0
        for num in columnList[y+1:copyA.shape[1]]:
            columnList = copyA[:,y].tolist()
            #print copyA
            base = columnList[y]
            #print base
            second = num
            if num != 0:
                cos = float(base) / (base**2 + second**2)**(1.0/2)

                sin = -1*float(num) / (base**2 + second**2)**(1.0/2)
                identity = eye(copyA.shape[0])
                identity[y, y] = cos
                identity[y+(counter+1), y] = sin
                #print "num =", num
                identity[y, y+(counter+1)] = -sin
                identity[y+(counter+1), y+counter+1] = cos
                counter += 1
                G = identity
                #print "G = ",G
                gList.append(identity)
                copyA = matrixMult(G, copyA)
    R = copyA
    Q = eye(A.shape[0])
    for g in gList:
        gT = g.transpose()
        Q = matrixMult(Q,gT)

    errorMatrix = matrixMult(Q,R) - A
    #print "error matrix =", errorMatrix
    maximum = 0
    for y in range(errorMatrix.shape[0]):
        for x in range(errorMatrix.shape[1]):
            if abs(errorMatrix[x,y]) > maximum:
                maximum = abs(errorMatrix[x,y])
    #print "max =", maximum
    x0 = solve_qr_b(Q, R, b)
    hErrorMatrix = matrixMult(A,x0) - b
    hxerror = 0
    for y in range(hErrorMatrix.shape[0]):
        for x in range(hErrorMatrix.shape[1]):
            if abs(hErrorMatrix[y,x]) > hxerror:
                hxerror = abs(hErrorMatrix[y,x])
    return Q, R, maximum, x0, hxerror
