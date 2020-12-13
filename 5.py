with open('5.in') as f:
    data = f.readlines()

m = 0
for d in data:
    d = d.strip()
    d = d.replace('R','1')
    d = d.replace('B','1')
    d = d.replace('F','0')
    d = d.replace('L','0')
    d = int(d, 2)
    m = max(d, m)
print(m)

arr = []
for d in data:
    d = d.strip()
    d = d.replace('R','1')
    d = d.replace('B','1')
    d = d.replace('F','0')
    d = d.replace('L','0')
    d = int(d, 2)
    arr.append(d)
lo = min(arr)
hi = max(arr)
print(hi*(1+hi)//2 - lo*(lo-1)//2 - sum(arr))
