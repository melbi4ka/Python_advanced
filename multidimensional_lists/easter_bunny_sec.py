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

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
import sys

def is_inside(row, col, mtrx):
    return 0 <= row < len(matrix) and 0<= col < len(matrix)


n = int(input())
matrix = []
bunny_row = 0
bunny_col = 0

for r in range(n):
    el = list(input().split())
    matrix.append(el)
    for c in range(n):
        if matrix[r][c] == "B":
            bunny_row = r
            bunny_col = c

directions = {
    "left": lambda r,c: (r, c-1),
    "right": lambda r,c: (r, c+1),
    "up": lambda r,c: (r-1, c),
    "down": lambda r,c: (r+1, c)
}
best_sum = -sys.maxsize
direction = None
best_path = None

for key in directions:
    sum = 0
    path = []
    next_row, next_col = directions[key](bunny_row, bunny_col)

    while is_inside(next_row, next_col, matrix) and matrix[next_row][next_col] != "X":
        sum += int(matrix[next_row][next_col])
        path.append([next_row, next_col])
        next_row, next_col = directions[key](next_row, next_col)

    if sum > best_sum and path:
        direction = key
        best_path = path
        best_sum = sum

print(direction)
print(*best_path, sep="\n")
print(best_sum)

