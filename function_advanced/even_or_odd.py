def even_odd(*args):
    command = args[-1]
    even_nums = []
    odd_nums = []
    if command == "even":
        for el in args[:-1]:
            if el % 2 == 0:
                even_nums.append(el)
        return even_nums

    elif command == "odd":
        for el in args[:-1]:
            if el % 2 == 1:
                odd_nums.append(el)
        return odd_nums



print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
