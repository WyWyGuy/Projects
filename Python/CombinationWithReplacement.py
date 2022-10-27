from math import factorial

n = 
r = 

top = factorial(n + r - 1)
bottom = (factorial(r))*(factorial((n - 1)))
print(int(top/bottom))