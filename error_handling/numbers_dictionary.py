import sys
from io import StringIO

input1 = '''one
1
two
2
Search
ten
Remove
two
End
'''
input2 = """one
two
Search
Remove
End
"""
input3 = """one
1
Search
one
Remove
two
End
"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)


numbers_dictionary = {}

line = input()

while line != "Search":
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print(f"The variable number must be an integer")
    line = input()

line = input()

while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError:
        print(f"Number does not exist in dictionary")
    line = input()

line = input()

while line != "End":
    try:
        searched = line
        del numbers_dictionary[searched]
    except KeyError:
        print(f"Number does not exist in dictionary")
    line = input()

print(numbers_dictionary)
