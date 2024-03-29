import sys
from io import StringIO

input1 = '''- - - - - - b -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -
'''
input2 = """- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
b - - - - - - -
- w - - - - - -
- - - - - - - -
"""
input3 = """- - - - - - b -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - w
- - - - - - - -
"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

def get_white_step (row, col):
    return row-1, col

def get_black_step (row, col):
    return row+1, col

def get_opposite_white(row, col):
    return (row-1, col-1), (row-1, col+1)

def is_inside(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)

def get_opposite_black(row, col):
    return (row+1, col-1), (row+1, col+1)

def get_chessboard_row (row):
    if row == 7:
        return "1"
    elif row == 6:
        return "2"
    elif row == 5:
        return "3"
    elif row == 4:
        return "4"
    elif row == 3:
        return "5"
    elif row == 2:
        return "6"
    elif row == 1:
        return "7"
    elif row == 0:
        return "8"

def get_chessboard_col (col):
    return chr(col+97)

n = 8
matrix = []
white_row = 0
white_col = 0
black_row = 0
black_col = 0

for r in range(n):
    line = input().split()
    matrix.append(line)
    for c in range(len(line)):
        if line[c] == "w":
            white_row = r
            white_col = c
        elif line[c] == "b":
            black_row = r
            black_col = c

print(matrix)
print(white_row, white_col)
print(black_row, black_col)

for i in range (n):

    white_opposite_left, white_opposite_right = get_opposite_white(white_row, white_col)
    white_right_row, white_right_col = white_opposite_right
    white_left_row, white_left_col = white_opposite_left

    if is_inside(white_right_row, white_right_col, matrix) \
            and matrix[white_right_row][white_right_col] == "b":
        print(f"Game over! White win, "
              f"capture on {get_chessboard_col(white_right_col)}{get_chessboard_row(white_right_row)}.")
        break
    elif is_inside(white_left_row, white_left_col, matrix) \
            and matrix[white_left_row][white_left_col] == "b":
        print(f"Game over! White win, "
              f"capture on {get_chessboard_col(white_left_col)}{get_chessboard_row(white_left_row)}.")
        break
    else:
        white_row, white_col = get_white_step(white_row, white_col)
        # white_row, white_col = next_white_row, next_white_col
        matrix[white_row][white_col] = "w"
        if white_row == 0:
            print(f"Game over! White pawn "
                f"is promoted to a queen at {get_chessboard_col(white_col)}"
                f"{get_chessboard_row(white_row)}.")
            break

    black_opposite_left, black_opposite_right = get_opposite_black(black_row, black_col)
    black_right_row, black_right_col = black_opposite_right
    black_left_row, black_left_col = black_opposite_left
    if is_inside(black_right_row, black_right_col, matrix) and matrix[black_right_row][black_right_col] == "w":
        print(f"Game over! Black win, "
              f"capture on {get_chessboard_col(black_right_col)}{get_chessboard_row(black_right_row)}.")
        break
    elif is_inside(black_left_row, black_left_col, matrix) and matrix[black_left_row][black_left_col] == "w":
        print(f"Game over! Black win, "
              f"capture on {get_chessboard_col(black_left_col)}{get_chessboard_row(black_left_row)}.")
        break
    else:
        black_row, black_col = get_black_step(black_row, black_col)
        # black_row, black_col = next_black_row, next_black_col
        matrix[black_row][black_col] = "b"
        if black_row == 7:
            print(f"Game over! Black pawn "
                f"is promoted to a queen at {get_chessboard_col(black_col)}{get_chessboard_row(black_row)}.")
            break
