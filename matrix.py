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
    if len(m1[0]) != len(m2):
        pass
    rows = []
    for y in range(len(m1[0])):
        row = []
        for x in range(len(m1)):
            row.append(m1[x][y])
        rows.append(row)
    ans = []
    for row in range(len(rows)):
        tempRow = []
        for col in range(len(m2)):
            temp = 0
            for num in range(len(rows[row])):
                temp+=rows[row][num]*m2[col][num]
            tempRow.append(temp)
        ans.append(tempRow)
    temp = []
    for y in range(len(ans[0])):
        row = []
        for x in range(len(ans)):
            row.append(ans[x][y])
        temp.append(row)
    print_matrix(temp)
    pass

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
