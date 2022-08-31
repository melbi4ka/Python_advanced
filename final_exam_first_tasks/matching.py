import sys
from io import StringIO

input1 = '''4 5 7 3 6 9 12
12 9 6 1
'''
input2 = """3 0 3 6 9 0 12
12 9 6 1 2 3 15 13 4
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0

while males and females:
    current_male = males.pop()
    current_female = females.popleft()

    if current_male <= 0:
        females.appendleft(current_female)
        continue

    if current_female <= 0:
        males.append(current_male)
        continue

    if current_male % 25 == 0:
        males.pop()
        females.appendleft(current_female)
        continue

    if current_female % 25 == 0:
        females.popleft()
        males.append(current_male)
        continue

    if current_male != current_female:
        current_male -= 2
        males.append(current_male)
    else:
        matches += 1

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(str(x) for x in males[::-1])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")
    
