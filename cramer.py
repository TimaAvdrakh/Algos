
from scipy.linalg import det
# def crammer(arr, b):
A = [[2, -1, 5],
     [2, 3, 2],
     [1, 3, 3], ]

B = [3,-21,45]

C = [[2, -1, 5],
     [2, 3, 2],
     [1, 3, 3],]

x = []

for i in range(len(B)):
    for j in range(len(B)):
        C[j][i] = B[j]
        if i > 0:
            C[j][i-1] = A[j][i-1]
    x.append(round(det(C)/det(A),1))

print(x)