import sys
from io import StringIO
input1 = """1 2 3 4 5"""
input2 = """1"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

line = input().split()
# print(line)

res = []
for num in range(len(line)):
    res.append(line.pop())

print(*res)