import sys
from io import StringIO

input1 = '''105 20 30 25
120 60 11 400 10 1
'''
input2 = """30 5 21 6 0 91
15 9 5 15 8
"""
input3 = """200
5 15 32 20 10 5
"""

input4 = """100 500 20 8 7 300 56 
5 25 100 105 
"""


# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)
# sys.stdin = StringIO(input4)

from collections import deque

def what_gift(res):
    a_gift = ""
    if 100 <= res <= 199:
        a_gift = "Gemstone"
    elif res <= 299:
        a_gift = "Porcelain Sculpture"
    elif res <= 399:
        a_gift = "Gold"
    elif res <= 499:
        a_gift = "Diamond Jewellery"

    return a_gift

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

# print(materials)
# print(magic)
count_gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()

    result = current_material + current_magic

    if result < 100:
        if result % 2 == 0:
            result = (current_material * 2) + (current_magic * 3)
        else:
            result *= 2

    elif result > 499:
        result = result // 2

    if 100 <= result <= 499:
        gift = what_gift(result)
        if gift in count_gifts:
            count_gifts[gift] += 1

# print(count_gifts)
if count_gifts["Gemstone"] > 0 and count_gifts["Porcelain Sculpture"] > 0:
    print("The wedding presents are made!")
elif count_gifts["Gold"] > 0 and count_gifts["Diamond Jewellery"] > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

sorted_dict = sorted(count_gifts.items(), key = lambda x: x[0])
for key, value in sorted_dict:
    if value > 0:
        print(f"{key}: {value}")
