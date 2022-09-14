def shopping_list(budget, **kwargs):

    products = 0
    print_list = []
    if budget >= 100:
        for key in kwargs:
            price, quantity = kwargs[key]
            total_price = price * quantity
            if total_price <= budget:
                budget -= total_price
                print_list.append(f"You bought {key} for {total_price:.2f} leva.")
                products += 1
            if products == 5:
                break
    else:
        print_list.append("You do not have enough budget.")

    return "\n".join(print_list)

# подавам бюджет и куаргс, които ми стават като речник
# проверявам дали бюджета ми е над 100 лв
# ако е над 100, почвам да обикалям ключовете в кваргс
# ако е под 100 - в лист за печат добавям че нямам достатъчно бюджет
# цената и количеството са във велюото на всеки ключ, умножавам ги
# ако цената по количеството е по-малка от бюджета - намалям бюджета с тази сума
# към речника за печат добавям каквото трябва да се печата
# увеличавам каунтъра за продукти с 1
# когато продуктите станат 5 брейквам
# накрая печатам листа за печат всяко на нов ред

print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print("-------------------------")
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print("-------------------------")
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
