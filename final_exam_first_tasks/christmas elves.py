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

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

from collections import deque

energy = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]

# print(energy)
# print(materials)

counter = 0
toy = 0
total_energy = 0

while energy and materials:
    current_energy = energy.popleft()
    current_materials = materials.pop()

    if current_energy < 5:
        materials.append(current_materials)
        continue

    counter += 1

    if counter % 3 == 0 and current_energy >= current_materials * 2:
        current_energy -= (current_materials * 2) - 1
        toy += 2
        total_energy += current_materials * 2
        if counter % 5 == 0:
            current_energy -= 1
            toy -= 2
        energy.append(current_energy)
        continue
    elif counter % 3 == 0 and current_energy < current_materials * 2:
        current_energy *= 2
        energy.append(current_energy)
        materials.append(current_materials)
        continue

    if counter % 5 == 0 and current_energy >= current_materials:
        current_energy -= current_materials
        total_energy += current_materials
        continue
    elif counter % 5 == 0 and current_energy < current_materials :
        current_energy *= 2
        energy.append(current_energy)
        materials.append(current_materials)
        continue

    if counter % 5 != 0 and counter % 3 != 0 and current_energy >= current_materials:
        current_energy -= current_materials - 1
        energy.append(current_energy)
        toy += 1
        total_energy += current_materials
    else:
        current_energy *= 2
        energy.append(current_energy)
        materials.append(current_materials)


print(f"Toys: {toy}")
print(f"Energy: {total_energy}")
if energy:
    print(f"Elves left: {', '.join([str(x) for x in energy])}")
if materials:
    print(f"Boxes left: {', '.join([str(x) for x in materials])}")

# 69/100 и още не мога да си намеря грешката






