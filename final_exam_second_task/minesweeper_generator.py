import sys
from io import StringIO

input1 = '''4
4
(0, 3)
(1, 1)
(2, 2)
(3, 0)
'''
input2 = """5
3
(1, 1)
(2, 4)
(4, 1)
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
import re

def is_inside(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)

def count_bombs(row, col, matrix):
    val = 0
    if is_inside(row, col+1, matrix) and matrix[row][col + 1] == "*":
        val += 1
    if is_inside(row, col-1, matrix) and matrix[row][col - 1] == "*":
        val += 1
    if is_inside(row-1, col, matrix) and matrix[row - 1][col] == "*":
        val += 1
    if is_inside(row+1, col, matrix) and matrix[row + 1][col] == "*":
        val += 1
    if is_inside(row-1, col-1, matrix) and matrix[row - 1][col - 1] == "*":
        val += 1
    if is_inside(row-1, col+1, matrix) and matrix[row - 1][col + 1] == "*":
        val += 1
    if is_inside(row+1, col-1, matrix) and matrix[row + 1][col - 1] == "*":
        val += 1
    if is_inside(row+1, col+1, matrix) and matrix[row + 1][col + 1] == "*":
        val += 1

    return val


size = int(input())
bombs = int(input())
matrix = []

for r in range(size):
    matrix.append(["0"] * size)


for _ in range(bombs):
    coordinates = input()
    row, col = tuple(map(int, re.findall(r'[0-9]+', coordinates)))
    matrix[row][col] = "*"

# print(matrix)
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == "0":
            matrix[r][c] = count_bombs(r, c, matrix)

    print(*matrix[r])
