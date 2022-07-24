from os import listdir
from os.path import isdir, join

def directory_traversal(path, files_extensions_dict):
    for el in listdir(path):
        if isdir(join(path, el)):  #(f"{path}/{el}")
            directory_traversal(join(path, el), files_extensions_dict)
        else:
            extension = el.split(".")[-1]
            if extension not in files_extensions_dict:
                files_extensions_dict[extension] = []
            files_extensions_dict[extension].append(el)


final_state = {}
directory_traversal(f"{input()}/",  final_state)

sorted_final = sorted(final_state.items(), key = lambda x: x[0])

with open ("./report.txt", "w") as result:
    for key, value in sorted_final:
        result.write(f'.{key}\n')
        for val in sorted(value):
            result.write(f'- - - {val}\n')
