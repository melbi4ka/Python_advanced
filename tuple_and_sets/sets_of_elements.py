import sys
from io import StringIO

input1 = """4 3
1
3
5
7
3
4
5
"""
input2 = """2 2
1
3
1
5
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

n, m = map(int, (input().split(" ")))
n_numbers = set()
m_numbers = set()


for i in range (n + m):
    line = int(input())
    if i < n:
        n_numbers.add(line)
    else:
        m_numbers.add(line)

common = n_numbers.intersection(m_numbers)
[print(x) for x in common]
