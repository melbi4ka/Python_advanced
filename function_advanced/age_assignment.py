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

# подавам аргс и куаргс
# на аргс изкарвам елементите и ги слигам в речник с валю 0
# след това обхождам създадения речник по ключове и с вътрешен цикъл обхождам ключовете на куаргс
#  ако първия индекс на името в новосъздания речник отговаря на ключа на куаргса
#  сменям валюто от 0 на това което е срещу ключа на куаргса
#  брейквам/ въприки че брейкването не ми прави проблем, възможно е в реален случай да трябва да се сменят няколко имена и може да е проблем
# сортирам речника - по ключа
# правя фор цикъл през сортирания речник и в един резултат добявям, ф-стринга с това, което трябва да се изпише и нов ред
# накрая връщам резултата


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))