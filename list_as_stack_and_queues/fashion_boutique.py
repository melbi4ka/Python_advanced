import sys
from io import StringIO

input1 = """5 4 8 6 3 8 7 7 9
16
"""
input2 = """1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
20
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

box_of_clothes = [int (x) for x in input().split()]
capacity = int(input())
size = capacity
rack = 1

while box_of_clothes:
    element = box_of_clothes[-1]
    if element <= size:
        size -= element
        box_of_clothes.pop()
    else:
        size = capacity
        rack += 1

print(rack)
