import sys
from io import StringIO

input1 = '''1 2 -3 -4 65 -98 12 57 -84
'''
input2 = """1 2 3
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

def positive_and_negative(*args):
    positive = 0
    negative = 0
    for el in args:
        if el > 0:
            positive += el
        if el < 0:
            negative += el
    print(negative)
    print(positive)
    if abs(negative) > positive:
        print(f"The negatives are stronger than the positives")
    else:
        print(f"The positives are stronger than the negatives")


positive_and_negative(*[int(x) for x in input().split()])