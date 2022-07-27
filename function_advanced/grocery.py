def grocery_store (**kwargs):
    a=5
    sorted_kwargs = sorted(kwargs.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))
    res = ""
    for name, quantity in sorted_kwargs[:-1]:
        res += f"{name}: {quantity}"
        res += "\n"
    for name, quantity in sorted_kwargs[-1:]:
        res += f"{name}: {quantity}"

    return res

# с куаргс получавам речник, който сортирам
# подавам речника по айтъми / тюпъли
# ключа е първо по намаляващ ред по велюто/бройката
# ако са еднакви, по намаляващ ред на дължината на името/ключа
# ако и дължините са еднакви, по възходящ ред на буквите на името
#  после минавам през елементите на тюпъла и ги събирам в един резултат
#  за да не получа празен ред - ползвам два цикъла - до предпоследния елемент където добавям празен ред
#  за последния елемент ползвам отделен цикъл - без празен ред
# 100/100

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
