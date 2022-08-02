import sys
from io import StringIO
input1 = """3
1 5
10 3
3 4
"""
input2 = """5
22 5
14 10
52 7
21 12
36 9
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

from collections import deque

n = int(input())
stations = deque()

for _ in range (n):
    one_station = [int(x) for x in input().split()]
    stations.append(one_station)

# print(stations)
index = 0

for attempt in range(len(stations)):
    tank = 0
    is_failed = False
    for fuel, distance in stations:
        tank += fuel

        if distance > tank:
            is_failed = True
            break
        else:
            tank -= distance

    if is_failed:
        stations.append(stations.popleft())
    else:
        print(attempt)
        break
