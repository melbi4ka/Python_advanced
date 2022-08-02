import sys

from io import StringIO

input1 = """ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End
"""
input2 = """ROB-8
7:59:59
detail
glass
wood
sock
End
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

from collections import deque
def read_robots():
    result = {}
    robot_input = input().split(";")
    for n in robot_input:
        name, processing_time = n.split("-")
        processing_time = int(processing_time)
        result[name] = processing_time
    return result

def to_seconds(hours, minutes, seconds):
    return hours*60*60 + minutes*60 + seconds

def read_products():
    result = deque()
    while True:
        line = input()
        if line == "End":
            break
        else:
            result.append(line)
    return result

def to_str_time(time_in_seconds):
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds % 3600) // 60
    seconds = (time_in_seconds % 3600) % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots = read_robots()
available_robots = [n for n in robots.keys()]
processing_robots = {}
hh, mm, ss = [int(x) for x in input().split(':')]
time_in_seconds = to_seconds(hh, mm, ss)
products = read_products()

while products:
    time_in_seconds = (time_in_seconds + 1) % (24*60*60)

    for robot_name in [k for k in processing_robots.keys()]:
        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] <= 0:
            processing_robots.pop(robot_name)

    current_product = products.popleft()
    for robot_name in available_robots:
        if robot_name not in processing_robots:
            print(f'{robot_name} - {current_product} [{to_str_time(time_in_seconds)}]')
            processing_robots[robot_name] = robots[robot_name]
            break
    else:
        products.append(current_product)






