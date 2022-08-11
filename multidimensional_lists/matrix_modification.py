import sys
from io import StringIO

input1 = '''3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
'''
input2 = """4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

def valid_coordinates (row, col, matrix):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False

rows = int(input())
matrix = []

for _ in range(rows):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

# print(matrix)
a_command = input()
while a_command != "END":
    command = a_command.split()
    action = command[0]
    row, col, value = map(int, command[1:])

    if action == "Add":
        if valid_coordinates(row, col, matrix):
            matrix[row][col] += value
        else:
            print(f"Invalid coordinates")

    elif action == "Subtract":
        if valid_coordinates(row, col, matrix):
            matrix[row][col] -= value
        else:
            print(f"Invalid coordinates")

    a_command = input()

for row in matrix:
    print(*row, sep = " ")
