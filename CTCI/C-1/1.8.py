from __future__ import print_function


# Prompt 1.8 : Write an algorithm such that if an element in an MxN matrix is 0,
#               its entire row and columns are set to 0


print("1.8")


matrix = [[1, 2, 3],
          [4, 0, 6],
          [7, 8, 0]]

matrix2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

martrixSolution = [[7, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]


def zeroOutIfZeroFound(xMatrix):
    #print("", xMatrix)

    dimension = len(matrix)  # Messed up had - 1 here, that would make newMatrix too small
    newMatrix = [[0 for row in range(dimension)] for col in range(dimension)]

    dimension = len(matrix) - 1  # 0, 1, 2 so 3 dimensional
    ifZeroFound = 0 #if a zero is found this be assigned where

    print("1")
    for row in range(len(xMatrix)):
        for col in range(len(xMatrix[row])):
            print("2 -", xMatrix[col][dimension])
            if xMatrix[col][dimension] == 0:
                print("3 -", xMatrix[col][dimension])
                ifZeroFound = dimension
                newMatrix[col][dimension] = 0
            else:
                print("4 -", ifZeroFound)
                if ifZeroFound != 0:
                    print("5")
                    newMatrix[col][dimension] = 0
                else:
                    print("6")
                    newMatrix[row][col] = xMatrix[row][col]
        dimension = dimension - 1
        ifZeroFound = 0


    return newMatrix


def printMatrix(xMatrix):
    print("Printing Matrix")
    print("---------------")
    for row in range(len(xMatrix)):
        if row != 0: print("")
        for col in range(len(xMatrix[row])):
            print(xMatrix[row][col]," ", end="")
    print("\n---------------")

print("Starting Program")
printMatrix(matrix)

matrix3 = zeroOutIfZeroFound(matrix)
printMatrix(matrix)
printMatrix(matrix3)
print("\nEnd of Program")
