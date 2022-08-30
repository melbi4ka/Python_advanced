import sys
from io import StringIO

input1 = """6
George
George
George
Peter
George
NiceGuy1234
"""
input2 = """10
Peter
Maria
Peter
George
Steve
Maria
Alex
Peter
Steve
George
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

n = int(input())
usernames = set()

for _ in range (n):
    name = input()
    usernames.add(name)

[print(name) for name in usernames]
