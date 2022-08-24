
import sys
from io import StringIO

input1 = """20 62 99 35 0 150
120 60 10 1 70 10
+ - + + / * - - /
"""
input2 = """30
15 9 5 150 8
* + + * -
"""


# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)


from collections import deque

def nectar_stack(line):
    nectar_as_stack = [int(x) for x in line.split()]
    return nectar_as_stack


def bees_queue(line):
    bees_as_queue = deque([int(x) for x in line.split()])
    return bees_as_queue

def operation_dict ():
    op_dict = {
        "+": lambda a,b: abs(a+b),
        "-": lambda a,b: abs(a-b),
        "*": lambda a,b: abs(a*b),
        "/": lambda a,b: abs(a/b),
    }
    return op_dict

def symbols_queue(line):
    symbols_as_queue = deque(line.split())
    return symbols_as_queue


bees = bees_queue(input())
nectar = nectar_stack(input())
symbols = symbols_queue(input())
operators = operation_dict()
# print(operators)

total_honey = 0

while bees and nectar:
    bee_work = bees.popleft()
    nectar_val = nectar.pop()

    if nectar_val < bee_work:
        bees.appendleft(bee_work)
        continue

    if nectar_val == 0:
        continue

    current_operator = symbols.popleft()
    total_honey += operators[current_operator](bee_work, nectar_val)


print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join([str(b) for b in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(b) for b in nectar])}")
