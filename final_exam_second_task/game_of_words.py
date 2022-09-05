import sys
from io import StringIO

input1 = '''Hello
4
P---
Mark
-l-y
--e-
4
down
right
right
right
'''
input2 = """Initial
5
-----
t-r--
--Pa-
--S--
z--t-
4
up
left
left
left
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

def next_step(row, col, command):
    if command == "right":
        return row, col+1
    elif command == "left":
        return row, col-1
    elif command == "up":
        return row-1, col
    elif command == "down":
        return row+1, col

def is_inside(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)

text = input()
n = int(input())
matrix = []
player_row = 0
player_col = 0

for r in range(n):
    line = list(input())
    matrix.append(line)
    for c in range(len(line)):
        if line[c] == "P":
            player_row = r
            player_col = c

# print(matrix)
# print(player_row, player_col)
m = int(input())

for _ in range(m):
    command = input()
    next_row, next_col = next_step(player_row, player_col, command)

    if is_inside(next_row, next_col, matrix):
        if matrix[next_row][next_col].isalpha():
            text = text + matrix[next_row][next_col]
        matrix[next_row][next_col] = "P"
        matrix[player_row][player_col] = "-"
        player_row, player_col = next_row, next_col

    else:
        next_row, next_col = player_row, player_col
        text = text[:-1]

print(text)
for r in matrix:
    print("".join(r))

# чета си матрицата и си изкравам къде ми плеър реда и колоната
# един фор цикъл да чета команди за движение
# на функция подавам плейр рола и кола и получавам следващите рол и кол -
# функцията е стандартна за движение в посока с една стъпка
# ако следващите координати са вътре - проверявам с функция
# ако са букви ги добавям към първоначалния текст„
# матрицата на следващите рол и кол става равна на P
# там където съм била - на плеър рола и кола става равно на -
# суапвам плеър рола и кола със следващия рол и кол
# ако не съм вътре в матрицата -
# текста ми става равен на текста без последната буква















