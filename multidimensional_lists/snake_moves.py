import sys
from io import StringIO

input1 = '''5 6
SoftUni
'''
input2 = """1 4
Python
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)


# def read_matrix(a):
#     a_matrix = []
#
#     for _ in range(a):
#         rows = input().split()
#         a_matrix.append(rows)
#     return a_matrix

from collections import deque

row, col = [int(x) for x in input().split()]
matrix = []
que = deque(input())
# print(que)


for r in range(row):
    c = ["a"]
    matrix.append(c * col)


for r in range(row):
    for c in range(col):
        current = que.popleft()
        if r % 2 == 0:
            matrix[r][c] = current
            que.append(current)
        elif r % 2 == 1:
            matrix[r][col-c-1] = current
            que.append(current)

    print(''.join(matrix[r]))





# print(matrix)
# line = input()
