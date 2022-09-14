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
