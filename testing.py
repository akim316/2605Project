from numpy import *
def readingDAT(filename):
	matrixList = []
	matrixList2 = []
	for line in open(filename, 'r'):
	    item = line.rstrip()
	    aList = item.split(" ")
	    for num in range(len(aList)):
	    	aList[num] = float(aList[num])
	    matrixList.append(aList)
	mat = matrix(matrixList)
	print mat
	if mat.shape[0] == mat.shape[1]:
		return mat
	else:
		b = mat[:,(mat.shape[1]-1)].tolist()
		for line in matrixList:
			newList = []
			for x in range(len(line)-1):
				newList.append(line[x])
			matrixList2.append(newList)
		mat = matrix(matrixList2)
		return mat, b
print readingDAT("b.dat")