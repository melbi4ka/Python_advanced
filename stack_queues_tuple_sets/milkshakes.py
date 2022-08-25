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

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

from collections import deque

chocolate = [int(x) for x in input().split(", ")]
# print(chocolate)
milk = deque(int(x) for x in input().split(", "))
# print(milk)
milkshakes = 0
are_made = False

while True:
    current_milk = milk[0]
    if current_milk <= 0:
        milk.popleft()
    current_chocolate = chocolate[-1]
    if current_chocolate <= 0:
        chocolate.pop()

    if not milk or not chocolate:
        break

    if current_chocolate == current_milk:
        milkshakes += 1
        milk.popleft()
        chocolate.pop()
    else:
        current = milk.popleft()
        milk.append(current)
        current_chocolate -= 5

    if milkshakes == 5:
        are_made = True
        break

if are_made:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if not chocolate:
    print("Chocolate: empty")
else:
    print("Chocolate: ", end="")
    print(*chocolate, sep=", ")

if not milk:
    print("Milk: empty")
else:
    print("Milk: ", end="")
    print(*milk, sep=", ")
