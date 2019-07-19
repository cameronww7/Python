from __future__ import print_function
"""
# Prompt 1.8 : Write an algorithm such that if an element in an MxN matrix is 0,
#               its entire row and columns are set to 0
"""

print("1.8")

"""
# ZeroOutIfZeroFound
#   This function takes in a matrix and if a zero is found will set the 
#   columns and rows of that zero slot to zero also.
#   Once all slots have been checked and zero'ed out if need be will 
#   return the new matrix.
"""
def ZeroOutIfZeroFound(xMatrix):
    dimension = len(matrix)  # Messed up had - 1 here, that would make newMatrix too small
    newMatrix = [["N" for row in range(dimension)] for col in range(dimension)]

    newMatrix = FindZeros(xMatrix, newMatrix)

    PrintMatrix(newMatrix)

    newMatrix = SetZeros(xMatrix, newMatrix)

    PrintMatrix(newMatrix)

    newMatrix = FillMatrixIn(xMatrix, newMatrix)

    return newMatrix


"""
# FindZeros
# Takes in 2 matrix's, first one is original and second is the newly created fresh one.
# Slot by slot it checks each matrix slot for a Zeros and if one is found puts a 0 in the new matrix,
# slots that no 0 is found it leaves the slot as the original set variable,
# a N then passes back the new matrix with the all 0s found.
"""
def FindZeros(xMatrix1, xMatrix2):
    for row in range(len(xMatrix1)):
        for col in range(len(xMatrix1[row])):
            if xMatrix1[col][row] == 0:
                xMatrix2[col][row] = 0
    return xMatrix2


"""
# SetZeros
# Takes in 2 matrix's, first one is original and second is the newly created fresh one.
# Then moves through each slot checking for a zero and if a zero is found the first for
# loop will zero out the columns of the matrix that contains a zero. Then will go through
# row by row finding the zeros and zeroing out the rows that there are found zeros in the
# new matrix and returns that back.
"""
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


"""
# FillMatrixIn
# Takes in 2 matrix's, first one is original and second is the newly created fresh one.
# The two for loops search for any variables in the matrix that contain a N and then
# when a N is found will replace the N with its corresponding number in the ordinal matrix,
# when finished all the slots that need to be Zeros are Zeros and the slots that don't
# contain their original number and returns the new matrix.
"""
def FillMatrixIn(xMatrix1, xMatrix2):
    for row in range(len(xMatrix1)):
        for col in range(len(xMatrix1[row])):
            if xMatrix2[col][row] != 0:
                xMatrix2[col][row] = xMatrix1[col][row]
    return xMatrix2


"""
# PrintMatrix
# Takes in a Matrix and then outputs the matrix nice and neat.
"""
def PrintMatrix(xMatrix):
    print("Printing Matrix")
    print("---------------")

    for row in range(len(xMatrix)):
        if row != 0:
            print("")

        for col in range(len(xMatrix[row])):
            print(xMatrix[row][col], " ", end="")

    print("\n---------------")


matrix = [[1, 2, 3],
          [4, 1, 6],
          [7, 8, 0]]

matrix2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

print("Starting Program")
PrintMatrix(matrix)

matrix3 = ZeroOutIfZeroFound(matrix)

PrintMatrix(matrix)

PrintMatrix(matrix3)

print("\nEnd of Program")
