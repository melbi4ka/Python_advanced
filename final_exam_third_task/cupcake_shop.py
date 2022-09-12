from collections import deque

def stock_availability (*args):
    inventory_boxes = deque(args[0])
    actions = args[1:]

    for el in range(len(actions)):
        if actions[el] == "delivery":
            new_additions = actions[el+1:]
            inventory_boxes.extend(new_additions)

        elif actions[el] == "sell":
            if actions[el] == actions[-1]:
                inventory_boxes.popleft()
            elif str(actions[el+1]).isdigit():
                sold_number = actions[el+1]
                while sold_number > 0:
                    inventory_boxes.popleft()
                    sold_number -= 1
            elif not actions[el+1].isdigit():
                sold_flavour = actions[el+1:]
                for flavour in sold_flavour:
                    if flavour in inventory_boxes:
                        inventory_boxes = [x for x in inventory_boxes if x != flavour]

    inventory_boxes = [x for x in inventory_boxes]

    return inventory_boxes

# подавам аргументи
# кутиите ми са в аргументите на 0 - в дек
# действията ми са в аргументите от 1 нататък
# въртя цикъл върху рейнджа на действията
# ако действието ми е равно на деливъри - новите придобивки са от елемента +1 нататък
# екстендвам кутиите с новите придобивки
#  ако действието ми е равно на сел -
# - ако сел е последната команда, т.е няма други след нея, поплефтвам първия елемент
#  - ако следващата команда е число, въртя един уайл цикъл докато числото е по-голямо от нула
#  и поплефтвам толкова пъти, колкото е казано
# - ако следващата команда не е число, значи след сел има стрингове, които са от сел нататък
# въртя един фор цикъл през следващите команди и проверявам дали командата я има в първоначалния списък
# ако е там правя един лист компрехеншън и оставям само тези елементи в първоначалния списък, които са различни
#  от елемента
# накрая кутиите ги подреждам от дек в лист
#  връщам листа





print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate", "banana"))

