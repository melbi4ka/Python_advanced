import sys
from io import StringIO

input1 = '''3, 3, 10, 3, 2 
0
'''
input2 = """4, 10, 10, 6, 2, 99
2
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

from collections import deque

jobs = deque([int(x) for x in input().split(", ")])
index = int(input())

our_job = jobs[index]
clock_cycles = 0
counter = -1

while jobs:
    current_job = jobs.popleft()
    counter += 1

    if current_job < our_job:
        clock_cycles += current_job
    elif current_job == our_job:
        if counter <= index:
            clock_cycles += current_job
        else:
            continue
    elif current_job > our_job:
        continue

print(clock_cycles)

# 100/100 - от раз и не мога да повярвам
# определям си нашата  задача с индекса
# сетвам си една променлива да събирам циклите
# сетвам си един каунтър на -1
# уайл цикъл - докато имам задачи
# увеличавам каунтъра - идеята ми е той да върви с индексите
# текущата задача я поплефтвам
# ако е по-малка  на нашата задача, събирам стойността и в циклите
# ако е равна на нашата задача, проверявам дали каунтъра е по-малък от нашия индекс
# ако е така събирам към циклите
# ако не - продължавам
# ако текущата задача е по-голяма от нашата работа континию, чета следващата задача
# докато не останат задачи

# целта ми е да събера всички задачи, които са по-малки или равни на моята
# за тези които са с еднаква стойност, събирам само ако индекса им е по-малък от моя










