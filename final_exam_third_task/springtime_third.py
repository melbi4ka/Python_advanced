def start_spring(**kwargs):

    new_dict = {}
    for key in kwargs:
        if kwargs[key] not in new_dict:
            new_dict[kwargs[key]] = []
        new_dict[kwargs[key]].append(key)


    sorted_new_dict = sorted(new_dict.items(), key = lambda x: (-len(x[1]), x[0]))

    for key, value in sorted_new_dict:
        yield f"{key}: "
        for el in sorted(value):
            yield f'-{el}'


        # yield е нещо като генератор на принтове, както си го направих отгоре за печат
        # като итерираш долу през него във функцията
        # то ти ги връща като принт


# подавам кваргс - получавам речник, който трябва да обърна в нов речник
# това, което е на велюто в кваргса трябва да стане ключ в новия речник
#  и ключа в кваргса трябва да стане велю в новия речник

# сортирам новия речник - първо по дължината на велюто в намаляващ ред, после по ключа в увеличаващ ред
# после минавам през ключа и велюто на сортирания речник
#  и  към един резълт добавям ключа и нов ред
#  като дойде време да добавям велюто
# го сортирам, тъй като и то трябва да е сортирано по азбучен ред и го добавям
#  накрая добавям празен ред
# печатам резултата
#  трябва да се внимава при този вид печат, тъй като дава един последен празен ред
#  и някъде джъдж може да ми го засече
#  затова може би първо ще трябва да мина през велюто на един речник
#  да го сортирам и после да направя другите две сортировки за да имам накрая един речник
# да го събера в лист компрехеншън и да печатам



example_objects = {
    "Water Lilly": "flower",
    "Swifts": "bird",
    "Callery Pear": "tree",
    "Swallows": "bird",
    "Dahlia": "flower",
    "Tulip": "flower",
}
for m in start_spring(**example_objects):
    print(m)


print("--------------------------")

example_objects = {
    "Swallow": "bird",
    "Thrushes": "bird",
    "Woodpeckers": "bird",
    "Swallows": "bird",
    "Warblers": "bird",
    "Shrikes": "bird",

}
print(start_spring(**example_objects))

print("------------------------------------")

example_objects = {
    "Magnolia": "tree",
    "Swallow": "bird",
    "Thrushes": "bird",
    "Pear": "tree",
    "Cherries": "tree",
    "Shrikes": "bird",
    "Butterfly": "insect",

}
print(start_spring(**example_objects))


