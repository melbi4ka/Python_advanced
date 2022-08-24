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


sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)


from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
operators = deque(input().split())
operations = {
        "+": lambda a,b: abs(a+b),
        "-": lambda a,b: abs(a-b),
        "*": lambda a,b: abs(a*b),
        "/": lambda a,b: abs(a/b),
    }

total_honey = 0

while bees and nectar:
    bee_work = bees.popleft()
    nectar_val = nectar.pop()

    if nectar_val < bee_work:
        bees.appendleft(bee_work)
        continue

    if nectar_val == 0:
        continue

    current_operator = operators.popleft()
    total_honey += operations[current_operator](bee_work, nectar_val)


print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join([str(b) for b in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(b) for b in nectar])}")
