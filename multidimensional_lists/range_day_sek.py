import sys
from io import StringIO

input1 = '''. . . . . 
x . . . . 
. A . . . 
. . . x . 
. x . . x 
3
shoot down
move right 4
move left 1
'''
input2 = """. . . . . 
. . . . . 
. A x . . 
. . . . . 
. x . . . 
2
shoot down
shoot right
"""

input3 = """. . . . . 
. . . . . 
. . x . . 
. . . . . 
. x . . A 
3
shoot down
move right 2
shoot left
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


def move_position (row, col, value, a_command):
    if a_command == "right":
        return row, col + value
    elif a_command == "left":
        return row, col - value
    elif a_command == "up":
        return row - value, col
    elif a_command == "down":
        return row + value, col

# def is_inside (row, col, a_matrix):
#     return 0 <= row < len(a_matrix) and 0 <= col < len(a_matrix)


matrix = []
range_row = 0
range_col = 0
all_targets = 0

for i in range (5):
    line = input().split()
    matrix.append(line)
    for j in range(5):
        if line[j] == "A":
            range_row = i
            range_col = j
        elif line[j] == "x":
            all_targets += 1

n = int(input())
all_coordinates = []

for _ in range (n):
    command = input().split()
    action, direction = command[:2]

    if action == "move":
        steps = int(command[2])
        next_row, next_col = move_position(range_row, range_col, steps, direction)

        if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix) and matrix[next_row][next_col] == ".":
            range_row, range_col = next_row, next_col

    elif action == "shoot":
        shooting_row, shooting_col = move_position(range_row, range_col, 1, direction)
        while 0 <= shooting_row < len(matrix) and 0 <= shooting_col < len(matrix):
            if matrix[shooting_row][shooting_col] == "x":
                matrix[shooting_row][shooting_col] = "."
                all_coordinates.append([shooting_row, shooting_col])
                all_targets -= 1
                break
            shooting_row,shooting_col = move_position(shooting_row,shooting_col, 1, direction)

        if all_targets == 0:
            break


# left_targets = all_targets - len(all_coordinates)


if all_targets:
    print(f"Training not completed! {all_targets} targets left.")
else:
    print(f"Training completed! All {len(all_coordinates)} targets hit.")

for el in all_coordinates:
    print(el)

# 100/100 - бахти и задачата
# Подавам ред и чета матрицата, докато я чета изкарвам текущите координати и броя на мишените
# Правя фор цикъл - имам две основни команди - мув и шут
# Ако е мув, правя функция, с която чета следващите стъпки
# Ако следващата стъпка е в матрицата и е равна на точка сменям координатите

# Функция шут - с горната функция, но със стъпка едно прочитам следващите координати
# Правя уайл цикъл, който казва докато съм в матрицата
#  - ако е клетката е равна на "х", правя я на точка, апендвам си в един лист координатите, намялям броя на мишените и брейквам
# - ако не е ще ми прочете следващи координати с функцията
# - после проверявам дали мишените не са станали нула, за да брейкна

# функкцията за движение - подавам ред, колона, стъпка и движение и връщам, спрямо посоките следващи координати
#  функцията за инсайд - връщам дали реда и колоната са между нула и матрицата