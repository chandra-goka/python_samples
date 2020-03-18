import re

# Reg Expression
# Removing Begining of a String
str = '    hello  python   '
str = re.sub(r"^\s+", "", str, flags=re.UNICODE)
print("removed spaces at left side :",str)

# Ending of a string
str = '    hello  python   '
str = re.sub(r"\s+$", "", str, flags=re.UNICODE)
print("removed spaces at right side :",str)

# Removing Begining and Ending
str = '    hello  python   '
str = re.sub("^\s+|\s+$", "", str, flags=re.UNICODE)
print("removed spaces at both sides :",str)

# Removing all spaces
str = ' hello  python   '
pattern = re.compile(r'\s+')
str = re.sub(pattern, '', str)
print(str)