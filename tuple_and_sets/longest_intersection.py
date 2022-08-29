import sys
from io import StringIO

input1 = """3
0,3-1,2
2,10-3,5
6,15-3,10
"""
input2 = """5
0,10-2,5
3,8-1,7
1,8-2,4
4,7-2,5
1,10-2,11
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

n = int(input())
final_len = 0
final_result = set()

for _ in range (n):
    first,second = input().split("-")
    first_start, first_end = map(int,first.split(","))
    # print(first_start)
    second_start, second_end = map(int,second.split(","))

    first_set = set(range(first_start, first_end + 1))
    # print(first_set)
    second_set = set(range(second_start, second_end + 1))

    result = first_set.intersection(second_set)
    len_result = len(result)
    if final_len < len_result:
        final_len = len_result
        final_result = result


final_result = ', '.join([str(x) for x in final_result])
print(f"Longest intersection is [{final_result}] with length {final_len}")

