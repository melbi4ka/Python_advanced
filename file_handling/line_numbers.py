import re

def count_letters(text):
    letter_pattern = r"[A-Za-z]"
    result_one = re.findall(letter_pattern, text)
    punctuation_pattern = r"[\!\"\#\$\\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\]\^\_\`\{\|\~\.]"
    result_two = re.findall(punctuation_pattern,text)
    return len(result_one), len(result_two)


with open("./text.txt", "r") as file, open ("./output.txt", "w") as result:
    for index, line in enumerate(file):
        letters, punctuation  = count_letters(line)
        result.write(f"Line {index+1}: {line.strip()} ({letters})({punctuation})\n")





