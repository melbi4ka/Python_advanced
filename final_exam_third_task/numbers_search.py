def numbers_searching(*args):
    args_as_list = [*args]
    args_as_set = {*args}
    min_element = min(args_as_set)
    max_element = max(args_as_set)
    min_max_range = set(range(min_element, max_element+1))
    diff = min_max_range.difference(args_as_set)
    duplicates = [*diff, []]

    for el in args_as_set:
        counter = args_as_list.count(el)
        if counter > 1:
            duplicates[1].append(el)

    duplicates[1] = sorted(duplicates[1])

    return duplicates



print(numbers_searching(1, 2, 4, 2, 5, 4))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

# подават ни аргументи  - аргс
# първо записвам аргументите като лист
# после ги записвам като сет
# на сета намирам максималното и минималното число и правя рейндж - пак като сет от минималното до максималното +1
# правя дифрънс между рейнджа и първия сет
# разопаковяния дифрънс го слагам в лист - крайния резултат, с втори елемент празен лист
# минавам по елементите на първия сет
# ако елемента го преброя в листа, че го има повече от 1 - значи се повтаря
# апендвам в го листа от крайния резултат
# накрая сортирам листа - елемент 1 от крайния резултат и връщам крайния лист
