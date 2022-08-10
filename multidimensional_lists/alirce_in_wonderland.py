import sys
from io import StringIO

input1 = '''5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left
'''
input2 = """7
. A . 1 1 . .
9 . . . 6 . 5
. 6 . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2
left
down
down
right
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
def right_direction(matrix, row, col, count):
    next_move = matrix[row][col + 1]
    is_hole = False
    is_inside = False
    if 0 <= row < len(matrix) and 0 <= col+1 < len(matrix) :
        is_inside = True
        if next_move == ".":
            matrix[row][col + 1] = "*"
        elif next_move == "*":
            pass
        elif next_move == "R":
            matrix[row][col+1] = "*"
            is_hole = True
        else:
            count += int(matrix[row][col + 1])
            matrix[row][col + 1] = "*"

    return matrix, count, is_hole, is_inside

def down_direction(matrix, row, col, count):
    next_move = matrix[row+1][col]
    is_hole = False
    is_inside = False
    if 0 <= row+1 < len(matrix) and 0 <= col < len(matrix):
        is_inside = True
        if next_move == ".":
            matrix[row+1][col] = "*"
        elif next_move == "*":
            pass
        elif next_move == "R":
            matrix[row + 1][col] = "*"
            is_hole = True
        else:
            count += int(matrix[row+1][col])
            matrix[row+1][col] = "*"

    return matrix, count, is_hole, is_inside

def up_direction(matrix, row, col, count):
    next_move = matrix[row-1][col]
    is_hole = False
    is_inside = False
    if 0 <= row-1 < len(matrix) and 0<= col < len(matrix):
        is_inside = True
        if next_move == ".":
            matrix[row-1][col] = "*"
        elif next_move == "*":
            pass
        elif next_move == "R":
            matrix[row - 1][col] = "*"
            is_hole = True
        else:
            count += int(matrix[row-1][col])
            matrix[row-1][col] = "*"

    return matrix, count, is_hole, is_inside

def left_direction(matrix, row, col, count):
    next_move = matrix[row][col-1]
    is_hole = False
    is_inside = False
    if 0 <= row < len(matrix) and 0 <= col-1 < len(matrix):
        is_inside = True
        if next_move == ".":
            matrix[row][col-1] = "*"
        elif next_move == "*":
            pass
        elif next_move == "R":
            matrix[row][col - 1] = "*"
            is_hole = True
        else:
            count += matrix[row][col-1]
            matrix[row][col-1] = "*"

    return matrix, count, is_hole, is_inside



n = int(input())
matrix = []
alice_row = 0
alice_col = 0

for i in range (n):
    line = input().split()
    matrix.append(line)
    for j in range(n):
        if line[j] == "A":
            alice_row = i
            alice_col = j
            matrix[alice_row][alice_col] = "*"


# print(matrix)
tea_bags = 0
rabbit_hole = False
in_field = False

while tea_bags < 10:
    command = input()

    if command == "right":
        matrix, tea_bags, rabbit_hole, in_field = right_direction(matrix, alice_row, alice_col, tea_bags)
        alice_col += 1

    elif command == "down":
        matrix, tea_bags, rabbit_hole, in_field = down_direction(matrix, alice_row, alice_col, tea_bags)
        alice_row += 1

    elif command == "up":
        matrix, tea_bags, rabbit_hole, in_field = up_direction(matrix, alice_row, alice_col, tea_bags)
        alice_row -= 1

    elif command == "left":
        matrix, tea_bags, rabbit_hole, in_field = left_direction(matrix, alice_row, alice_col, tea_bags)
        alice_col -= 1

    if not in_field:
        break

    if rabbit_hole:
        break


if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for r in matrix:
    print(*r, sep = " ")

# 55/100


