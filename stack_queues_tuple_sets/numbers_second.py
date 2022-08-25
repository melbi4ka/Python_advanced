import sys
from io import StringIO

input1 = """1 2 3 4 5
1 2 3
3
Add First 5 6
Remove Second 8 9 11
Check Subset
"""
input2 = """5 4 2 9 9 5 4
1 1 1 5 6 5
4
Add First 5 6 9 3
Add Second 1 2 3 3 3
Check Subset
Remove Second 1 2 3 4 5
"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

def unique_numbers(nums):
    return set([int(x) for x in nums])


first_line = unique_numbers(input().split())
second_line = unique_numbers(input().split())

number = int(input())

for _ in range(number):
    parts = input().split()
    # print(parts)
    command = parts[0]
    target_set = parts[1]

    if command == "Add":
        if target_set == "First":
            first_line = first_line.union([int(x) for x in parts[2:]])

        elif target_set == "Second":
            second_line = second_line.union([int(x) for x in parts[2:]])

    elif command == "Remove":
        if target_set == "First":
            first_line = first_line.difference([int(x) for x in parts[2:]])

        elif target_set == "Second":
            # second_line = second_line.difference([int(x) for x in parts[2:]])
            m = set([int(x) for x in parts[2:]])
            second_line = second_line.difference(m)
            # print(m)

    elif command == "Check":
        if first_line.issubset(second_line) or second_line.issubset(first_line):
            print("True")
        else:
            print("False")

print(*sorted(first_line), sep=", ")
print(*sorted(second_line), sep=", ")
