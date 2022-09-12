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



print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate", "banana"))

