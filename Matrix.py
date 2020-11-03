import numpy as np

M_1 = [1,1,1], [2,2,2], [3,3,3]
M_2 = [3,3,3], [4,4,4], [3,3,7]
M_3 = [0,0,0], [0,0,0], [0,0,0]

print('Display all Matrix using with loop')
for x in M_1, M_2, M_3:
    for y in x:
        print(y)
    print()

print('Adding Matrix :')
for m in range(len(M_1)):
    for n in range(len(M_2)):
        M_3[m][n] = M_1[m][n] + M_2[m][n]
print(M_3)

print('Using NumPy to add Matrix')
M_1 = np.array([[1,1,1], [2,2,2], [3,3,3]])
M_2 = np.array([[3,3,3], [4,4,4], [3,3,7]])
M_3 = M_1 + M_2

print(M_3)
