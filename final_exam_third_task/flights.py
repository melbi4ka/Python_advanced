def flights (*args):

    fly_dict = {}
    for el in range(0, len(args) - 1, 2):
        if args[el] == "Finish":
            return fly_dict
        else:
            destination = args[el]
            passengers = int(args[el+1])
            if destination not in fly_dict:
                fly_dict[destination] = 0
            fly_dict[destination] += passengers

    return fly_dict

# 100/100
# получавам всичките параметри като аргс
# създавам празен речник
# почвам да ги обикалям от нула до края на аргс -1 със стъпка 2
# ако получа Finish - връщам каквото съм събрала в речника, ако не

# ако елемента го няма в речника го добавям като ключ - дестинацията
# и към нея добавям това което е в арг на елемент +1 - т.е хората
# накрая връщам речник


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))



