import sys
from io import StringIO

input1 = '''3
1, 2, 3
4, 5, 6
7, 8, 9
'''

sys.stdin = StringIO(input1)


def read_matrix(m):
    matrix = []

    for _ in range(m):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


n = int(input())
matrix = read_matrix(n)
# print(matrix)
primary_diagonal_sum = 0
secondary_diagonal_sum = 0
primary_numbers = ()
secondary_numbers = ()

for i in range(n):
    primary_numbers += (str(matrix[i][i]), )
    primary_diagonal_sum += matrix[i][i]
    secondary_numbers += (str(matrix[i][n-1-i]), )
    secondary_diagonal_sum += matrix[i][n-1-i]

print(f"Primary diagonal: {', '.join(primary_numbers)}. Sum: {primary_diagonal_sum}")
print(f"Secondary diagonal: {', '.join(secondary_numbers)}. Sum: {secondary_diagonal_sum}")
