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


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
