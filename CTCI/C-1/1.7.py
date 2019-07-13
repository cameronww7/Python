from __future__ import print_function


# Prompt 1.7 : Given an image represented by an NxN matrix,
#               where each pixel in the image is 4 bytes, write a method
#               to rotate the image by 90 degrees can you do this in place?
#
#       EX:  1 2 3    to   7 4 1
#            4 5 6         8 5 2
#            7 8 9         9 6 3
#
#

print("1.7")

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

martrixSolution = [[7, 4, 1],
                   [8, 5, 2],
                   [9, 6, 3]]

# RotateMatrix90Deg
# Takes in a Matrix, creates a new same size matrix and then rotates said matrix 90 degrees.
def RotateMatrix90Deg(xMatrix):
    #print("", xMatrix)

    dimension = len(matrix)  # Messed up had - 1 here, that would make newMatrix too small
    newMatrix = [[0 for row in range(dimension)] for col in range(dimension)]

    dimension = len(matrix) - 1  # 0, 1, 2 so 3 dimensional

    for row in range(len(xMatrix)):
        for col in range(len(xMatrix[row])):
            newMatrix[col][dimension] = xMatrix[row][col]
        dimension = dimension - 1

    return newMatrix

# PrintMatrix
# Takes in a Matrix and then outputs the matrix nice and neat.
def PrintMatrix(xName, xMatrix):
    print("Printing", xName)
    print("---------------")

    for row in range(len(xMatrix)):
        if row != 0:
            print("")

        for col in range(len(xMatrix[row])):
            print(xMatrix[row][col], " ", end="")

    print("\n---------------")

print("Starting Program")
PrintMatrix("0 Rotation", matrix)

matrix = RotateMatrix90Deg(matrix)
PrintMatrix("1 Rotation", matrix)

matrix = RotateMatrix90Deg(matrix)
PrintMatrix("2 Rotation", matrix)

matrix = RotateMatrix90Deg(matrix)
PrintMatrix("3 Rotation", matrix)

matrix = RotateMatrix90Deg(matrix)
PrintMatrix("4 Rotation", matrix)

print("End of Program")
