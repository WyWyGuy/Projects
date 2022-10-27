input = ""

reversedInput = input[::-1]

commas = (','.join(reversedInput[i:i+3] for i in range(0, len(reversedInput), 3)))

output = commas[::-1]

print(output)