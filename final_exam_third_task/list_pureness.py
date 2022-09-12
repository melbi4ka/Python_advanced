import sys
from collections import deque

def best_list_pureness(a_list, number):
    queue = deque(a_list)
    counter = 0
    best_pureness = -sys.maxsize
    rotation = 0

    while counter <= number:

        all_sum = 0
        for index, num in enumerate(queue):
            all_sum += index * num

        if all_sum > best_pureness:
            best_pureness = all_sum
            rotation = counter

        last = queue.pop()
        queue.appendleft(last)
        counter += 1

    return f"Best pureness {best_pureness} after {rotation} rotations"


test = ([-4, -3, -2, -6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

# 100/100
# подавам аргументите като позиционни, първия е лист, втория е число
# листа го правя в дек
# сетвам на 0 три променливи, каунтър, ротация и бест пюрнес
# въртя уайл цикъл докато каунтъра ми е по-малък от числото
# в него фор цикъл индекс, число в енумерейт на дека
# изчислявам сума и ако сумата е по-голяма от бест пюрнес сетвам сумата и ротацията,
# която е равна на каунтъра преди да се увеличи
# накрая попвам последния елемент, слагам го най-отпред и въртя отново
# увеличавам каунтъра
