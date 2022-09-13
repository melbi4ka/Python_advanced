def naughty_or_nice_list(*args, **kwargs):
    santas_dict = {"Nice": [], "Naughty": [], "Not found": []}

    first_list = args[0]
    santas_list = []
    for num, name in first_list:
        santas_list.append(num)
        santas_list.append(name)

    for el in args[1:]:
        number, command = el.split("-")
        number = int(number)
        counter = santas_list.count(number)
        if counter == 1:
            idx = santas_list.index(number)
            santas_dict[command].append(santas_list[idx+1])
            del santas_list[idx:idx+2]

    for key in kwargs:
        if key in santas_list:
            counter = santas_list.count(key)
            if counter == 1:
                kid_name = key
                behaviour = kwargs[key]
                santas_dict[behaviour].append(kid_name)
                idx = santas_list.index(kid_name)
                del santas_list[idx - 1:idx + 1]

    for el in santas_list[1::2]:
        santas_dict["Not found"].append(el)

    res = [f"{key}: {', '.join(value)}" for key, value in santas_dict.items() if value]
    return '\n'.join(res)


# Подавам аргс и куаргс като параметри
# Нулевия елемент на аргс ми е листа с тюпълите
# Разопаковам го и го поставям в обикновен лист - подреден номер, име, номер, име
# Правя си най-отгоре един речник - ключове добро, лошо и ненамерено дете и велюта - празни листи
# Почвам да обикалям следващите команди след листа, сплитвам ги по "-" и получавам номер и поведение
# Проверявам номера дали и колко пъти се намира в обикновения лист - с метода count()
#  Ако метода ми върне веднъж вземам индекса на този номер и в речника на поведението
#  добавям името, което е на индекс +1
# трия листа от индекса до индекса +2  - да ми изтрие номера и името

# после минавам през ключовете в кваргс, ако има
# там ключа е име, ако това име е в обикновения лист, пак изчислявам колко пъти го има с метода count()
#  ако ми върне веднъж вземам име и поведение от кваргс и ги слагам речника на дядо коледа
#  намирам индекса където е детето в листа и го трия - от индекс -1 до индекс +1 за да изтрие номера и детето

# накрая всичко, което е останало в листа го апендвам към ненамерени
# правя компрехеншън за стойностите в дикта с проверка дали имат нещо във велюто си и печатам само тези,
#  които имат велю




print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    "1-Nice",
    Amy="Nice",
    Katy="Naughty",
))

# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))

# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))

