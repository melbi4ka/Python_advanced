import sys
from io import StringIO

input1 = '''5
up right right up right
* * * c *
* * * e *
* * c * *
s * * c *
* * c * *
'''
input2 = """4
up right right right down
* * * e
* * c *
* s * c
* * * *
"""
input3 = """6
left left down right up left left down down down
* * * * * *
e * * * c *
* * c s * *
* * * * * *
c * * * c *
* * c * * *
"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

from collections import deque

def next_step(a_row, a_col, a_command):
    if a_command == "down":
        return a_row+1, a_col
    elif a_command == "up":
        return a_row - 1, a_col
    elif a_command == "left":
        return a_row, a_col - 1
    elif a_command == "right":
        return a_row, a_col + 1

def is_inside (row, col, a_matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


size = int(input())
queue = deque([x for x in input().split()])
# print(queue)
matrix = []
miner_row = 0
miner_col = 0
coal = 0

for r in range(size):
    line = input().split()
    matrix.append(line)
    for c in range(len(line)):
        if line[c] == "s":
            miner_row = r
            miner_col = c
        elif line[c] == "c":
            coal += 1

is_over = False
while queue:
    direction = queue.popleft()

    next_row, next_col = next_step(miner_row, miner_col, direction)

    if is_inside(next_row, next_col, matrix):
        miner_row, miner_col = next_row, next_col

    else:
        continue

    if matrix[miner_row][miner_col] == "e":
        is_over = True
        break
    elif matrix[miner_row][miner_col] == "c":
        coal -= 1
        matrix[miner_row][miner_col] = "*"

        if coal == 0:
            break


if not coal:
    print(f"You collected all coal! ({miner_row}, {miner_col})")
elif is_over:
    print(f"Game over! ({miner_row}, {miner_col})")
else:
    print(f"{coal} pieces of coal left. ({miner_row}, {miner_col})")
