import numpy as np
text=np.loadtxt(fname = "this.txt")

list = []
num = 0

for i in text:
    list.append(int(i))
    

for i in list:
    if (i % 2) == 0:
        num = num + i
    else:
        num = num - i

print(num)