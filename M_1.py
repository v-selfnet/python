#xx = [[10, 20, 30], [40, 50, 60], [70,80, 90]]
#print(xx)

def Matrix(row, col):
    m_1 = [[row for row in range(1,row)] for col in range(1,col)]
    m_2 = [[row for row in range(1,row)] for col in range(1,col)]
    sum = [[0 for row in range(1, row)] for col in range(1, col)]
    #sum = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for row in m_1:
        print(row)
    print()
    for row in m_2:
        print(row)
    print()
    # for row in sum:
    #     print(row)
    # print()
    # for m in range(len(m_1)):
    #     for n in range(len(m_2)):
    #         sum[m][n] = m_1[m][n] + m_2[m][n]
    sum = [[m_1[m][n] + m_2[m][n] for n in range(len(m_2))] for m in range(len(m_1))]
    for i in sum:
        print(i)
Matrix(4,4)


# Comprehension
print()

