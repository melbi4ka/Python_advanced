import sys
from io import StringIO

input1 = '''- R - - - -
- - - - - R
- E - R - -
- W - - - -
- - - C - -
M - - - - -
down, right, down, right, down, left, left, left
'''
input2 = """R - - - - -
- - C - - -
- - - - M -
- - W - - -
- E - W - R
- - - - - -
up, right, down, right, right, right
"""
input3 = """R - - - - -
- - C - - -
- - - - M -
C - M - R M
- E - W - -
- - - - - -
right, right, up, left, left, left, left, left
"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

from collections import deque


def next_step(a_row, a_col, a_command):
    if a_command == "down":
        return a_row+1, a_col
    elif a_command == "up":
        return a_row - 1, a_col
    elif a_command == "left":
        return a_row, a_col - 1
    elif a_command == "right":
        return a_row, a_col + 1


def is_outside(a_row, a_col, matrix, a_direction):
    if not 0 <= a_row < len(matrix) or not 0 <= a_col < len(matrix):
        if a_direction == "left":
            return a_row, 5
        elif a_direction == "right":
            return a_row, 0
        elif a_direction == "up":
            return 5, a_col
        elif a_direction == "down":
            return 0, a_col
    else:
        return a_row, a_col


mars = []
explorer_row = 0
explore_col = 0

for r in range(6):
    line = input().split()
    mars.append(line)
    for c in range(len(line)):
        if line[c] == "E":
            explorer_row = r
            explore_col = c

# print(mars)
# print(explorer_row, explore_col)
queue = deque(input().split(", "))
# print(queue)
water = 0
concreate = 0
metal = 0

while queue:
    command = queue.popleft()

    explorer_row, explore_col = next_step(explorer_row, explore_col, command)
    explorer_row, explore_col = is_outside(explorer_row, explore_col, mars, command)


    if mars[explorer_row][explore_col] == "W":
        water += 1
        print(f"Water deposit found at ({explorer_row}, {explore_col})")
    elif mars[explorer_row][explore_col] == "C":
        concreate += 1
        print(f"Concrete deposit found at ({explorer_row}, {explore_col})")
    elif mars[explorer_row][explore_col] == "M":
        metal += 1
        print(f"Metal deposit found at ({explorer_row}, {explore_col})")
    elif mars[explorer_row][explore_col] == "R":
        print(f"Rover got broken at ({explorer_row}, {explore_col})")
        break

if water >= 1 and concreate >= 1 and  metal >= 1:
    print("Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")


# чета матрица и събирам координати на експлоръра
# след това командите идват със запетайка и ги правя на дек
#  въртя уайл цикъл докато имам команди
# изчислявам следващата стъпка във функция от която получавам резултатите
# изчислявам още една функция ако съм извън матрицата
# проверявам дали матрицата на новия ред и колона е W, C, M
# ако е едно о тях ги събирам в отделни променливи и печатам съответните координати
# ако матрицата на реда и колоната е R - принтирам, че съм счупена и брейкавм
# печатам че е успешно ако имам повече от една вода, метал или конкрийт
# иначе печатам неуспешно

# функция за новия ред и колона - подавам първоначалните ред, колона и накъде се движа  на функцията
# и тя ми връща кои са ми следващите стъпки, които приравнявам на изчислените от функцията ред и колона

# в другата функция подавам вече новите ред и колона и ако те са извън матрицата,
# връща нови координати - на обратната страна
# ако не мине през иф проверката ще ми същите колона и матрица, които съм подала
#  при всички случаи ще ми върне координати, които са в матрицата





