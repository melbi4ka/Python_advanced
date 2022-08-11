import sys
from io import StringIO

input1 = '''5
4
- X V -
- S - V
- - - -
X - - -
up
right
down
right
Christmas morning
'''
input2 = """3
4
- - - -
V - X -
- V C V
- - - S
left
up
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

def next_position (command, row, col):
    if command == "right":
        return row, col+1
    elif command == "left":
        return row, col-1
    elif command == "up":
        return row-1, col
    elif command == "down":
        return row+1, col

def is_inside (row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col <= len(matrix)

def get_neighbours (matrix, row, col):
    result = []
    if is_inside(row, col -1, matrix) and matrix[row][col - 1] == "V" or matrix[row][col - 1] == "X":
        result.append([row, col -1])
    if is_inside(row, col + 1, matrix) and matrix[row][col + 1] == "V" or matrix[row][col + 1] == "X":
        result.append([row, col+1])
    if is_inside(row -1, col, matrix) and matrix[row - 1][col] == "V" or matrix[row - 1][col] == "X":
        result.append([row - 1, col])
    if is_inside(row + 1, col, matrix) and matrix[row + 1][col] == "V" or matrix[row + 1][col] == "X":
        result.append([row + 1, col])
    return result

presents = int(input())
n = int(input())
matrix = []
good_guys = 0
santa_row = 0
santa_col = 0
gifted_good_guys = 0

for i in range(n):
    line = input().split()
    matrix.append(line)
    for j in range(n):
        if line[j] == "S":
            santa_row = i
            santa_col = j
        elif line[j] == "V":
            good_guys += 1


command = input()
while True:
    if command == "Christmas morning":
        break
    direction = command

    matrix[santa_row][santa_col] = "-"
    santa_row,  santa_col = next_position(direction, santa_row, santa_col)

    if matrix[santa_row][santa_col] == "V":
        presents -= 1
        gifted_good_guys += 1
        matrix[santa_row][santa_col] = "S"

    elif matrix[santa_row][santa_col] == "C":
        matrix[santa_row][santa_col] = "S"
        neighbour_kids = get_neighbours(matrix, santa_row, santa_col)
        for n_row, n_col in neighbour_kids:
            if matrix[n_row][n_col] == "V":
                gifted_good_guys += 1
                if presents == 0:
                    break

            presents -= 1
            matrix[n_row][n_col] = "-"

    if presents == 0:
        break

    command = input()



# print(good_guys)
# print(gifted_good_guys)
if not presents and good_guys != gifted_good_guys:
    print(f"Santa ran out of presents!")

for j in range(n):
    print(*matrix[j])

if good_guys == gifted_good_guys:
    print(f"Good job, Santa! {gifted_good_guys} happy nice kid/s.")
else:
    print(f"No presents for {good_guys-gifted_good_guys} nice kid/s.")



# 100/100 -  с много мъка
# Четем матрицата и докато я четем, събираме данни за координатите на санта и колко добри деца има
# Уайл тру - брейква ако подаръците станат = 0 или ако получим Кристмъс морнинг
# Извън това - сменям санта роу и санта кол на "-"
# Получавам следващите координати на санта чрез функция
#  Ако следващите координати на Санта са Х нищо не правя, ако са V - намалям подаръците с 1, увеличавам децата получили подарък с 1,
#  правя клетката да отговаря на S
# Ако клетката е С
#  трябва да обходя клетките отляво, отдясно, отгоре, отстрани - с функция, която ми връща координатите на които има лошо или добро дете
#  с фор цикъл обхождам координатите и гледам дали е V - ако да - увеличавам надарените деца с 1, намалям подаръците (за всички)
#  и с вътрешна проверка следа дали, подаръците не ста стигнали до 0. Ако са стигнали брейквам и накрая променям колоната на "-"

# Проверката за печата - ако нямам подаръци и надарените деца са различни от добрите - печатам, че подаръците са му свършили
# Печатам матрицата
# Ако добрите деца са равни на надарените - печатам, че дядо коледа си е свършил работата
# Иначе - Печатам колко деца са останали ненадарени

#  Функцията за следваща клетка на дядо Коледа - подавам команда, ред и колона и в зависимост от колоната да ми сметне следващата стъпка

# Функцията за координатите на бисвитените деца - подавам ред, колона, матрица - функцията вика друга функция, която да провери дали клетките
#  нгоре, надолу, наляво и надясно са в матрицата и дали е V или X - ако е така в един общ резултат апендвам ред и колона

