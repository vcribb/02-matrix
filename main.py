from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [20, 255, 239]
matrix = new_matrix()

for num in range(25):
    temp = num*10
    add_edge(matrix, temp, temp, 0, 500-temp, temp, 0)
    add_edge(matrix, temp, temp, 0, temp, 500-temp, 0)
    add_edge(matrix, 500-temp, temp, 0, 500-temp, 500-temp, 0)
    add_edge(matrix, temp, 500-temp, 0, 500-temp, 500-temp, 0)

draw_lines(matrix, screen, color)
matrix = new_matrix()
color = [188, 255, 210]

for num in range(25):
    temp = num*10
    add_edge(matrix, temp, 250, 0, 250, 500-temp, 0)
    add_edge(matrix, 250, 500-temp, 0, 500-temp, 250, 0)
    add_edge(matrix, 500-temp, 250, 0, 250, temp, 0)
    add_edge(matrix, 250, temp, 0, temp, 250, 0)

draw_lines(matrix, screen, color)

matrix = new_matrix(0, 0)
add_edge(matrix, 1, 1, 0, 2, 2, 0)
add_edge(matrix, 3, 3, 0, 4, 4, 0)
print('Testing add_edge method:')
print_matrix(matrix)

ident(matrix)
print('Testing ident method:')
print_matrix(matrix)

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if r == c:
            matrix[r][c] = 2

temp = [[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4], [5, 6, 7, 8]]
matrix_mult(temp, matrix)
print('Testing matrix_mult method:')
print_matrix(matrix)

display(screen)
