import sys
from io import StringIO

input1 = '''5
4
- X V -
- S - V
- - - -
X - - -
up
right
down
right
Christmas morning
'''
input2 = """3
4
- - - -
V - X -
- V C V
- - - S
left
up
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

def next_position (command, row, col):
    if command == "right":
        return row, col+1
    elif command == "left":
        return row, col-1
    elif command == "up":
        return row-1, col
    elif command == "down":
        return row+1, col

def is_inside (row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col <= len(matrix)

def get_neighbours (matrix, row, col):
    result = []
    if is_inside(row, col -1, matrix) and matrix[row][col - 1] == "V" or matrix[row][col - 1] == "X":
        result.append([row, col -1])
    if is_inside(row, col + 1, matrix) and matrix[row][col + 1] == "V" or matrix[row][col + 1] == "X":
        result.append([row, col+1])
    if is_inside(row -1, col, matrix) and matrix[row - 1][col] == "V" or matrix[row - 1][col] == "X":
        result.append([row - 1, col])
    if is_inside(row + 1, col, matrix) and matrix[row + 1][col] == "V" or matrix[row + 1][col] == "X":
        result.append([row + 1, col])
    return result

presents = int(input())
n = int(input())
matrix = []
good_guys = 0
santa_row = 0
santa_col = 0
gifted_good_guys = 0

for i in range(n):
    line = input().split()
    matrix.append(line)
    for j in range(n):
        if line[j] == "S":
            santa_row = i
            santa_col = j
        elif line[j] == "V":
            good_guys += 1


command = input()
while True:
    if command == "Christmas morning":
        break
    direction = command

    matrix[santa_row][santa_col] = "-"
    santa_row,  santa_col = next_position(direction, santa_row, santa_col)

    if matrix[santa_row][santa_col] == "V":
        presents -= 1
        gifted_good_guys += 1
        matrix[santa_row][santa_col] = "S"

    elif matrix[santa_row][santa_col] == "C":
        matrix[santa_row][santa_col] = "S"
        neighbour_kids = get_neighbours(matrix, santa_row, santa_col)
        for n_row, n_col in neighbour_kids:
            if matrix[n_row][n_col] == "V":
                gifted_good_guys += 1
                if presents == 0:
                    break

            presents -= 1
            matrix[n_row][n_col] = "-"

    if presents == 0:
        break

    command = input()



# print(good_guys)
# print(gifted_good_guys)
if not presents and good_guys != gifted_good_guys:
    print(f"Santa ran out of presents!")

for j in range(n):
    print(*matrix[j])

if good_guys == gifted_good_guys:
    print(f"Good job, Santa! {gifted_good_guys} happy nice kid/s.")
else:
    print(f"No presents for {good_guys-gifted_good_guys} nice kid/s.")
