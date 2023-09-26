# Pascal's Triangle Generator

A Python function to generate Pascal's Triangle up to the nth row.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Pascal's Triangle is a mathematical construct that consists of an array of numbers with interesting properties. 
This Python function allows you to generate Pascal's Triangle up to a specified row, returning the result as a list of lists.

## Prerequisites

- Python 3.x

## Usage

1. Import the `pascal_triangle` function into your Python script or project.

   ```python
   from pascal_triangle import pascal_triangle

Call the pascal_triangle function with an integer argument to generate Pascal's Triangle up to the nth row.

result = pascal_triangle(n)
The function returns a list of lists representing Pascal's Triangle.

# Example

from pascal_triangle import pascal_triangle

# Generate Pascal's Triangle up to the 5th row
result = pascal_triangle(5)

# Print the result
for row in result:
    print(row)
This will output:

#csharp

[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]

# Contributing
Contributions to this project are welcome! If you'd like to improve the code, add features, or fix issues, please feel free to open a pull request.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
