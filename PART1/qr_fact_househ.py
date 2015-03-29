from numpy import *

A = matrix([[1,0,1],[0,1,1],[1,1,0]])
copyA = copy(A)

def matrixMult(A,B):
    D = zeros((A.shape[0],B.shape[1]))
    for x in range(A.shape[0]):
        for y in range(B.shape[1]):
            leftRows = A[x,:]
            rightCols = B[:,y]
            c = dot(leftRows, rightCols)
            D[x,y] = c
    return D

def mag(aVector):
	sum = 0
	for element in aVector[0]:
		sum += element**2
	mag = sum**(1.0/2)
	return mag

count = 0
hList = []
for num in range(copyA.shape[1]):
	columnList = copyA[:,num].tolist()
	xList = columnList[count:copyA.shape[0]]
	x = array([xList])
	v = array(x) + mag(x)*array([1] + [0]*(x.shape[1] - 1))
	if v.shape[1] != 1:
	 	uT = v / mag(v)
	 	u = uT[0][newaxis, :].T
	  	H = eye(v.shape[1]) - 2*matrixMult(u,uT)
	  	if H.shape[0] != A.shape[0]:
	  		identity = eye(A.shape[0])
	  		m = A.shape[0] - H.shape[0]

	  		for y in range(A.shape[0] - H.shape[0], A.shape[0]):
	  			for x in range(A.shape[0] - H.shape[0], A.shape[0]):
	  				identity[y,x] = H[y-m,x-m]
	  		H = identity
		hList.append(H)
		copyA = matrixMult(H, copyA)
		count += 1

print copyA
print hList

# listOfX = []
# count = 0
# for num in range(copyA.shape[1]):
# 	columnList = copyA[:,num].tolist()
# 	listOfX.append(columnList[count:copyA.shape[0]])
# 	count += 1

# print listOfX

# vList = []
# uList = []
# hList = []
# for number in range(A.shape[1] - 1):
# 	v = asarray(listOfX[number]) + mag(listOfX[number])*array([1] + [0]*(len(listOfX[number]) - 1))
# 	u = v / mag(v)
# 	H = eye(len(v)) - 2*u*u.T
# 	print H
