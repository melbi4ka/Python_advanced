import sys
from io import StringIO

input1 = '''1 2 3 |4 5 6 |  7  88
'''
input2 = """7 | 4  5|1 0| 2 5 |3
"""
input3 = """1| 4 5 6 7  |  8 9
"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

line = input().split("|")

result = []
for el in range (len(line)-1, -1, -1):
    subresult = line[el].strip().split()
    result.extend(subresult)

print(*result, end = " ")
# print(matrix)