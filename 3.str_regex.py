import re

password = input("Password: ")

# Regular Expression
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{12,}$'

if re.match(pattern, password) == True:
    print('Valid')
else:
    print('Invalid')

# ^                       # start of string
# (?=.*[a-z])             # at least one lowercase
# (?=.*[A-Z])             # at least one uppercase
# (?=.*\d)                # at least one digit
# (?=.*[!@#$%^&*()_\-+=\[\]{};:'",.<>?/\\|`~])  # at least one special char
# .{12,}                  # at least 12 characters
# $                       # end of string