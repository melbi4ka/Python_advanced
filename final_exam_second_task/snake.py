import sys
from io import StringIO

input1 = '''6
-----S
----B-
------
------
--B---
--*---
left
down
down
down
left
'''
input2 = """7
--***S-
--*----
--***--
---**--
---*---
---*---
---*---
left
left
left
down
down
right
right
down
left
down
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

def snake_move(row, col, matrix, command):
    if command == "left":
        return row, col-1
    elif command == "right":
        return row, col+1
    elif command == "up":
        return  row-1, col
    elif command == "down":
        return row+1, col

def is_inside(row, col,  matrix):
    return 0<= row < len(matrix) and 0 <= col < len(matrix)

def opposite_burrow(matrix):
    a_row = 0
    a_col = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "B":
                a_row = r
                a_col = c
    return a_row, a_col



size = int(input())
matrix = []
snake_row = 0
snake_col = 0

for r in range(size):
    line = list(input())
    matrix.append(line)
    for c in range(size):
        if line[c] == "S":
            snake_row = r
            snake_col = c

# print(matrix)
# print(snake_row, snake_col)

food = 0
outside = False
command = input()

while food < 10:

    next_row, next_col = snake_move(snake_row, snake_col,matrix, command)
    matrix[snake_row][snake_col] = "."
    if is_inside(next_row, next_col, matrix):
        snake_row,snake_col = next_row, next_col
        if matrix[snake_row][snake_col] == "*":
            matrix[snake_row][snake_col] = "S"
            food += 1
            if food == 10:
                break

        elif matrix[snake_row][snake_col] == "-":
            matrix[snake_row][snake_col] = "S"

        elif matrix[snake_row][snake_col] == "B":
            matrix[snake_row][snake_col] = "."
            snake_row,snake_col = opposite_burrow(matrix)

    else:
        outside = True
        print("Game over!")
        break

    command = input()

if not outside:
    print("You won! You fed the snake.")
print(f"Food eaten: {food}")
for r in matrix:
    print(*r, sep="")
