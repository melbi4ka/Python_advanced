import sys
from io import StringIO

input1 = '''o e a o e a i
p r s x r
'''
input2 = """a a a
x r l t p p
"""
input3 = """u a o i u y o e
p m t l
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)
from collections import deque

vowels = deque(input().split())
# print(vowels)
consonants = input().split()
# print(consonants)

flowers = ["rose", "tulip", "lotus", "daffodil"]
flowers_as_copy = flowers.copy()

is_found = False
while vowels and consonants:
    current_vow = vowels.popleft()
    current_cons = consonants.pop()

    for flo in range(len(flowers)):
        if current_vow in flowers[flo]:
            unrevealed_part = flowers[flo].replace(current_vow, "")
            flowers[flo] = unrevealed_part
        if current_cons in flowers[flo]:
            unrevealed_part = flowers[flo].replace(current_cons, "")
            flowers[flo] = unrevealed_part

        if len(flowers[flo]) == 0:
            is_found = True
            print(f"Word found: {flowers_as_copy[flo]}")
            break

    if is_found:
        break


if not is_found:
    print(f"Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
