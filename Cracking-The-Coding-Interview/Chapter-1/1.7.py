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

def rotateMatrix90Deg(xMatrix):
    print(xMatrix)



rotateMatrix90Deg(matrix)