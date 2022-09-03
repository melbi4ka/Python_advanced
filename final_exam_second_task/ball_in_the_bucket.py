import re
import sys
from io import StringIO

input1 = '''10 30 B 4 20 24
7 8 27 23 11 19
13 3 14 B 17 В
12 5 21 22 9 6
B 26 1 28 29 2
25 B 16 15 B 18
(1, 1)
(20, 15)
(4, 0)
'''
input2 = """B 30 14 23 20 24
29 8 27 18 11 19
13 3 B B 17 6
28 5 21 22 9 B
10 B 26 12 B 2
25 1 16 15 7 4
(0, 0)
(2, 2)
(2, 3)
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
import re

def sum_column(col, matrix):
    res = 0
    if matrix[0][col] != "B":
        res += int(matrix[0][col])
    if matrix[1][col] != "B":
        res += int(matrix[1][col])
    if matrix[2][col] != "B":
        res += int(matrix[2][col])
    if matrix[3][col] != "B":
        res += int(matrix[3][col])
    if matrix[4][col] != "B":
        res += int(matrix[4][col])
    if matrix[5][col] != "B":
        res += int(matrix[5][col])

    return res

def is_inside(row, col, matrix):
    return 0 <= row < len(matrix) and 0<= col < len(matrix)


n = 6
matrix = []
for r in range(n):
    line = input().split()
    matrix.append(line)

# print(matrix)
all_sum = 0

for _ in range(3):
    coordinates = input()
    row, col = tuple(map(int, re.findall(r'[0-9]+', coordinates)))

    if not is_inside(row,col,matrix):
        continue

    if matrix[row][col] == "X":
        continue

    if matrix[row][col] == "B":
        all_sum += sum_column(col, matrix)
        matrix[row][col] = "X"

toy_dict = {
    "Football": list(range(100, 200)),
    "Teddy Bear": list(range(200, 300)),
    "Lego Construction Set": list(range(300, 800))
}
for key in toy_dict:
    if all_sum in toy_dict[key]:
        print(f"Good job! You scored {all_sum} points, and you've won {key}.")
        break
else:
    print(f"Sorry! You need {100 - all_sum} points more to win a prize.")
