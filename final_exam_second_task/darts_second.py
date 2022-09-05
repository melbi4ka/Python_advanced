import sys
from io import StringIO

input1 = '''Ivan, Peter
12 21 18 4 20 7 11
9 D D D D D 10
15 D T T T D 3
2 D T B T D 19
17 D T T T D 6
22 D D D D D 14
5 8 23 13 16 1 24
(3, 3)
'''
input2 = """George, Hristo
17 8 21 6 13 3 24
16 D D D D D 14
7 D T T T D 15
23 D T B T D 2
9 D T T T D 22
19 D D D D D 10
12 18 4 20 5 11 1
(1, 0)
(2, 3)
(0, 0)
(4, 2)
(5, 1)
(3, 1)
(0, 0)
(2, 3)
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

import re

def is_inside(row, col, matrix):
    return 0 <= row < len(matrix) and 0<= col < len(matrix)


def player_game(row, col, matrix):
    points = int(matrix[row][0]) + int(matrix[row][6]) + \
             int(matrix[0][col]) + int(matrix[6][col])
    if matrix[row][col] == "B":
        result = "win"
    elif matrix[row][col] == "D":
        result = points * 2
    elif matrix[row][col] == "T":
        result = points * 3
    else:
        result = int(matrix[row][col])
    return result


first_player, second_player = input().split(", ")
n = 7
matrix = [input().split() for _ in range(n)]

# for r in range(n):
#     line = input().split()
#     matrix.append(line)

# print(matrix)
first_player_won = False
second_player_won = False
turn = 1
first_start_score = 501
second_start_score = 501


while first_start_score > 0 and second_start_score > 0:
    coordinates = input()
    row, col = tuple(map(int, re.findall(r'[0-9]+', coordinates)))
    turn += 1

    if not is_inside(row, col, matrix):
        continue

    points = player_game(row, col, matrix)
    if points == "win":
        if turn % 2 == 0:
            first_player_won = True
        else:
            second_player_won = True
        break
    else:
        if turn % 2 == 0:
            first_start_score -= points
        else:
            second_start_score -= points

if first_player_won or first_start_score <= 0:
    print(f"{first_player} won the game with {turn//2} throws!")

elif second_player_won or second_start_score <= 0:
    print(f"{second_player} won the game with {turn//2} throws!")

# чета матрицата Б.О.
# дори с комприхеншън
# сетвам си две променливи на фолс - първия печели, втория печели
# сетвам си две променливи с първоначални точки - 501 - на първия, на втория
# един търн, който е равен на 1

# уайл цикъл - докато нито първия е спечил и нито втория е спечелил
# чета координати от инпута
# изкарвам ги с регекс
# търна го увеличавам с 1
# ако координатите не са вътре - континию
# Инес го реши с try - except
# получавам точки от функцията
#  ако точките са уин  и е ред на първия - той печели, ако не - обратно и брейква
# ако точките са число - чийто ред е ги вадя от първоначалните му точки
# накрая печатам според резултата

#  функция - подавам реда, колоната и матрицата
# ако матрицата на този ред и колана е равна на В - връщам като резултат уин
# ако координатите в матрицата са равни на Д - умножавам по 2 точките, които
# са ми сбор от четирите странични точки
# ако координатите в матрицата са равни на Т - умножавам по 3 точките, които
# # са ми сбор от четирите странични точки
# ако е цифра - връщам парснат към инт резултат
# накрая връщам резултата - уин/двойни точки/тройни точки/обикновени точки
#



