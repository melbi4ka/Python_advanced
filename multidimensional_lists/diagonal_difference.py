import sys
from io import StringIO

input1 = '''3
11 2 4
4 5 6
10 8 -12
'''
input2 = """4
-7 14 9 -20
3 4 9 21
-14 6 8 44
30 9 7 -14
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

def read_matrix(m):
    matrix = []

    for _ in range(m):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


n = int(input())
matrix = read_matrix(n)
# print(matrix)
primary_diagonal_sum = 0
secondary_diagonal_sum = 0


for i in range(n):
    primary_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][n-1-i]

difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

print(difference)

