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

# 100/100 но заради грешно изписване на дафодила ми изкърти нервите с 83
# гласните в дек, съгласните в стек
#  цветята в един лист и едно копие на листа
#  уайл цикъл докато имам гласни или съгласни
# поплефтвам първия елемент на дека и попвам последния на стека
# правя един цикъл в дължината на листа на цветята
#  вземам всеки елемент от листа, т.е съответното цвете и гледам гласната или съгласната дали ги има в него
# ако ги има ги заменям с празен стринг
# и така докато някоя от думите стане празен стринг
# после проверявам дали дължината на текущата дума е станала 0
#  ако е станала нула съм открила съвпадението, печатам текста, сменям булевата променлива и брейквам
#  брейквам и вътрешния цикъл
#  при сменена булева променлива печатам текста, че не съм намерила и после останалите елементи
