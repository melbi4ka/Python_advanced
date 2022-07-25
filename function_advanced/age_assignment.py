def age_assignment (*args, **kwargs):

    final_dict = {}
    for el in args:
        if el not in final_dict:
            final_dict[el] = 0
    for name in final_dict.keys():
        # print(key)
        for key in kwargs:
            if name[0] == key:
                final_dict[name] = kwargs[key]
                break
    sorted_final_dict = sorted(final_dict.items(), key = lambda x: x[0])
    res = ""
    for name, age in sorted_final_dict:
        res += f"{name} is {age} years old."
        res += "\n"
    return  res


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
