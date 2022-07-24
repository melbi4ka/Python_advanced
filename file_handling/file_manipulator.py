import sys
from io import StringIO

input1 = '''Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
Delete-random.txt
Delete-file.txt
End
'''

# sys.stdin = StringIO(input1)

from os.path import exists
from os import remove

command = input()

while command != "End":
    command_parts = command.split("-")
    action, file = command_parts[0], command_parts[1]

    if action == "Create":
        with open (f"./{file}", "w") as new_file:
            pass
    elif action == "Add":
        text = command_parts[2]
        with open(f"./{file}", "a") as new_file:
            new_file.write(text + '\n')

    elif action == "Replace":
        try:
            old_text = command_parts[2]
            new_text = command_parts[3]
            with open(f"./{file}", "r+") as new_file:
                content = new_file.read().replace(old_text, new_text)
                new_file.seek(0)
                new_file.truncate(0)
                new_file.write(content)
        except FileNotFoundError:
            print(f"An error occurred")

    elif action == "Delete":
        if not exists(f"./{file}"):
            print(f"An error occurred")
        else:
            remove(f"./{file}")

    command = input()
