import sys
from io import StringIO

input1 = '''5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
left
right
right
up
up
right
'''

input2 = """8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
up
down
up
left
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

from math import floor

def is_in_matrix(row,col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)

def next_step(a_row, a_col, a_command):
    if a_command == "down":
        return a_row+1, a_col
    elif a_command == "up":
        return a_row - 1, a_col
    elif a_command == "left":
        return a_row, a_col - 1
    elif a_command == "right":
        return a_row, a_col + 1

def oposite_side(row, col, matrix, direction):
    if direction == "left":
        return row, n-1
    elif direction == "right":
        return row, 0
    elif direction == "up":
        return n-1, col
    elif direction == "down":
        return 0, col


n = int(input())
player_row = 0
player_col = 0
matrix = []

for r in range(n):
    line = input().split()
    matrix.append(line)
    for c in range(len(line)):
        if line[c] == "P":
            player_row = r
            player_col = c

# print(matrix)
# print(player_row)
# print(player_col)
coins = 0
path = [(player_row, player_col)]
matrix[player_row][player_col] = 0
is_wall = False

while coins < 100:
    command = input()

    player_row, player_col = next_step(player_row, player_col, command)

    if not is_in_matrix(player_row, player_col, matrix):
        player_row, player_col = oposite_side(player_row, player_col, matrix, command)

    path.append((player_row, player_col))

    if matrix[player_row][player_col] == "X":
        is_wall = True
        break

    elif matrix[player_row][player_col] != "X":
        coin = int(matrix[player_row][player_col])
        coins += coin
        matrix[player_row][player_col] = 0

# print(coins)
# print(path)

if is_wall:
    coins = floor(coins / 2)
    print(f"Game over! You've collected {coins} coins.")
else:
    print(f"You won! You've collected {coins} coins.")
print(f"Your path:")
for el in path:
    print(f"[{el[0]}, {el[1]}]")
