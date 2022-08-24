import sys
from io import StringIO

input1 = """6 3 - 2 1 * 5 /
"""
input2 = """2 2 - 1 *
"""
input3 = """10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

from collections import deque

def numbers_operation (nums):
    return deque(nums.split())

queue = numbers_operation(input())
# print(line)
operators = "*+-/"
numbers_list = []
expression = []

while len(queue) > 0:

    current_el = queue[0]
    if current_el not in operators:
        numbers_list.append(int(queue.popleft()))
        # print(line)
    else:
        if current_el == "+":
            result = sum(numbers_list)
            queue.popleft()
            queue.appendleft(str(result))

        elif current_el == "*":
            result = 1
            for x in numbers_list:
                result = result * x
            queue.popleft()
            queue.appendleft(str(result))

        elif current_el == "-":
            result = numbers_list[0]
            for x in numbers_list[1:]:
                result -= x
            queue.popleft()
            queue.appendleft(str(result))

        elif current_el == "/":
            result = numbers_list[0]
            for x in numbers_list[1:]:
                result /= x
            result = int(result)
            queue.popleft()
            queue.appendleft(str(result))

        numbers_list.clear()
        expression.append(result)

print(expression.pop())





