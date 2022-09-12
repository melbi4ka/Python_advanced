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
