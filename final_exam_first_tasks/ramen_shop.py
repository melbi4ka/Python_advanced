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

# рамена в стек, клиентите в дек
# попвам рамен и поплефтвам клиент
# ако стойностите на рамена и клиента са равни давам континию да чете нова команда
# ако стойността на рамена е по-голяма от стойността на клиента
# текущия рамен го намалям със стойността на клиента
# и накрая на редицата нареждат намаления рамен
# ако кърънт рамена е по-малък от стойността на клиента
# намалям стойността на текущия клиент с къстъм рамена
# и връщам клиента най-отпред в опашката с апендлефт

# печатам, ако няма клиенти - съобщение, че са обслужени всички и има рамен - колко рамен има
# иначе печатам ако има клиенти - съобщение, че е свършил рамена и имак клиенти - колко клиенти са останали



