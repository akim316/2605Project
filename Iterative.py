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

print "Input in [A|b]"

line = raw_input().replace(",", " ").split(" ")

A = zeros(([len(line) - 1, len(line) - 1]))
b = zeros(([len(line) - 1, 1]))

count = 0
for j in range(len(line)):
    if j == len(line) - 1:
        b[count , 0] = float(line[j])
    else:
        A[count, j] = float(line[j])
count += 1

lineLen = len(line)
for i in range(lineLen - 2):
    line = raw_input().replace(",", " ").split(" ")
    if len(line) > lineLen:
        print "Matrix need to be a square matrix"
        break
    for j in range(len(line)):
        if j == len(line) - 1:
            b[count, 0] = float(line[j])
        else:
            A[count, j] = float(line[j])
    count += 1

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

x_k = zeros(([b.shape[0], 1]))

print D
print U
print L

for i in range(10):
    print "\nIteration: %d:" % (i + 1)
    x_k = matrixMult(inv.inverse(D), (matrixMult(-1 * (L + U), x_k) + b))
    print x_k

print matrixMult(inv.inverse(A), b)

