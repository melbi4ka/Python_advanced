import sys
from io import StringIO


input1 = """d yel blu e low redd
"""
input2 = """r ue nge ora bl ed
"""
input3 = """re ple blu pop e pur d
"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

from collections import deque

queue = deque(input().split())
prime_colors = {"red", "blue", "yellow"}
secondary_colors = {"orange", "purple", "green" }
new_colors = []


while queue:
    first_substring = queue.popleft()
    second_substring = queue.pop() if queue else ""

    result = first_substring + second_substring

    if result in prime_colors or result in secondary_colors:
        new_colors.append(result)
        continue

    result = second_substring + first_substring
    if result in prime_colors or result in secondary_colors:
        new_colors.append(result)
        continue

    first_substring = first_substring[:-1]
    second_substring = second_substring[:-1]

    if first_substring:
        queue.insert(len(queue) // 2, first_substring)
    if second_substring:
        queue.insert(len(queue)//2, second_substring)

result = []
secondary_dict = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

for color in new_colors:
    if color in prime_colors:
        result.append(color)
        continue

    is_collected = True
    for one_color in secondary_dict[color]:
        if one_color not in new_colors:
            is_collected = False
            break

    if is_collected:
        result.append(color)

print(result)








