def fill_the_box (*args):
    height, length, width = args[:3]
    size_of_box = height * length * width

    for el in args[3:]:
        if el == "Finish":
            break
        else:
            size_of_box -= el

    if size_of_box > 0:
        return f"There is free space in the box. You could put {size_of_box} more cubes."
    else:
        return f"No more free space! You have {abs(size_of_box)} more cubes."




print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))