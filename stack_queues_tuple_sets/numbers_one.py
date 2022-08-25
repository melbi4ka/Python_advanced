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

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

def unique_numbers(nums):
    unique_set = set()
    for n in nums:
        unique_set.add(int(n))
    return unique_set

first_line = unique_numbers(input().split())
second_line = unique_numbers(input().split())
# print(first_line)
# print(second_line)

number = int(input())

for _ in range(number):
    command = input().split()
    if command[0] == "Add":
        new_set = set(map(int, command[2:]))
        if command[1] == "First":
            first_line = first_line.union(new_set)
            # [first_line.add(int(x)) for x in command[2:]]

        elif command[1] == "Second":
            second_line = second_line.union(new_set)

    elif command[0] == "Remove":
        numbers = [int(x) for x in command[2:]]
        if command[1] == "First":
            for n in numbers:
                if n in first_line:
                    first_line.remove(n)

        if command[1] == "Second":
            for n in numbers:
                if n in second_line:
                    second_line.remove(n)

    elif command[0] == "Check":
        if first_line.issubset(second_line) or second_line.issubset(first_line):
            print("True")
        else:
            print("False")

print(*sorted(first_line), sep=", ")
print(*sorted(second_line), sep=", ")
