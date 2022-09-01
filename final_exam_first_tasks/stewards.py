import sys
from io import StringIO

input1 = '''17K, 20B, 3C, 15D, 31Z, 28F
20, 35, 15, 3, 2, 10
1, 15, 64, 53, 45, 46
'''
input2 = """25A, 16B, 44T, 49D, 27M, 44F
25, 3, 31, 49, 26, 13
10, 15, 44, 40
"""
input3 = """15C, 25C, 36C, 43P, 40E, 38G
15, 25, 80, 40, 15, 99, 52
15, 42, 29
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

from collections import deque

seats = input().split(", ")
first_sequence = deque(map(int, input().split(", ")))
second_sequence = deque(map(int, input().split(", ")))

# print(seats)
# print(first_sequence)
# print(second_sequence)
matches = 0
rotation = 0
seat_matches = []
while matches < 3 and rotation < 10:
    current_first = first_sequence.popleft()
    current_second = second_sequence.pop()
    rotation += 1

    common_letter = chr(current_first + current_second)
    first_number = str(current_first) + common_letter
    second_number = str(current_second) + common_letter

    if first_number not in seats and second_number not in seats:
        first_sequence.append(current_first)
        second_sequence.appendleft(current_second)

    if first_number in seats and first_number not in seat_matches:
        seat_matches.append(first_number)
        matches += 1

    elif second_number in seats and second_number not in seat_matches:
        seat_matches.append(second_number)
        matches += 1


print(f"Seat matches: {', '.join(x for x in seat_matches)}")
print(f"Rotations count: {rotation}")











