import sys
from io import StringIO

input1 = '''5 
0K0K0
K000K
00K00
K000K
0K0K0
'''
input2 = """2
KK
KK
"""
input3 = """8
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK
"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

def get_count(matrix, row, col):
    possible_children_cords = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1 , col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1],
    ]

    hit_count = 0
    for child_row, child_col in possible_children_cords:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix):
            if matrix[child_row][child_col] == "K":
                hit_count += 1

    return hit_count

n = int(input())
matrix = []

for _ in range (n):
    line = [x for x in input()]
    matrix.append(line)

removed_knight = 0

while True:
    best_count = 0
    knight_row = 0
    knight_col = 0

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "K":
                row = r
                col = c
                count = get_count(matrix, row, col)

                if count > best_count:
                    best_count = count
                    knight_row = row
                    knight_col = col

    if best_count == 0:
        break

    matrix[knight_row][knight_col] = "0"
    removed_knight += 1

print(removed_knight)
