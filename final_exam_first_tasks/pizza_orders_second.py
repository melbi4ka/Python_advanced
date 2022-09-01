import sys
from io import StringIO

input1 = '''11, 6, 8, 1
3, 1, 9, 10, 5, 9, 1
'''
input2 = """10, 9, 8, 7, 5
5, 10, 9, 8, 7
"""
input3 = """12, -3, 14, 3, 2, 0
10, 15, 4, 6, 3, 1, 22, 1
"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

from collections import deque


def orders_process(orders, bakers, total_pizza):
    while orders[0] > bakers[-1]:
        orders[0] -= bakers[-1]
        total_pizza += bakers[-1]
        bakers.pop()
        if not orders or not bakers:
            return total_pizza
    return total_pizza

orders = deque([int(x) for x in input().split(", ") if 0 < int(x) <= 10])
bakers = [int(x) for x in input().split(", ")]

total_pizza = 0

while orders and bakers:
    if orders[0] > bakers[-1]:
        total_pizza = orders_process(orders, bakers, total_pizza)
    else:
        total_pizza += orders[0]
        orders.popleft()
        bakers.pop()

if orders:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in orders])}")
else:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    print(f"Employees: {', '.join([str(x) for x in bakers])}")
