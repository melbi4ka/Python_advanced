import sys
from io import StringIO
input1 = """9
1 97
2
1 20
2
1 26
1 20
3
1 91
4
"""
input2 = """10
2
1 47
1 66
1 32
4
3
1 25
1 16
1 8
4
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

number = int(input())

stack = []

for n in range(number):
    command = [int(n) for n in input().split()]

    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2 and stack:
        stack.pop()
    elif command[0] == 3 and stack:
         print(max(stack))
    elif command[0] == 4 and stack:
        print(min(stack))

while stack:
    element = stack.pop()
    if stack:
        print(element, end = ", ")
    else:
        print(element)
