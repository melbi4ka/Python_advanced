from collections import deque


def list_manipulator (*args):
    nums_list = deque(args[0])
    first_action = args[1]
    second_action = args[2]

    if first_action == "add" and second_action == "beginning":
        numbers = args[3:]
        for el in numbers[::-1]:
            nums_list.appendleft(el)

    elif first_action == "add" and second_action == "end":
        numbers = args[3:]
        for el in numbers:
            nums_list.append(el)

    elif first_action == "remove" and second_action == "beginning":
        if len(args) > 3:
            counter = args[3]
            while counter > 0:
                nums_list.popleft()
                counter -= 1
        else:
            nums_list.popleft()

    elif first_action == "remove" and second_action == "end":
        if len(args) > 3:
            counter = args[3]
            while counter > 0:
                nums_list.pop()
                counter -= 1
        else:
            nums_list.pop()

    return [*nums_list]


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

# 100/100
# получавам всичко като аргс
# арг от 0 - ми е листа, който ще обработвам - правя го в дек
# аргс от 1 ми е първата команда
# аргс от 2 ми е втората команда
# правя различни иф проверки за комбинацията от команди
# ако добавям в началото
# - имам номер/а, които са ми аргс от 3 нататък
# - обикалям ги наобратно
# - апендлефтвам ги в листа

# ако довям в края
# - имам номер/а, които са ми аргс от 3 нататък
# - обикалям ги нормално
# - апендвам ги в листа

# ако махам от началото
# ако имам цифра – (има цифра, ако лен на аргументите ми е по-голям от 3)
# - каунтъра ми е равен на тази цифра
# - докато каунтъра ми е по-голям от 0 -  поплефтвам първия елемент
# ако няма цифра - поплефтвам само първия елемент

# ако махам от края
# ако имам цифра – (има цифра, ако лен на аргументите ми е по-голям от 3)
# - каунтъра ми е равен на тази цифра
# - докато каунтъра ми е по-голям от 0 - попвам последния елемент
# ако няма цифра - попвам последния елемент


