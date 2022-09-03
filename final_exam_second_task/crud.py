import sys
from io import StringIO

input1 = '''. . . . . .
. 6 . . . .
G . S . t S
. . 10 . . .
. 95 . . 8 .
. . P . . .
(1, 1)
Create, down, r
Update, right, e
Create, right, a
Read, right
Delete, right
Stop
'''
input2 = """. . . . . .  
. 6 . . . .  
. T . D . O  
. . 10 A . .  
. 95 . 80 5 .  
. . P . t .   
(2, 3)
Create, down, o
Delete, right
Read, up
Create, left, 20
Update, up, P
Stop
"""
input3 = """H 8 . . . .
70 i . . . .
t . . . B .
50 . 16 . C .
. . . t . .
. 25 . . . .
(0, 0)
Read, right
Read, down
Read, left
Delete, down
Create, right, 10
Read, left
Stop
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

import re


def positions(row, col, direct):
    if direct == "left":
        return row, col - 1
    if direct == "right":
        return row, col + 1
    if direct == "up":
        return row - 1, col
    if direct == "down":
        return row + 1, col


def create_position(row, col, matrix, direction, value):
    if direction == "left" and matrix[row][col - 1] == ".":
        matrix[row][col - 1] = value
    if direction == "right" and matrix[row][col + 1] == ".":
        matrix[row][col + 1] = value
    if direction == "up" and matrix[row - 1][col] == ".":
        matrix[row - 1][col] = value
    if direction == "down" and matrix[row + 1][col] == ".":
        matrix[row + 1][col] = value
    return matrix


def update_position(row, col, matrix, direction, value):
    if direction == "left" and matrix[row][col - 1] != ".":
        matrix[row][col - 1] = value
    if direction == "right" and matrix[row][col + 1] != ".":
        matrix[row][col + 1] = value
    if direction == "up" and matrix[row - 1][col] != ".":
        matrix[row - 1][col] = value
    if direction == "down" and matrix[row + 1][col] != ".":
        matrix[row + 1][col] = value
    return matrix


def delete_position(row, col, matrix, direction):
    if direction == "left" and matrix[row][col - 1] != ".":
        matrix[row][col - 1] = "."
    if direction == "right" and matrix[row][col + 1] != ".":
        matrix[row][col + 1] = "."
    if direction == "up" and matrix[row - 1][col] != ".":
        matrix[row - 1][col] = "."
    if direction == "down" and matrix[row + 1][col] != ".":
        matrix[row + 1][col] = "."
    return matrix


def read_position(row, col, matrix, direction):
    if direction == "left" and matrix[row][col - 1] != ".":
        print(matrix[row][col - 1])
    if direction == "right" and matrix[row][col + 1] != ".":
        print(matrix[row][col + 1])
    if direction == "up" and matrix[row - 1][col] != ".":
        print(matrix[row - 1][col])
    if direction == "down" and matrix[row + 1][col] != ".":
        print(matrix[row + 1][col])


n = 6
matrix = []

for r in range(n):
    line = input().split()
    matrix.append(line)

# print(matrix)
row, col = tuple(map(int, re.findall(r'[0-9]+', input())))

command = input()

while command != "Stop":
    a_command = command.split(", ")
    if a_command[0] == "Create":
        direction = a_command[1]
        value = a_command[2]

        matrix = create_position(row, col, matrix, direction, value)
        row, col = positions(row, col, direction)

    elif a_command[0] == "Update":
        direction = a_command[1]
        value = a_command[2]

        matrix = update_position(row, col, matrix, direction, value)
        row, col = positions(row, col, direction)

    elif a_command[0] == "Delete":
        direction = a_command[1]

        matrix = delete_position(row, col, matrix, direction)
        row, col = positions(row, col, direction)

    elif a_command[0] == "Read":
        direction = a_command[1]

        read_position(row, col, matrix, direction)
        row, col = positions(row, col, direction)

    command = input()

for r in matrix:
    print(*r)

# first_player_won = False
# second_player_won = False
# turn = 1
# first_start_score = 501
# second_start_score = 501
#
#
# while first_start_score > 0 and second_start_score > 0:
#     coordinates = input()
#     row, col = tuple(map(int, re.findall(r'[0-9]+', coordinates)))
#     turn += 1
#
#     if turn % 2 == 0:
#         if not is_inside (row, col, matrix):
#             continue
#
#         if matrix[row][col] == "B":
#             first_player_won = True
#             break
#
#         elif matrix[row][col] == "D":
#             points = get_points(row, col, matrix, "D")
#
#         elif matrix[row][col] == "T":
#             points = get_points(row, col, matrix, "T")
#
#         else:
#             points = int(matrix[row][col])
#
#         first_start_score -= points
#
#
#     elif turn % 2 != 0:
#
#         if not is_inside(row, col, matrix):
#             continue
#
#         if matrix[row][col] == "B":
#             second_player_won = True
#             break
#
#         elif matrix[row][col] == "D":
#             points = get_points(row, col, matrix, "D")
#
#         elif matrix[row][col] == "T":
#             points = get_points(row, col, matrix, "T")
#
#         else:
#             points = int(matrix[row][col])
#
#         second_start_score -= points
#
# if first_player_won or first_start_score <=0:
#     print(f"{first_player} won the game with {turn//2} throws!")
#
# elif second_player_won or second_start_score <=0:
#     print(f"{second_player} won the game with {turn//2} throws!")
