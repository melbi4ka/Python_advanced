import sys
from io import StringIO

input1 = '''5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0
'''
input2 = """8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

def direction(submatrix):
    if "X" in submatrix:
        trap_idx = submatrix.index("X")
        submatrix_sum = sum([int(x) for x in submatrix[0:trap_idx]])

        # submatrix_sum = sum(submatrix[0:trap_idx])
    else:
        submatrix_sum = sum([int(x) for x in submatrix])

    return submatrix_sum


n = int(input())
matrix = []

for _ in range(n):
    el = list(input().split())
    matrix.append(el)

print(matrix)
best_directions ={
    "left": 0,
    "right": 0,
    "above": 0,
    "under": 0,
}


for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] == "B":
            row = r
            col = c

            right_submatrix = matrix[row][col+1:]
            sum_right = direction(right_submatrix)
            best_directions["right"] += sum_right


            left_submatrix = matrix[row][:col]
            sum_left = direction(left_submatrix)
            best_directions["left"] += sum_left

            above_submatrix = []
            above_coordinates = []
            cur_row = row - 1
            while cur_row > -1:
                above_submatrix.append(matrix[cur_row][col])
                above_coordinates.append(cur_row)
                above_coordinates.append(col)
                cur_row -= 1
            above_sum = direction(above_submatrix)
            best_directions["above"] += above_sum
            print(above_coordinates)

            under_submatrix = []
            cur_row = row + 1
            while cur_row < len(matrix):
                under_submatrix.append(matrix[cur_row][col])
                cur_row += 1
            under_sum = direction(under_submatrix)
            best_directions["under"] += under_sum

            print(sum_left, sum_right, above_sum, under_sum)

            sorted_directions = sorted(best_directions.items(), key=lambda kv: -kv[1])
            if sorted_directions[0][0] == "right":
                print("right")
                for el in right_submatrix:
                    if str(el) in matrix:
                        


