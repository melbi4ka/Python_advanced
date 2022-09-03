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

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

def opposite_king(a_row, a_col, matrix):
    can_capture = []
    col = a_col
    row = a_row

    while col < len(matrix):
        if matrix[row][col] == "Q":
            can_capture.append([row, col])
            break
        col += 1

    col = a_col
    row = a_row
    while col >= 0:
        if matrix[row][col] == "Q":
            can_capture.append([row, col])
            break
        col -= 1

    col = a_col
    row = a_row
    while row < len(matrix):
        if matrix[row][col] == "Q":
            can_capture.append([row, col])
            break
        row += 1

    col = a_col
    row = a_row
    while row >= 0:
        if matrix[row][col] == "Q":
            can_capture.append([row, col])
            break
        row -= 1

    col = a_col
    row = a_row
    while row < len(matrix) and col < len(matrix):
        if matrix[row][col] == "Q":
            can_capture.append([row, col])
            break
        row += 1
        col += 1

    col = a_col
    row = a_row
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == "Q":
            can_capture.append([row, col])
            break
        row += 1
        col -= 1

    col = a_col
    row = a_row
    while row >= 0 and col >= 0:
        if matrix[row][col] == "Q":
            can_capture.append([row, col])
            break
        row -= 1
        col -= 1

    col = a_col
    row = a_row
    while row >= 0 and col < len(matrix):
        if matrix[row][col] == "Q":
            can_capture.append([row, col])
            break
        row -= 1
        col += 1

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
