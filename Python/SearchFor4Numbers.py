import re

input = ""

regex = r"\d{4}"

output = re.findall(regex, input)

print(output)