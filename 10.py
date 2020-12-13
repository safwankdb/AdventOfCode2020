with open('10.in') as f:
    a = [int(i) for i in f.readlines()]
a.append(0)
a.append(max(a)+3)
a.sort()
b = [a[i+1]-a[i] for i in range(len(a)-1)]
print(b.count(1), b.count(3), b.count(1)*b.count(3))

S = {}

def no_of_paths(i, j):
    if i == j: return 1
    if i in S: return S[i]
    children = [i+k for k in range(1,4) if i+k < len(a) and a[i+k]-a[i] < 4]
    S[i] = sum(no_of_paths(c, j) for c in children)
    return S[i]

print(no_of_paths(0, len(a)-1))
