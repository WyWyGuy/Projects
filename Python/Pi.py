import math

answer = 1
top = math.sqrt(2)
full = top/2
answer = answer*full

for x in range(100):
    oldtop = top
    top = math.sqrt(2 + oldtop)
    full = top/2
    answer = answer*full

print(2 / answer)