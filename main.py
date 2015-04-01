from numpy import *
import math2605 as math
import lu_fact as LU
import qr_fact_househ as hh
import qr_fact_givens as g
import power_method as pm
import testing as test
import gauss_seidel as gs
import jacobi as j
print "*************************************************************************"
print "* Welcome to the 2605 Project by Min Je Jung, William Su, and Alex Kim. *"
print "*************************************************************************"
print "NOTE: This code was coded in PYTHON."
input1 = int(input("Enter a part: 1, 2, or 3\n"))
if input1 == 1:
    print "Choose an option."
    input11 = int(input("[1] View LU, QR and error of one Hilbert Matrix\n[2] View all 19 Hilbert Matrices, from 2 x 2 to 20 x 20\n[3] View LU, QR, error, and solutions your own matrix.\n"))
    if input11 == 1:
        input112 = int(input("Enter a size (n) Hilbert matrix: "))
        hMatrix, b = math.hilbertMat(input112)
        L, U, maximum, x, LUhxerror = LU.lu_fact(hMatrix, b)
        hQ, hR, hmaximum, hx, hhxerror = hh.qr_fact_househ(hMatrix, b)
        gQ, gR, gmaximum, gx, ghxerror = g.qr_fact_givens(hMatrix, b)
        print "Hilbert Matrix =", hMatrix
        print "b vector =", b
        print "L =", L
        print "U =", U
        print "LU error =", maximum
        print "LU x solution =", x
        print "LU hilbert solution error =", LUhxerror
        print "House holder Q =", hQ
        print "House holder R =", hR
        print "House holder error =", hmaximum
        print "House holder x sol =", hx
        print "House holder solution error =", hhxerror
        print "Givens Q =", gQ
        print "Givens R =", gR
        print "Givens error =", gmaximum
        print "Givens x sol =", gx
        print "Givens solution error =", ghxerror
        print "================== END OF " + str(input112) + " x " + str(input112) + " MATRIX CALCULATIONS =================="
    elif input11 == 2:
        for n in range(2,21):
            hMatrix, b = math.hilbertMat(n)
            L, U, maximum, x, LUhxerror = LU.lu_fact(hMatrix, b)
            hQ, hR, hmaximum, hx, hhxerror = hh.qr_fact_househ(hMatrix, b)
            gQ, gR, gmaximum, gx, ghxerror = g.qr_fact_givens(hMatrix, b)
            print "Hilbert Matrix =", hMatrix
            print "b vector =", b
            print "L =", L
            print "U =", U
            print "LU error =", maximum
            print "LU x solution =", x
            print "LU hilbert solution error =", LUhxerror
            print "House holder Q =", hQ
            print "House holder R =", hR
            print "House holder error =", hmaximum
            print "House holder x solution =", hx
            print "House holder solution error =", hhxerror
            print "Givens Q =", gQ
            print "Givens R =", gR
            print "Givens error =", gmaximum
            print "Givens x solution =", gx
            print "Givens solution error =", ghxerror
            print "================== END OF " + str(n) + " x " + str(n) + " MATRIX CALCULATIONS =================="
    elif input11 == 3:
        input113 = str(input("Please enter the file with an augmented matrix you would like to solve as a string:\n"))
        hMatrix, b = test.readingAugmentDAT(input113)
        L, U, maximum, x, LUhxerror = LU.lu_fact(hMatrix, b)
        hQ, hR, hmaximum, hx, hhxerror = hh.qr_fact_househ(hMatrix, b)
        gQ, gR, gmaximum, gx, ghxerror = g.qr_fact_givens(hMatrix, b)
        print "Hilbert Matrix =", hMatrix
        print "b vector =", b
        print "L =", L
        print "U =", U
        print "LU error =", maximum
        print "LU x solution =", x
        print "LU Hilbert solution error =", LUhxerror
        print "House holder Q =", hQ
        print "House holder R =", hR
        print "House holder error =", hmaximum
        print "House holder x solution =", hx
        print "House holder solution error =", hhxerror
        print "Givens Q =", gQ
        print "Givens R =", gR
        print "Givens error =", gmaximum
        print "Givens x solution =", gx
        print "Givens solution error =", ghxerror
        print "================== END OF MATRIX CALCULATIONS =================="
elif input1 == 2:
    input12 = int(input("Please choose an option:\n[1] Encoding\n[2] Jacobi & Gauss-Seidal\n[3] Decoding\n"))
    if input12 == 1:
        input121 = int(input("Please enter a length n: "))
        e.encoding(input121)

    if input12 == 2:
        input122 = str(input("Please enter a filename as a string: "))
        input123 = float(input("Please enter an error tolerance: "))
        tolerance = input123
        input124 = input("Enter an initial guess array in this format (AS A STRING!): 'x[1] x[2] x[3] x[4] ... x[n]'\n")
        arraySplit = input124.split(" ")
        for num in range(len(arraySplit)):
            arraySplit[num] = int(arraySplit[num])
        initalMatrix = matrix(arraySplit)
        initialArray = initalMatrix.transpose()
        mat, b = test.readingAugmentDAT(input122)
        print "=========GAUSS-SEIDAL=========="
        gs.gauss(mat, b, initialArray, tolerance)

        print "=========JACOBI=========="
        j.jacobi(mat, b, initialArray, tolerance)


    if input12 == 3:
        input125 = input("Please enter a binary stream y as a string! (no spaces or commas) Ex. '010010110': ")
        binaryList = []
        for num in input125:
            binaryList.append(int(num))
        binaryArrayY = array(binaryList)
        print binaryArrayY
        print "Sorry, this part of the program is not listed. Please use the code in the directory Decoding.py to grade."

elif input1 == 3:
    fileInput = str(input("Enter filename with matrix values as a string: "))
    mat = test.readingMatrixDAT(fileInput)
    tolerance = int(input("Enter the error tolerance: "))
    initEig = zeros((mat.shape[0], 1))
    for i in range(mat.shape[0]):
        initEig[i,0] = 1
    iters, maxEig = pm.power_method(mat, tolerance, initEig)
    print "Iterations: " + str(iters)
    print "Max eigenvalue: " + str(maxEig)
