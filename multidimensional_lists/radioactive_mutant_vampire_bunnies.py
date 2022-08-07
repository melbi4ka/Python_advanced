import sys
from io import StringIO

input1 = '''5 6
.....P
......
...B..
......
......
ULDDDR
'''
input2 = """4 5
.....
.....
.B...
...P.
LLLLLLLL
"""
input3 = """5 8
.......B
...B....
....B..B
........
..P.....
ULLL
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

def read_matrix(a):
    a_matrix = []

    for _ in range(a):
        rows = [x for x in input()]
        a_matrix.append(rows)
    return a_matrix


def get_next_pos(row, col, command):
    if command == "U":
        return row - 1, col
    elif command == "D":
        return row + 1, col
    elif command == "R":
        return row, col + 1
    elif command == "L":
        return row, col-1

def is_outside(row, col, rows, cols):
    return 0 > row or 0 > col or row >= rows or col >= cols

def get_children(row, col, rows, cols):
    possible_children = [
        [row, col + 1 ],
        [row, col - 1],
        [row + 1, col],
        [row - 1 , col],
    ]
    result = []
    for children_row, children_col in possible_children:
        if not is_outside(children_row, children_col, rows, cols):
            result.append([children_row, children_col])
    return result


rows, cols = [int(x) for x in input().split()]
matrix = read_matrix(rows)
# print(matrix)

bunnies = []
player_row = 0
player_col = 0


for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == "P":
            player_row = r
            player_col = c
        elif matrix[r][c] == "B":
            bunnies_row = r
            bunnies_col = c
            bunnies.append([bunnies_row, bunnies_col])

# print(bunnies)
# print(player_row)
# print(bunnies)

commands = input()
is_win = False
is_dead = False


for command in commands:
    matrix[player_row][player_col] = "."
    next_row, next_col = get_next_pos(player_row, player_col, command)
    if is_outside(next_row, next_col, rows, cols):
        is_win = True

    else:
        if matrix[next_row][next_col] == ".":
            # matrix[player_row][player_col] = "."
            player_row, player_col = next_row, next_col
            matrix[player_row][player_col] = "P"
        elif matrix[next_row][next_col] == "B":
            is_dead = True
            player_row, player_col = next_row, next_col

    new_bunnies = []
    for bunnies_row, bunnies_col in bunnies:
        bunnies_children = get_children(bunnies_row, bunnies_col, rows, cols)
        new_bunnies.extend(bunnies_children)
        for child_row, child_col in bunnies_children:
            matrix[child_row][child_col] = "B"
            if matrix[child_row][child_col] == matrix[player_row][player_col]:
                is_dead = True

    bunnies = new_bunnies

    if is_dead or is_win:
        break

for r in matrix:
    print(*r, sep = "")

if is_win:
    print(f"won: {player_row} {player_col}")
if is_dead:
    print(f"dead: {player_row} {player_col}")






