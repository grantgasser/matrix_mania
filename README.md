# Matrix Mania
This package performs basic operations on mathematical (m x n) matrices such as addition, subtraction, and multiplication. This project is being done as a personal introduction to creating Python packages and making them available with PyPi.

### Author: Grant Gasser

## Installation
`pip install matrix-mania`

## Example Code
* See matrix_mania/sample.py for more 
### Import package
`
import matrix_mania as mm
mat = mm.Matrix()
`

### Add values to the matrix
`
for i in range(2):
    for j in range(2):
        mat.insert_value_given_index(i, j, 1)
`

## Files
* matrix_mania/Matrix.py: contains the Matrix class
* matrix_mania/test.py: contains unit tests for the Matrix class
* matrix_mania/sample.py: contains some sample code to demonstrate the matrix-mania package

### Important Links
* Source Code Repo: https://github.com/grantgasser/matrix_mania
* Release Download: https://pypi.org/project/matrix-mania/
