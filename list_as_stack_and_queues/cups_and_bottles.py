import sys
from io import StringIO

input1 = """4 2 10 5
3 15 15 11 6
"""
input2 = """1 5 28 1 4
3 18 1 9 30 4 5
"""

input3 = """10 20 30 40 50
20 11
"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

from collections import deque


def cups_capacity(line):
    cups_as_queue = deque([int(x) for x in line.split()])
    return cups_as_queue

def bottle_capacity(line):
    bottles_as_stack = [int(x) for x in line.split()]
    return bottles_as_stack


cups = cups_capacity(input())
bottles = bottle_capacity(input())
wasted = 0
is_fill = False

# print(cups)
# print(bottles)

while bottles:
    current_bottle = bottles.pop()
    # current_cup = cups[0]

    if current_bottle >= cups[0]:
        wasted += current_bottle - cups[0]
        cups.popleft()

    else:
        diff = abs(current_bottle - cups[0])
        # bottles.pop()
        cups[0] = diff

    if not cups:
        is_fill = True
        break

if is_fill:
    bottles_str = ""
    for n in bottles:
        bottles_str += str(n) + " "
    print(f"Bottles: {bottles_str}")
else:
    cups_str = ""
    for m in cups:
        cups_str += str(m) + " "
    print(f"Cups: {cups_str}")

print(f"Wasted litters of water: {wasted}")


