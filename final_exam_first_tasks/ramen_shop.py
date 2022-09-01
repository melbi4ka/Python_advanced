import sys
from io import StringIO

input1 = """14, 25, 37, 43, 19
58, 23, 37
"""
input2 = """30, 13, 45
70, 25, 55, 15
"""
input3 = """30, 25
20, 35
"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

from collections import deque

ramen = ([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])
# print(ramen)

while ramen and customers:
    current_ramen = ramen.pop()
    current_customer = customers.popleft()

    if current_ramen == current_customer:
        continue

    elif current_ramen > current_customer:
        current_ramen -= current_customer
        ramen.append(current_ramen)

    else:
        current_customer -= current_ramen
        customers.appendleft(current_customer)

if not customers:
    print("Great job! You served all the customers.")
    if ramen:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in ramen])}")

else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
