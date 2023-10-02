#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''

def pascal_triangle(n):
    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle list
    triangle = []

    # Generate each row
    for i in range(n):
        # Initialize the row list for this iteration
        row = []

        # Calculate the values in the row
        for j in range(i + 1):
            if j == 0 or j == i:
                # The first and last values in each row are always 1
                row.append(1)
            else:
                # Other values are the sum of the two values above them
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)

        # Append the row to the triangle list
        triangle.append(row)

    # Return the Pascal's Triangle
    return triangle

#calling the above function with an integer n as an argument to generate Pascal's Triangle up to the nth row.
# print result

result = pascal_triangle(5)
for row in result:
    print(row)
