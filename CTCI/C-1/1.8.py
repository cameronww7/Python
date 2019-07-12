from __future__ import print_function

# Prompt 1.8 : Write an algorithm such that if an element in an MxN matrix is 0,
#               its entire row and columns are set to 0


print("1.8")

matrix = [[1, 2, 3],
          [4, 1, 6],
          [7, 8, 0]]

matrix2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

martrixSolution = [[1, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]


def zeroOutIfZeroFound(xMatrix):
    dimension = len(matrix)  # Messed up had - 1 here, that would make newMatrix too small
    newMatrix = [["N" for row in range(dimension)] for col in range(dimension)]

    newMatrix = FindZeros(xMatrix, newMatrix)
    newMatrix = SetZeros(xMatrix, newMatrix)
    newMatrix = fillMatrixIn(xMatrix, newMatrix)

    return newMatrix


def FindZeros(xMatrix1, xMatrix2):
    for row in range(len(xMatrix1)):
        for col in range(len(xMatrix1[row])):
            if xMatrix1[col][row] == 0:
                xMatrix2[col][row] = 0
    return xMatrix2


def SetZeros(xMatrix1, xMatrix2):
    ifZeroFound = 0
    for row in range(len(xMatrix1)):
        for col in range(len(xMatrix1[row])):
            if xMatrix1[col][row] == 0:
                ifZeroFound = 1
        if ifZeroFound == 1:
            for col in range(len(xMatrix1[row])):
                xMatrix2[col][row] = 0

    ifZeroFound = 0
    for col in range(len(xMatrix1)):
        for row in range(len(xMatrix1[col])):
            if xMatrix1[col][row] == 0:
                ifZeroFound = 1
        if ifZeroFound == 1:
            for row in range(len(xMatrix1[col])):
                xMatrix2[col][row] = 0

    return xMatrix2


def fillMatrixIn(xMatrix1, xMatrix2):
    for row in range(len(xMatrix1)):
        for col in range(len(xMatrix1[row])):
            if xMatrix2[col][row] != 0:
                xMatrix2[col][row] = xMatrix1[col][row]
    return xMatrix2


def printMatrix(xMatrix):
    print("Printing Matrix")
    print("---------------")

    for row in range(len(xMatrix)):
        if row != 0:
            print("")

        for col in range(len(xMatrix[row])):
            print(xMatrix[row][col], " ", end="")

    print("\n---------------")


print("Starting Program")
printMatrix(matrix)

matrix3 = zeroOutIfZeroFound(matrix)
printMatrix(matrix)
printMatrix(matrix3)
print("\nEnd of Program")
