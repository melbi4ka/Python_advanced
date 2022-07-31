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
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

from collections import deque


def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


size = int(input())
commands = deque([x for x in input().split()])

field = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

expected_coals = 0
coals = 0
currRow = -1  # следи позиция на s
currCol = -1  # следи позиция на s

for row in range(size):
    field.append(input().split())

for row2 in range(len(field)):
    for col2 in range(len(field)):
        if field[row2][col2] == "c":
            expected_coals += 1

for row in range(len(field)):  # намира позиция на s
    for col in range(len(field)):
        if field[row][col] == "s":
            currRow = row
            currCol = col

while commands:
    if commands:
        current_command = commands.popleft()
        new_row = currRow + directions[current_command][0]
        new_col = currCol + directions[current_command][1]
        if is_in_range(new_row, new_col, size):
            if field[new_row][new_col] == "*":
                field[currRow][currCol], field[new_row][new_col] = "*", "s"
            elif field[new_row][new_col] == "e":
                print(f"Game over! ({new_row}, {new_col})")
                quit()  # трябва да спре програмата
            elif field[new_row][new_col] == "c":
                coals += 1
                field[currRow][currCol], field[new_row][new_col] = "*", "s"
            currRow = new_row
            currCol = new_col
if coals == expected_coals:
    print(f"You collected all coal! ({currRow}, {currCol})")
else:
    print(f"{expected_coals - coals} pieces of coal left. ({currRow}, {currCol})")
