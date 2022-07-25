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


# подавам само аргументи, като знам, че командата ще е на последно място
#  във функцията я изкарвам от последното място
#  правя две проверки - ако командата е четна или ако командата е нечетна
#  във всяка проверка фор цикъл в аргументите без последния/тъй като той е командата
# съответно събирам в четно или нечетно
# връщам резултата

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))