def concatenate(*args, **kwargs):
    a=5
    text = ""
    for el in args:
        text += el
    for key in kwargs:
        if key in text:
            text = text.replace(key, kwargs[key])
    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
