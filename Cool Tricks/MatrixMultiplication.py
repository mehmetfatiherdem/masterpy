import numpy as np

# create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6, 3], [1, 2, 1]])

# multiply the matrices using @ operator
C1 = A @ B
print("Using @ operator:\n", C1)

# multiply the matrices using dot() function
C2 = np.dot(A, B)
print("Using dot() function:\n", C2)


### with no library

a = [[1, 2],
     [3, 4]]

b = [[5, 6, 3],
     [1, 2, 1]]

c = []

## c = [[7, 10, 5],
#       [19, 26, 13]]

a_row_cnt = len(a)
a_col_cnt = len(a[0])
b_col_cnt = len(b[0])

for l in range(a_row_cnt):
    c.append([0])
    for m in range(b_col_cnt - 1):
        c[l].append(0)

for i in range(a_row_cnt):
    for j in range(a_col_cnt):
        for k in range(b_col_cnt):
            c[i][k] += a[i][j] * b[j][k]

print(c)

