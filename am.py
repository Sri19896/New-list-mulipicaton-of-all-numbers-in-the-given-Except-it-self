

from numpy import product

l = [3, 2, 1]
f = []
for i in l:
    s = product(l) / i
    f.append(int(s))
print(f)
