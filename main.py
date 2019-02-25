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

display(screen)
