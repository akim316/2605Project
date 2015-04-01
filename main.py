from numpy import *
import math2605 as math
import lu_fact as LU
import qr_fact_househ as hh
import qr_fact_givens as g
import power_method as pm
import testing as test
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

elif input1 == 3:
    fileInput = str(input("Enter filename with matrix values: "))
    mat = test.readingMatrixDAT(fileInput)
    tolerance = int(input("Enter the error tolerance: "))
    initEig = zeros((mat.shape[0], 1))
    for i in range(mat.shape[0]):
        initEig[i,0] = 1
    iters, maxEig = pm.power_method(mat, tolerance, initEig)
    #print "Iterations: " + str(iters)
    #print "Max eigenvalue: " + str(maxEig)
