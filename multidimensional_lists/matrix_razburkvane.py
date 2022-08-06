import sys
from io import StringIO

input1 = '''2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END
'''
input2 = """1 2
Hello World
0 0 0 1
swap 0 0 0 1
swap 0 1 0 0
END
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)


def read_matrix(a):
    a_matrix = []

    for _ in range(a):
        rows = input().split()
        a_matrix.append(rows)
    return a_matrix


row, col = [int(x) for x in input().split()]
matrix = read_matrix(row)
# print(matrix)
# line = input()

while True:
    action = input()
    if action == "END":
        break

    actions = action.split()

    if actions[0] != "swap" or len(actions) != 5:
        print("Invalid input!")
        continue

    row_one, col_one, row_two, col_two = [int(x) for x in actions[1:]]

    if 0 < row_one < row or 0 < row_two < row or 0< col_one < col or 0 < col_two < col:
        matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
        for i in range(row):
            print(f"{' '.join(matrix[i])}")
    else:
        print("Invalid input!")
        continue



