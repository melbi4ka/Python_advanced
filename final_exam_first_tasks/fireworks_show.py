import sys
from io import StringIO

input1 = '''5, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22
'''
input2 = """-15, -8, 0, -16, 0, -22
10, 5
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

from collections import deque

effects = deque([int(x) for x in input().split(", ")])
power = [int(x) for x in input().split(", ")]

# print(effects)
# print(power)
palm = 0
willow = 0
crossette = 0
have_fireworks = False

while effects and power:
    current_effect = effects.popleft()
    current_power = power.pop()

    if current_effect <= 0:
        power.append(current_power)
        continue

    if current_power <= 0:
        effects.appendleft(current_effect)
        continue

    sum_both = current_power + current_effect

    if sum_both % 3 == 0 and sum_both % 5 != 0:
        palm += 1
    elif sum_both % 5 == 0 and sum_both % 3 != 0:
        willow += 1
    elif sum_both % 5 == 0 and sum_both % 3 == 0:
        crossette += 1
    else:
        current_effect -= 1
        effects.append(current_effect)
        power.append(current_power)

    if willow >= 3 and palm >= 3 and crossette >= 3:
        have_fireworks = True
        break

if have_fireworks:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in effects)}")
if power:
    print(f"Explosive Power left: {', '.join(str(x) for x in power)}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")

# ефектите в дек, паура в стек
# брояч за видовете фойрверки, една булева променлива сетната на фолс дали имам по 3 бройки
# докато имам ефекти и пауър
# поплефтвам ефектите и попвам пауръ
# проверявам ги дали не са равни или под 0
# ако да - това, което не е под нула го връщам на мястото му и континиу
# ако са положителни - сумирам
# проверявам сумата по трите изисквания - за делене на 3 и 5
# ако влезе в една от тези проверки добавям съответната фойрверка
# ако не влезе в проверката намалям ефекта с 1 и го връщам накрая на опашката, връщам и пауъра
# ако междувременно и трите са станали по 3 или повече сетвам булевата на тру и брейквам
# печатам според това дали имам по 3 бр или не










