import sys
from io import StringIO

input1 = """4
Pesho
Stefan
Stamat
Gosho
"""
input2 = """6
Preslav
Gosho
Ivan
Stamat
Pesho
Stefan
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

n = int(input())
odd_set = set()
even_set = set()

for i in range(1, n+1):
    text = input()

    text_sum = int(sum(ord(ch) for ch in text) / i)
    # print(text_sum)
    if text_sum % 2 == 0:
        even_set.add(text_sum)
    else:
        odd_set.add(text_sum)

sum_even_set = sum(even_set)
sum_odd_set = sum(odd_set)
result = set()

if sum_odd_set == sum_even_set:
    result = odd_set.union(even_set)

elif sum_odd_set > sum_even_set:
    result = odd_set.difference(even_set)

elif sum_odd_set < sum_even_set:
    result = odd_set.symmetric_difference(even_set)

print(*result, sep = ", ")
