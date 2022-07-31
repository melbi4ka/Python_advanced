import sys
from io import StringIO

input1 = """348
20 54 30 16 7 9
"""
input2 = """499
57 45 62 70 33 90 88 76 100 50
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)


from collections import deque

quantity_of_food = int(input())

queue = deque([int(x) for x in input().split()])

max_order = max(queue)
print(max_order)
# print(queue)


while queue:
    element = queue[0]
    if element <= quantity_of_food:
        quantity_of_food -= element
        queue.popleft()
    else:
        break

if queue:
    queue = [str(x) for x in queue]
    print(f"Orders left: {' '.join(queue)}")
else:
    print("Orders complete")










