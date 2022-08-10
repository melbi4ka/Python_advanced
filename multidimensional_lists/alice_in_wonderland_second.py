import sys
from io import StringIO

input1 = '''5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
up
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

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

def next_position (command, row, col):
    if command == "right":
        return row, col+1
    elif command == "left":
        return row, col-1
    elif command == "up":
        return row-1, col
    elif command == "down":
        return row+1, col

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


while tea_bags < 10:
    command = input()
    next_row, next_col = next_position(command, alice_row, alice_col)

    if not 0 <= next_row < len(matrix) or not 0 <= next_col < len(matrix):
        break

    if matrix[next_row][next_col] == "*":
        pass
    elif matrix[next_row][next_col] == ".":
        matrix[next_row][next_col] = "*"
    elif matrix[next_row][next_col] == "R":
        matrix[next_row][next_col] = "*"
        break
    else:
        tea_bags += int(matrix[next_row][next_col])
        matrix[next_row][next_col] = "*"


    alice_row,alice_col = next_row, next_col


if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for r in matrix:
    print(*r, sep = " ")

