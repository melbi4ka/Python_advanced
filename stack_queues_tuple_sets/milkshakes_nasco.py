import sys
from io import StringIO


input1 = """20, 24, -5, 17, 22, 60, 26
26, 60, 22, 17, 24, 10, 55
"""
input2 = """-10, -2, -30, 10
-5
"""
input3 = """2, 3, 3, 7, 2
2, 7, 3, 3, 2, 14, 6
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

from collections import deque

chocolate = [int(x) for x in input().split(", ")]
milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while chocolate and milk and milkshakes < 5:
    chocolate_ingradient = chocolate.pop()
    milk_ingradient = milk.popleft()

    if chocolate_ingradient <= 0 and milk_ingradient <= 0:
        continue

    if chocolate_ingradient <= 0:
        milk.appendleft(milk_ingradient)
        continue

    if milk_ingradient <= 0:
        chocolate.append(chocolate_ingradient)
        continue


    if chocolate_ingradient == milk_ingradient:
        milkshakes += 1
    else:
        milk.append(milk_ingradient)
        chocolate.append(chocolate_ingradient - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if not chocolate:
    print("Chocolate: empty")
else:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
    # print(*chocolate, sep=", ")

if not milk:
    print("Milk: empty")
else:
    print(f"Milk: {', '.join([str(x) for x in milk])}")
    # print(*milk, sep=", ")
