from numpy import *
def readingMatrixDAT(filename):
	matrixList = []
	matrixList2 = []
	for line in open(filename, 'r'):
	    item = line.rstrip()
	    aList = item.split(" ")
	    for num in range(len(aList)):
	    	aList[num] = float(aList[num])
	    matrixList.append(aList)
	mat = matrix(matrixList)
	return mat
def readingAugmentDAT(filename):
	matrixList = []
	matrixList2 = []
	for line in open(filename, 'r'):
	    item = line.rstrip()
	    aList = item.split(" ")
	    for num in range(len(aList)):
	    	aList[num] = float(aList[num])
	    matrixList.append(aList)
	mat = matrix(matrixList)
	b = mat[:,(mat.shape[1]-1)].tolist()
	b = array(b)
	for line in matrixList:
		newList = []
		for x in range(len(line)-1):
			newList.append(line[x])
		matrixList2.append(newList)
	mat = matrix(matrixList2)
	return mat, b
print readingAugmentDAT("b.dat")