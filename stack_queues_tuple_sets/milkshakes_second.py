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
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

from collections import deque

chocolate = deque()
f_line = input().split(", ")
for el in range(len(f_line) -1, -1, -1):
    chocolate.append(int(f_line[el]))
    # print(chocolate)

milk = deque()
s_line = input().split(", ")
for el in s_line:
    milk.append(int(el))


milkshakes = 0
are_made = False

while milk and chocolate:
    current_milk = milk[0]
    current_chocolate = chocolate[0]
    if current_milk <= 0:
        milk.popleft()
    if current_chocolate <= 0:
        chocolate.popleft()
    if not milk or not chocolate:
        break

    if current_chocolate == current_milk:
        milkshakes += 1
        milk.popleft()
        chocolate.popleft()

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
    chocos = []
    while chocolate:
        chocos.append(chocolate.pop())
    print(*chocos, sep=", ")

if not milk:
    print("Milk: empty")
else:
    print("Milk: ", end="")
    print(*milk, sep=", ")

