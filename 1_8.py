def zero_mat(m1):
    row = set()
    col = set()
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if m1[i][j] == 0:
                row.add(i)
                col.add(j)
    for i in row:
        m1[i] = 0 * len(m1[0])
    for i in col:
        for j in range(len(m1[0])):
            m1[i][j] = 0
    return m1
