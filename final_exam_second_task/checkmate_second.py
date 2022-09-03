import re
import sys
from io import StringIO

input1 = '''. . . . . . . .
Q . . . . . . .
. K . . . Q . .
. . . Q . . . .
Q . . . Q . . .
. Q . . . . . .
. . . . . . Q .
. Q . Q . . . .
'''
input2 = """. . . . . . . .
. . . Q . . . .
. . . . . . . .
. . . . . . . .
Q . . . Q . . .
. . K . . . . .
. . . . . . Q .
. . . Q . . . .
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

def is_inside(a_row, a_col, matrix):
    return 0<= a_row < len(matrix) and 0 <= a_col < len(matrix)

def opposite_king(a_row, a_col, matrix):
    can_capture = []

    directions = {
        "right": lambda r, c: (r, c + 1),
        "left": lambda r, c: (r, c - 1),
        "up": lambda r, c: (r - 1, c),
        "down": lambda r, c: (r + 1, c),
        "up left": lambda r, c: (r - 1, c - 1),
        "up right": lambda r, c: (r - 1, c + 1),
        "down left": lambda r, c: (r + 1, c - 1),
        "down right": lambda r, c: (r + 1, c + 1),
    }

    for key in directions:
        row, col = directions[key](a_row, a_col)
        while is_inside(row, col, matrix):
            if matrix[row][col] == "Q":
                can_capture.append([row, col])
                break
            row, col = directions[key](row, col)

    return can_capture


n = 8
matrix = []
king_row = 0
king_col = 0

for r in range(n):
    line = input().split()
    matrix.append(line)
    for c in range(len(line)):
        if line[c] == "K":
            king_row = r
            king_col = c

# print(matrix)
# print(king_row, king_col)
capturing_king = opposite_king(king_row, king_col, matrix)
if capturing_king:
    for el in capturing_king:
        print(el)
else:
    print(f"The king is safe!")
