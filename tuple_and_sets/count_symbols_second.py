import sys
from io import StringIO

input1 = """SoftUni rocks
"""
input2 = """Why do you like Python?
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

line = input()
counts = {}

for el in line:
    if el not in counts:
        counts[el] = 0
    counts[el] += 1

for key, value in sorted(counts.items()):
    print(f"{key}: {value} time/s")
