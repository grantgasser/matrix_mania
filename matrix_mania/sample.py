## Author: Grant Gasser
## Date: 6/18/2019
## Description: A sample file to get you started with the matrix-mania package

import matrix_mania as mm

mat = mm.Matrix()
mat2 = mat

print('mat:', mat)


#Make two matrices of all 1's
for i in range(2):
    for j in range(2):
        mat.insert_value_given_index(i, j, 1)


for i in range(2):
    for j in range(2):
        mat2.insert_value_given_index(i, j, 1)

print('\nmat:', mat, '\tmat2:', mat2)

#Add matrices
sum = mat + mat2

print('\nsum:', sum)
