class MustContainAtSymbolError(Exception):
    pass

class NameTooShortError(Exception):
    pass

class InvalidDomainError (Exception):
    pass

import sys
from io import StringIO

input1 = '''abc@abv.bg
'''
input2 = """peter@gmail.com
petergmail.com
"""
input3 = """peter@gmail.hotmail
"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)



command = input()
while command != "End":
    email = command

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    username, domain = email.split("@")

    if len(username) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    # domain_name, domain_extension = domain.split(".")
    extensions = (".com", ".bg", ".org", ".net")
    if domain.endswith(extensions):
        print(f"Email is valid")
    else:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")


    command = input()
