# Create Matrix with Comprehension.
def Matrix(row, col):
    m1 = [[a+1 for a in range(1, row)] for a in range(1, col)]
    m2 = [[b+1 for b in range(1, row)] for b in range(1, col)]
    sum = [[m1[m][n] * m2[m][n] for n in range(len(m1))] for m in range(len(m2))]

    print(m1, '<-------1')
    print(m2, '<-------2')
    print()
    for x in m1:
        print(x)
    print()
    for y in m2:
        print(y)
    print()
    for i in sum:
        print(i)
Matrix(6, 6)

w = [[b for b in range(1, a+1)] for a in range(1, 5)]
print(w)


