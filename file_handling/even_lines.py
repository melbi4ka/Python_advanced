symbols = ["-", ",", ".", "!", "?"]

with open("./text.txt", "r") as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            res = line.strip().split()
            res = ' '.join(res[::-1])
            for symbol in symbols:
                if symbol in res:
                    res = res.replace(symbol, "@")
            print(res)
            