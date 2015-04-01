from numpy import *
import Inverse as inv
import GaussSeidel as gs

def matrixMult(A,B): 
    D = zeros((A.shape[0], B.shape[1]))
    for x in range(A.shape[0]):
        for y in range(B.shape[1]):
            leftRows = A[x,:]
            rightCols = B[:,y]
            c = dot(leftRows, rightCols)
            D[x,y] = c
    return D

tolerance = float(raw_input("input tolerance"))

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

print D
print U
print L

maxE = 1000
count = 0

x_old = zeros(([A.shape[0], 1]))
x_k = x_old[:]

count = 0

while maxE > tolerance and count < 50:
    print "Iteration %d:" % (count + 1)
    x_old = copy(x_k)
    x_k = matrixMult(inv.inverse(D), (matrixMult(-1 * (L + U), x_old) + b))
    maxE = abs(x_k[i, 0] - x_old[i, 0])
    for i in range(x_k.shape[0]):
        error = abs((x_k[i, 0] - x_old[i, 0]))
        if error > maxE:
            maxE = error
    print maxE
    print x_k
    count += 1
    
print "\nx_k ="
print x_k

gs.GaussSeidel(A, b, tolerance)
