from numpy import *
from math2605 import *
A = matrix([[1.,0.5,0.333333,0.25],[0.5,0.333333,0.25,0.2],[0.333333,0.25,0.2,0.166667],[0.25,0.2,0.166667,0.142857]], dtype='f')
B = matrix([[12,-51,4],[6,167,-68], [-4,24,-41]])
def qr_fact_househ(A, b):
    copyA = copy(A)
    count = 0
    hList = []
    for num in range(copyA.shape[1]):
        columnList = copyA[:,num].tolist()
        xList = columnList[count:copyA.shape[0]]
        x = array([xList])
        #print "x = ", x
        v = array(x) - mag(x)*array([1] + [0]*(x.shape[1] - 1))
        #print "v = ", v
        #print "v shape =", v.shape[1]
        if v.shape[1] != 1:
            uT = v / mag(v)
            #print "mag v=", mag(v)
            #print "uT=", uT
            u = uT[0][newaxis, :].T
            #print "u=" , u
            H = eye(v.shape[1]) - 2*matrixMult(u,uT)
            #print "previous H =",H
            if H.shape[0] != A.shape[0]:
                identity = eye(A.shape[0])
                m = A.shape[0] - H.shape[0]

                for y in range(A.shape[0] - H.shape[0], A.shape[0]):
                    for x in range(A.shape[0] - H.shape[0], A.shape[0]):
                        identity[y,x] = H[y-m,x-m]
                H = identity
                #print "H = ", H
            hList.append(H)
            #print "H = ", H
            copyA = matrixMult(H, copyA)
            #print "new A=", copyA
            count += 1
    #print "hList=",hList
    R = copyA
    #print "R =", R
    Q = eye(R.shape[0])
    for matrix in hList:
        Q = matrixMult(Q,matrix)
    #print "Q = ", Q

    errorMatrix = matrixMult(Q,R) - A
    #print "error matrix =", errorMatrix
    maximum = 0
    for y in range(errorMatrix.shape[0]):
        for x in range(errorMatrix.shape[1]):
            if abs(errorMatrix[x,y]) > maximum:
                maximum = abs(errorMatrix[x,y])
    #print "max =", maximum
    x = solve_qr_b(Q, R, b)
    hErrorMatrix = matrixMult(A,x) - b
    hxerror = 0
    for y in range(hErrorMatrix.shape[0]):
        for x in range(hErrorMatrix.shape[1]):
            if abs(hErrorMatrix[y,x]) > hxerror:
                hxerror = abs(hErrorMatrix[y,x])
    return Q, R, maximum, x, hxerror
# listOfX = []
# count = 0
# for num in range(copyA.shape[1]):
#   columnList = copyA[:,num].tolist()
#   listOfX.append(columnList[count:copyA.shape[0]])
#   count += 1

# print listOfX

# vList = []
# uList = []
# hList = []
# for number in range(A.shape[1] - 1):
#   v = asarray(listOfX[number]) + mag(listOfX[number])*array([1] + [0]*(len(listOfX[number]) - 1))
#   u = v / mag(v)
#   H = eye(len(v)) - 2*u*u.T
#   print H
