import sys
from io import StringIO

input1 = """SoftUni rocks
"""
input2 = """Why do you like Python?
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

line = [x for x in input()]
# print(line)
counts = {}

for el in line:
    if el not in counts:
        counts[el] = 0
    counts[el] += 1

# print(counts)
sorted_counts = dict(sorted(counts.items()))
for key, value in sorted_counts.items():
    print(f"{key}: {value} time/s")
# print(sorted_counts)




