import sys
from io import StringIO

input1 = """{[()]}
"""
input2 = """{[(])}
"""

input3 = """{{[[(())]]}}"""
input4 = """)}]"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)
sys.stdin = StringIO(input4)


opening = [chr for chr in input()]
closing = []

while opening:
    chr = opening[-1]

    if chr in ")}]":
        closing.append(opening.pop())
    elif chr in "([{":
        if len(closing) > 0:

            cls = closing[-1]
            if chr + cls == "("")" or chr + cls == "[""]" or chr + cls == "{""}":
                opening.pop()
                closing.pop()
            else:
                opening.pop()
        else:
            break

if len(closing) == 0 and len(opening) == 0:
    print("YES")
else:
    print("NO")
