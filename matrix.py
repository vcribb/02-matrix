import math

def print_matrix(matrix):
    output = ""
    for num in range(len(matrix[0])):
        for item in matrix:
            output+=str(item[num])+" "
        output+="\n"
    print(output)
    pass

def ident(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if row == col:
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0
    pass

def matrix_mult(m1, m2):
    ans = [[],[],[],[]]
    for r in range(4):
        for c in range(len(m2)):
            entry = 0
            for num in range(4):
                entry += m1[r][num] * m2[num][c]
            ans[r].append(entry)
    for row in range(4):
        for col in range(len(m2)):
            m2[row][col] = ans[row][col]
    pass

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

