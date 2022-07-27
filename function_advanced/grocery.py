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
