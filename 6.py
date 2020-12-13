with open("6.in") as f:
    data = [a.split('\n') for a in f.read().split("\n\n")]

c = 0
for i in data:
    S = set()
    for j in i:
        S = S.union(set(j))
    c += len(S)
print(c)

c = 0
for i in data:
    S = set(i[0])
    for j in i[1:]:
        S = S.intersection(set(j))
    c += len(S)
print(c)
