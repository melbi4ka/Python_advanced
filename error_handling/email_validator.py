class MustContainAtSymbolError(Exception):
    pass

class NameTooShortError(Exception):
    pass

class InvalidDomainError (Exception):
    pass

command = input()

while command != "End":
    email = command

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    username, domain = email.split("@")

    if len(username) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    extensions = (".com", ".bg", ".org", ".net")
    if domain.endswith(extensions):
        print(f"Email is valid")
    else:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    command = input()
