import sys
from io import StringIO

input1 = '''4 6
'''
input2 = """3 2
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)


row, col = [int(x) for x in input().split()]
aplphabet = {
    0: "a", 1: "b", 2: "c",
    3: "d", 4: "e", 5: "f",
    6: "g", 7: "h", 8: "i",
    9: "j", 10: "k", 11: "l",
    12: "m", 13: "n", 14: "o",
    15: "p", 16: "q", 17: "r",
    18: "s", 19: "t", 20: "u",
    21: "v", 22: "w", 23: "x",
    24: "y", 25: "z",
}
matrix = []

for r in range(row):
    combinations = []
    for c in range(col):
        letters = (aplphabet[r] + aplphabet[r+c] + aplphabet[r])
        combinations.append(letters)
    matrix.append(combinations)
    print(f"{' '.join(matrix[r])}")

