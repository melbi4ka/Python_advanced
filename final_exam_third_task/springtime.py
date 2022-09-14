def start_spring(**kwargs):
    new_dict = {}
    for key in kwargs:
        if kwargs[key] not in new_dict:
            new_dict[kwargs[key]] = []
        new_dict[kwargs[key]].append(key)

    sorted_new_dict = sorted(new_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""

    for key, value in sorted_new_dict:
        result += f"{key}:"
        result += "\n"
        for el in sorted(value):
            result += f"-{el}"
            result += '\n'

    return result




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
