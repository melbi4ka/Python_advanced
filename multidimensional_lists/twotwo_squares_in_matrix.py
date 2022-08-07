import sys
from io import StringIO

input1 = '''3 4
A B B D
E B B B
I J B B
'''
input2 = """2 2
a b
c d
"""
input3 = """5 4
A A B D
A A B B
I J B B
C C C G
C C K P
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

def read_matrix(a):
    matrix = []

    for _ in range(a):
        row = input().split()
        matrix.append(row)
    return matrix


row, col = [int(x) for x in input().split()]
matrix = read_matrix(row)
# print(matrix)
result = 0

for r in range(row-1):
    for c in range(col-1):
        if matrix[r][c] == matrix[r][c+1] == matrix[r+1][c] == matrix[r+1][c+1]:
            result += 1

print(result)
