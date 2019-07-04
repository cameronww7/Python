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

#print(len(matrix))
#print("Goal Solution:\n", martrixSolution)

def rotateMatrix90Deg(xMatrix):
    #print("", xMatrix)

    dimension = len(matrix) - 1 # 0, 1, 2 so 3 dimensional
    newMatrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for row in range(len(xMatrix)):
        for col in range(len(xMatrix[row])):
            newMatrix[col][dimension] = xMatrix[row][col]
        dimension = dimension - 1

    return newMatrix

print("Starting Program")
print("0 rotate", matrix)

matrix = rotateMatrix90Deg(matrix)
print("1 rotate", matrix)

matrix = rotateMatrix90Deg(matrix)
print("2 rotate", matrix)

matrix = rotateMatrix90Deg(matrix)
print("3 rotate", matrix)

matrix = rotateMatrix90Deg(matrix)
print("4 rotate", matrix)

print("End of Program")
