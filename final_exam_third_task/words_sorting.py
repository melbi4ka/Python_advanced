def words_sorting (*args):
    word_dict = {}
    all_sum = 0
    for word in args:
        if word not in word_dict:
            ord_sum = sum([ord(x) for x in word])
            word_dict[word] = ord_sum
            # word_dict[word] = sum(map(ord, word))
            all_sum += ord_sum
    if all_sum % 2 == 0:
        sorted_word_dict = sorted(word_dict.items(), key = lambda x: x[0])
    else:
        sorted_word_dict = sorted(word_dict.items(), key=lambda x: -x[1])
    for_print = ""
    for key, value in sorted_word_dict:
        for_print += f"{key} - {value}"
        for_print += "\n"

    return for_print

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
