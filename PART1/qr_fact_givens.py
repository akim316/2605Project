from numpy import *

def matrixMult(A,B):
    D = zeros((A.shape[0],B.shape[1]))
    for x in range(A.shape[0]):
        for y in range(B.shape[1]):
            leftRows = A[x,:]
            rightCols = B[:,y]
            c = dot(leftRows, rightCols)
            D[x,y] = c
    return D

A = matrix([[1,2,0],[1,1,1],[2,1,0]])
copyA = copy(A)

gList = []
G = 0
for y in range(copyA.shape[0]):
	columnList = copyA[:,y].tolist()
	for num in columnList[y+1:copyA.shape[1]]:
		columnList = copyA[:,y].tolist()
		print copyA
		base = columnList[y]
		print base
		second = num
		if num != 0:
			print num
			cos = float(base) / (base**2 + second**2)**(1.0/2)

			sin = -1*float(num) / (base**2 + second**2)**(1.0/2)
			identity = eye(copyA.shape[0])
			identity[y, y] = cos
			identity[y, num] = -1*sin
			identity[y+(num-y), y] = sin
			identity[y+(num-y), num] = cos
			G = identity
			gList.append(identity)
			copyA = matrixMult(G, copyA)

print copyA
