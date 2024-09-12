#!/usr/bin/python3
"""0-rotate_2d_matrix.py"""


def rotate_2d_matrix(matrix):
    """ an n x n 2D matrix, rotate it 90 degrees clockwise."""

    matrix.reverse()
    mat_len = len(matrix)
    for i in range(mat_len):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
