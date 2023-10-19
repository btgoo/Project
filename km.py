import re

number = '07748240391'
x = re.search("07", number)

print(x.group())