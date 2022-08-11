import sys
from io import StringIO

input1 = '''. . . . . 
x . . . . 
. A . . . 
. . . x . 
. x . . x 
3
shoot down
move right 4
move left 1
'''
input2 = """. . . . . 
. . . . . 
. A x . . 
. x . . . 
. x . . . 
2
shoot down
shoot right
"""

input3 = """. . . . . 
. . . . . 
. . x . . 
. . . . . 
. x . . A 
3
shoot down
move right 2
shoot left
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


def move_position (row, col, value, command):
    if command == "right":
        return row, col + value
    elif command == "left":
        return row, col - value
    elif command == "up":
        return row - value, col
    elif command == "down":
        return row + value, col


def is_inside(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def shooting(row, col, matrix, direction):
    targets = []
    directions = {
        "left": lambda r,c: (r, c-1),
        "right": lambda r,c: (r, c+1),
        "up": lambda r,c: (r-1, c),
        "down": lambda r,c: (r+1, c)
    }
    row, col = directions[direction](row, col)
    while is_inside(row, col, matrix):
        if matrix[row][col] == "x":
            matrix[row][col] = "."
            targets.append([row,col])
            break
        row, col = directions[direction](row, col)
    return targets


matrix = []
range_row = 0
range_col = 0
all_targets = 0

for i in range (5):
    line = input().split()
    matrix.append(line)
    for j in range(5):
        if line[j] == "A":
            range_row = i
            range_col = j
        elif line[j] == "x":
            all_targets += 1

n = int(input())
all_coordinates = []

for _ in range (n):
    command = input().split()
    action, direction = command[:2]

    if action == "move":
        steps = int(command[2])
        next_row, next_col = move_position(range_row, range_col, steps, direction)

        if is_inside (next_row, next_col, matrix) and matrix[next_row][next_col] == ".":
            range_row, range_col = next_row, next_col

    elif action == "shoot":
        targets = shooting(range_row, range_col, matrix, direction)
        all_targets -= len(targets)
        if targets:
            all_coordinates.extend(targets)

    if all_targets == 0:
        break

if not all_targets:
    print(f"Training completed! All {len(all_coordinates)} targets hit.")
else:
    print(f"Training not completed! {all_targets} targets left.")

for el in all_coordinates:
    print(el)
