import sys
from io import StringIO

input1 = """10
5
Mercedes
green
Mercedes
BMW
Skoda
green
END
"""
input2 = """9
3
Mercedes
Hummer
green
Hummer
Mercedes
green
END
"""
input3 = """10
5
Mercedes
BMW
Skoda
green
END
"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)

from collections import deque


green = int(input())
free = int(input())

command = input()
queue = deque()
counter = 0
is_safe = True


while command != "END":
    if command != "green":
        car = command
        queue.append(car)

    else:
        green_light = green
        free_window = free
        while queue:
            pass_car = queue[0]
            if len(pass_car) <= green_light:
                green_light -= len(pass_car)
                queue.popleft()
                counter += 1

            elif len(pass_car) > green_light > 0:
                diff = len(pass_car) - green_light
                green_light = 0
                if diff <= free_window:
                    free_window -= diff
                    counter += 1
                    queue.popleft()
                elif diff > free_window:
                    print("A crash happened!")
                    crash_car = queue.popleft()
                    index = free_window
                    print(f"{crash_car} was hit at {crash_car[index+1]}.")
                    is_safe = False
                    break

            elif green_light == 0:
                break

    if not is_safe:
        break


    command = input()

if is_safe:
    print("Everyone is safe.")
    print(f"{counter} total cars passed the crossroads.")
