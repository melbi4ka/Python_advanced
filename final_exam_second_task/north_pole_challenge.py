import sys
from io import StringIO

input1 = '''6, 5
. . . . .
C . . G .
. C . . .
G . . C .
. D . . D
Y . . . G
left-3
up-1
left-2
right-7
up-1
End
'''
input2 = """5, 6
. . . . . .
. . . . . .
Y C D D . .
. . . C . .
. . . C . .
right-3
down-3
"""
input3 = """5, 2
. .
. .
. Y
. .
. G
up-1
left-11
down-10
End
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

def make_steps(row, col, a_direction):
    if a_direction == "left":
        return row, col - 1
    elif a_direction == "right":
        return row, col + 1
    elif a_direction == "up":
        return row - 1, col
    elif a_direction == "down":
        return row + 1, col

def is_outside(row, col, matrix_rows, matrix_columns):
    return 0 > row or row >= matrix_rows or 0 > col or col >= matrix_columns

def opposite_side(row, col, a_direction, matrix_row, matrix_columns):
    if a_direction == "left":
        return row, matrix_columns - 1
    elif a_direction == "right":
        return row, 0
    elif a_direction == "up":
        return matrix_row-1, col
    elif a_direction == "down":
        return 0, col

rows, columns = map(int, input().split(", "))
matrix = []
santa_row = 0
santa_col = 0
decoration = 0
gifts = 0
cookie = 0

for r in range(rows):
    line = input().split()
    matrix.append(line)
    for c in range(columns):
        if line[c] == "Y":
            santa_row = r
            santa_col = c
        if line[c] == "D":
            decoration += 1
        if line[c] == "G":
            gifts += 1
        if line[c] == "C":
            cookie += 1

# print(matrix)
command = input()
is_collect = False
collected_decoration = 0
collected_gift = 0
collected_cookie = 0


while command != "End":
    direction, steps = command.split("-")
    steps = int(steps)
    matrix[santa_row][santa_col] = "x"

    while steps > 0:
        santa_row,santa_col = make_steps(santa_row, santa_col, direction)
        if is_outside(santa_row,santa_col,rows, columns):
            santa_row, santa_col = opposite_side(santa_row,santa_col,direction, rows, columns)
        if matrix[santa_row][santa_col] == "D":
            collected_decoration += 1
            matrix[santa_row][santa_col] = "x"
        elif matrix[santa_row][santa_col] == "G":
            collected_gift += 1
            matrix[santa_row][santa_col] = "x"
        elif matrix[santa_row][santa_col] == "C":
            collected_cookie += 1
            matrix[santa_row][santa_col] = "x"
        elif matrix[santa_row][santa_col] == ".":
            matrix[santa_row][santa_col] = "x"

        steps -= 1

        if decoration == collected_decoration and gifts == collected_gift\
                and cookie == collected_cookie:
            print("Merry Christmas!")
            is_collect = True
            matrix[santa_row][santa_col] = "Y"
            break

    if is_collect:
        break

    matrix[santa_row][santa_col] = "Y"
    command = input()

print("You've collected:")
print(f"- {collected_decoration} Christmas decorations")
print(f"- {collected_gift} Gifts")
print(f"- {collected_cookie} Cookies")

for r in range(len(matrix)):
    print(*matrix[r])
