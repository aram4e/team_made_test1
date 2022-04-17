import math
import numpy as np
'''
vals = [i+1 for i in range(10)]
print(np.mean(vals))
print(np.var(vals))
print(np.std(vals))

vals2 = [i*2 for i in range(10)]
print(np.mean(vals2))
print(np.var(vals2))
print(np.std(vals2))
'''


def np_std(vals3):
    print(np.std(vals3))


a = [1, 1, 1]
b = [1, 2, 4]
c = [1, 2, 3]
d = [1, 1, 4]
e = [1, 1, 3]
f = [1, 2, 2]
g = [2, 2, 3]
h = [2, 3, 4]
j = [2, 2, 4]

alist = [a, b, c, d, e, f, g, h, j]

for v in alist:
    np_std(v), print(v)