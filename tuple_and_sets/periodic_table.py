import sys
from io import StringIO

input1 = """4
Ce O
Mo O Ce
Ee
Mo
"""
input2 = """3
Ge Ch O Ne
Nb Mo Tc
O Ne
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

n = int(input())
periodic = set()

for _ in range (n):
    line = input().split()
    for el in line:
        periodic.add(el)

[print(x) for x in periodic]
