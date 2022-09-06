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
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


def is_inside(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def get_step (row, col, color):
    if color == "white":
        return row-1, col
    else:
        return row+1, col


def get_opposite(row, col, color):
    if color == "white":
        return (row-1, col-1), (row-1, col+1)
    else:
        return (row + 1, col - 1), (row + 1, col + 1)


def get_chessboard_row_col (row, col):
    row_names = [8, 7, 6, 5, 4, 3, 2, 1]
    columns_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return row_names[row], columns_names[col]


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

# print(len(matrix))
# print(white_row, white_col)
# print(black_row, black_col)
winner = None
winner_row = None
winner_col = None
turn = -1

while not winner:
    if abs(white_col - black_col) != 1:
        if abs(0 - white_row) <= abs(len(matrix)- 1 - black_row):
            winner = "White"
            white_row = 0
            winner_row, winner_col = white_row, white_col
        else:
            winner = "Black"
            black_row = len(matrix)-1
            winner_row, winner_col = black_row, black_col
        print(f"Game over! {winner} pawn is promoted to a queen "
            f"at {get_chessboard_row_col(winner_row, winner_col)[1]}"
            f"{get_chessboard_row_col(winner_row, winner_col)[0]}.")
        break

    else:
        turn += 1
        if turn % 2 == 0:
            opposite = get_opposite(white_row, white_col, "white")
            for c_row, c_col in opposite:
                if is_inside(c_row, c_col, matrix) and matrix[c_row][c_col] == "b":
                    winner = "White"
                    winner_row, winner_col = black_row, black_col
                    break
            else:
                white_row, white_col = get_step(white_row, white_col, "white")
                matrix[white_row][white_col] = "w"

        elif turn % 2 != 0:
            opposite = get_opposite(black_row, black_col, "black")
            for c_row, c_col in opposite:
                if is_inside(c_row, c_col, matrix) and matrix[c_row][c_col] == "w":
                    winner = "Black"
                    winner_row, winner_col = white_row, white_col
                    break
            else:
                black_row, black_col = get_step(black_row, black_col, "black")
                matrix[black_row][black_col] = "b"

        if winner:
            print(f"Game over! {winner} win, capture on "
                f"{get_chessboard_row_col(winner_row, winner_col)[1]}"
                f"{get_chessboard_row_col(winner_row, winner_col)[0]}.")
            break
