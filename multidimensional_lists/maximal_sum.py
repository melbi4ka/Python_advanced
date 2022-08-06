import sys
from io import StringIO

input1 = '''4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4
'''
input2 = """5 6
1 0 4 3 1 1
1 3 1 3 0 4
6 4 1 2 5 6
2 2 1 5 4 1
3 3 3 6 0 5
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)


def read_matrix(a):
    a_matrix = []

    for _ in range(a):
        rows=[int(x) for x in input().split()]
        a_matrix.append(rows)
    return a_matrix


row, col = [int(x) for x in input().split()]
matrix = read_matrix(row)
# print(matrix)
result = -sys.maxsize
maxsum_matrix = []

for r in range(row-2):
    for c in range(col-2):
        submatrix = [matrix[r][c],  matrix[r][c+1],  matrix[r][c+2],  \
                     matrix[r+1][c],   matrix[r+1][c+1],  matrix[r+1][c+2],  \
                     matrix[r+2][c],  matrix[r+2][c+1],   matrix[r+2][c+2]]
        square_sum = sum(submatrix)

        if square_sum > result:
            result = square_sum
            maxsum_matrix = submatrix.copy()

# print(maxsum_matrix)

print(f"Sum = {result}")
print(f"{' '.join(str(x) for x in maxsum_matrix[0:3])}")
print(f"{' '.join(str(x) for x in maxsum_matrix[3:6])}")
print(f"{' '.join(str(x) for x in maxsum_matrix[6:])}")
