import sys
from io import StringIO

input1 = '''5 
0K0K0
K000K
00K00
K000K
0K0K0
'''
input2 = """2
KK
KK
"""
input3 = """8
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK
"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

def get_count(matrix, row, col):
    possible_children_cords = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1 , col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1],
    ]

    hit_count = 0
    for child_row, child_col in possible_children_cords:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix):
            if matrix[child_row][child_col] == "K":
                hit_count += 1

    return hit_count

n = int(input())
matrix = []

for _ in range (n):
    line = [x for x in input()]
    matrix.append(line)

removed_knight = 0

while True:
    best_count = 0
    knight_row = 0
    knight_col = 0

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "K":
                row = r
                col = c
                count = get_count(matrix, row, col)

                if count > best_count:
                    best_count = count
                    knight_row = row
                    knight_col = col

    if best_count == 0:
        break

    matrix[knight_row][knight_col] = "0"
    removed_knight += 1

print(removed_knight)


# Прочитам си матрицата, трябва да я обходя елемент по елемент за да видя колко са конете и да видя всеки кон колко може да удари
# След като ги прочета трябва да махна този, който може да удари най-много и след това пак да извършвам същото действие
# За това while цикъл - докато е вярно
# Обхождам матрицата по ред и по колона, виждам къде има кон и вземам неговите координати
# Подавам ги на функция, която ми връща коня, който съм намерила колко коня може да удари
# Преди фор циклите - правя нулеви стойности за най-много ударени и координатите на коня, който го прави
# След като съм прочела цялата матрица с фор, вземам координатите на най-удрящия и тези координати го заменям с О в матрицата
# Броя един външен каунтър, който да ми казва колко съм махнала
# Това се повтаря докато нямам кон, който може да хитва други и бест каунтъра ми остане нула
# Тогава цикъла прекъсва

# Функцията - подавам  ред и колона за намерения кон и матрицата
# Правя един списък от списъци, като изброявам лимитирано възможните, стойности където може да кацне всеки намерен кон
# За всеки списък от списъка с възможни ходове на коня, проверявам
# - дали реда и колоната са в матрицата
# - дали ако са в матрицата са равни на К
#  - ако е така увеличавам каунтъра




