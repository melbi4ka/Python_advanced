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

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


from collections import deque

orders = deque([int(x) for x in input().split(", ")])
bakers = [int(x) for x in input().split(", ")]

# print(orders)
# print(bakers)
total_pizza = 0

while orders and bakers:
    current_order = orders.popleft()
    current_baker = bakers.pop()

    if current_order > 10 or current_order <= 0:
        bakers.append(current_baker)
        continue


    if current_order > current_baker:
        total_pizza += current_baker
        current_order -= current_baker
        orders.appendleft(current_order)
    else:
        total_pizza += current_order


if orders:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in orders])}")
else:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    print(f"Employees: {', '.join([str(x) for x in bakers])}")
