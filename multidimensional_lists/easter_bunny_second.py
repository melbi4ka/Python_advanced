import sys
from io import StringIO

input1 = '''5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0
'''
input2 = """8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

def right_direction(matrix, row, col):
    sum_right = 0
    path_right = []
    while col + 1 < len(matrix):
        if matrix[row][col+1] != "X":
            sum_right += int(matrix[row][col + 1])
            path_right.append([row, col + 1])
            col += 1
        else:
            break

    return sum_right, path_right

def left_direction(matrix, row, col):
    sum_left = 0
    path_left = []
    while col - 1 > -1:
        if matrix[row][col-1] != "X":
            sum_left += int(matrix[row][col - 1])
            path_left.append([row, col - 1])
            col -= 1
        else:
            break

    return sum_left, path_left

def up_direction(matrix, row, col):
    sum_up = 0
    path_up = []
    while row - 1 > -1:
        if matrix[row-1][col] != "X":
            sum_up += int(matrix[row-1][col])
            path_up.append([row-1, col])
            row -= 1
        else:
            break

    return sum_up, path_up


def down_direction(matrix, row, col):
    sum_down = 0
    path_down = []
    while row + 1 < len(matrix):
        if matrix[row+1][col] != "X":
            sum_down += int(matrix[row+1][col])
            path_down.append([row+1, col])
            row += 1
        else:
            break

    return sum_down, path_down


n = int(input())
matrix = []

bunny_row = 0
bunny_col = 0

for r in range(n):
    el = input().split()
    matrix.append(el)
    for c in range(n):
        if el[c] == "B":
            bunny_row = r
            bunny_col = c

# print(matrix)
# print(bunny_row, bunny_col)


right_sum, right_path = right_direction(matrix, bunny_row, bunny_col)
left_sum, left_path = left_direction(matrix, bunny_row, bunny_col)
up_sum, up_path = up_direction(matrix, bunny_row, bunny_col)
down_sum, down_path = down_direction(matrix, bunny_row, bunny_col)

best_sum = float("-inf")
best_coordinates = None
best_direction = ""
if right_sum > best_sum and right_path:
    best_sum = right_sum
    best_coordinates = right_path
    best_direction = "right"

if left_sum > best_sum and left_path:
    best_sum = left_sum
    best_coordinates = left_path
    best_direction = "left"

if up_sum > best_sum and up_path:
    best_sum = up_sum
    best_coordinates = up_path
    best_direction = "up"

if down_sum > best_sum and down_path:
    best_sum = down_sum
    best_coordinates = down_path
    best_direction = "down"

print(best_direction)
print(*best_coordinates, sep="\n")
print(best_sum)
