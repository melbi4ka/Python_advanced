import sys
from io import StringIO

input1 = '''10 16 13 25
12 11 8
'''
input2 = """10 14 22 4 5
11 16 17 11 1 8
"""
input3 = """5 6 7
2 1 5 7 5 3
"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

from collections import deque

energy = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]

# print(energy)
# print(materials)

counter = 0
toy = 0
total_energy = 0

while energy and materials:
    if energy[0] < 5:
        energy.popleft()
        continue

    elf = energy.popleft()
    material = materials.pop()
    counter += 1

    if counter % 3 == 0:
        if elf >= material * 2:
            elf -= material * 2
            elf += 1
            toy += 2
            if counter % 5 == 0:
                elf -= 1
                toy -= 2
            energy.append(elf)
            total_energy += material * 2
        else:
            energy.append(elf * 2)
            materials.append(material)
        continue

    if elf >= material:
        if counter % 5 != 0:
            elf -= material
            elf += 1
            toy += 1
            energy.append(elf)
            total_energy += material
        elif counter % 5 == 0:
            elf -= material
            energy.append(elf)
            total_energy += material
    else:
        energy.append(elf * 2)
        materials.append(material)

print(f"Toys: {toy}")
print(f"Energy: {total_energy}")
if energy:
    print(f"Elves left: {', '.join([str(x) for x in energy])}")
if materials:
    print(f"Boxes left: {', '.join([str(x) for x in materials])}")
