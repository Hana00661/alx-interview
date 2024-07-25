#!/usr/bin/python3
"""
function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's
    triangle of n """

    if n <= 0:
        return []

    else:
        # Initialize a variable called triangle with a list containing a
        # single element which represents the first row of the triangle.
        triangle = [[1]]

        for i in range(1, n):
            # On each iteration of the loop, a new list is created and
            # appended to the triangle variable.
            triangle.append([1])

            # The function then enters a nested loop that iterates over the
            # elements in the previous row (the row with an index of i-1) and
            # calculates the value of each element in the new row.
            for j in range(1, i):
                triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])

            # This process continues until all of the elements in the new row.
            triangle[i].append(1)
        return triangle
