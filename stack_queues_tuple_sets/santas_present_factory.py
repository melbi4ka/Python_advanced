import sys
from io import StringIO


input1 = """10 -5 20 15 -30 10
40 60 10 4 10 0
"""
input2 = """30 5 15 60 0 30
-15 10 5 -15 25
"""
input3 = """30 10
15 10 5 0 10
"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])
doll = 0
train = 0
bike = 0
bear = 0
gifts = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}
counted_toys = {}



while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()

    result = current_magic * current_material

    if current_material == 0 and current_magic == 0:
        continue

    elif current_material == 0:
        magic.appendleft(current_magic)
        continue

    elif current_magic == 0:
        materials.append(current_material)
        continue


    if result in gifts:
        toy = gifts[result]

        if toy not in counted_toys:
            counted_toys[toy] = 0
        counted_toys[toy] += 1


    else:
        if result < 0:
            result = current_material + current_magic
            materials.append(result)

        elif result > 0:
            materials.append(current_material + 15 )


if ("Doll" in counted_toys and "Wooden train" in counted_toys) or ("Teddy bear" in counted_toys and "Bicycle" in counted_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str (x) for x in materials[::-1]])}")

if magic:
    print(f"Magic left: {', '.join([str (x) for x in magic])}")

for name, value in sorted(counted_toys.items()):
    # sorted_name = sorted(name)
    print(f"{name}: {value}")
    
