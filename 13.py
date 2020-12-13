import numpy as np

with open("13.in") as f:
    x = int(f.readline())
    t = [i for i in f.readline().strip().split(",")]
    y = [int(i) for i in t if i != "x"]


## Part 1
a = [i - x % i for i in y]
res = y[np.argmin(a)]
print((min(a)) * res)

## Part 2
def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = extended_euclidean(a, m)
    return x % m

def crt(m, x):
    while True:
        temp1 = modinv(m[1], m[0]) * x[0] * m[1] + modinv(m[0], m[1]) * x[1] * m[0]
        temp2 = m[0] * m[1]
        x.remove(x[0])
        x.remove(x[0])
        x = [temp1 % temp2] + x
        m.remove(m[0])
        m.remove(m[0])
        m = [temp2] + m
        if len(x) == 1:
            break
    return x[0]

m = [i for i in range(len(t)) if t[i] != "x"]
m = [x % int(t[i]) - i for i in m]
ans = crt(y, m)
print(ans - x)
