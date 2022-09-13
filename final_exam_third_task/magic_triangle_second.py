def get_magic_triangle(num_rows):
    list = []  # an empty list
    for n in range(num_rows):
        list.append([])
        list[n].append(1)
        for m in range(1, n):
            list[n].append(list[n - 1][m - 1] + list[n - 1][m])
        if n != 0:
            list[n].append(1)
    return list

print(get_magic_triangle(5))

# 100/100 решение от нетя за Pascal triangle
