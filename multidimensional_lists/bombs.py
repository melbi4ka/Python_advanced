import sys
from io import StringIO

input1 = '''4
8 3 2 5
6 4 7 9
9 9 3 6
6 8 1 2
1,2 2,1 2,0
'''
input2 = """3
7 8 4
3 1 5
6 4 9
0,2 1,0 2,2
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

from collections import deque

def read_matrix(a):
    a_matrix = []

    for _ in range(a):
        rows = [int(x) for x in input().split()]
        a_matrix.append(rows)
    return a_matrix

def get_neighbour (a_matrix, row, col):
    possible_neighbours = [
        [row-1, col-1],
        [row-1,  col],
        [row-1, col+1],
        [row, col-1],
        [row, col+1],
        [row+1, col-1],
        [row+1, col],
        [row+1, col+1]
    ]
    result = []
    for neighbour_row, neighbour_col in possible_neighbours:
        if 0 <= neighbour_row < len(matrix) and 0 <= neighbour_col < len(matrix) and matrix[neighbour_row][neighbour_col] > 0:
            result.append([neighbour_row, neighbour_col])
    return result


n = int(input())
matrix = read_matrix(n)
# print(matrix)
queue = deque()
line = input().split()

for el in line:
    coord_one, coord_two  = el.split(",")
    queue.append(int(coord_one))
    queue.append(int(coord_two))
# print(queue)

while queue:
    row_index = queue.popleft()
    col_index = queue.popleft()

    power = matrix[row_index][col_index]

    if power < 0:
        continue

    matrix[row_index][col_index] = 0

    neighbour = get_neighbour(matrix, row_index, col_index)
    for neighbour_r, neighbour_c in neighbour:
        matrix[neighbour_r][neighbour_c] -= power

alive_count = 0
alive_sum = 0
for row in matrix:
    for el in row:
        if el > 0:
            alive_count += 1
            alive_sum += el
print(f"Alive cells: {alive_count}")
print(f"Sum: {alive_sum}")

for row in matrix:
    print(*row, sep = " ")
