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

line = input().split()
nums_queue = deque()

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}

for el in line:
    if el in "+*-/":
        while len(nums_queue) > 1:
            left = nums_queue.popleft()
            right = nums_queue.popleft()
            result = operations[el](left, right)
            nums_queue.appendleft(result)
    else:
        nums_queue.append(int(el))

print(nums_queue.pop())

