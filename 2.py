from parse import parse


def verify1(l, h, c, p):
    t = p.count(c)
    return t >= int(l) and t <= int(h)

def verify2(l, h, c, p):
    l = int(l) - 1
    h = int(h) - 1
    a =  p[l]==c
    b = p[h]==c
    return (a or b) and not (a and b)

if __name__ == "__main__":
    fmt = "{}-{} {}: {}"
    counter = 0
    with open('2.in') as f:
        data = f.readlines()
        for d in data:
            correct = verify1(*parse(fmt, d))
            if correct:
                counter += 1
    print(counter)

    counter = 0
    with open('2.in') as f:
        data = f.readlines()
        for d in data:
            correct = verify2(*parse(fmt, d))
            if correct:
                counter += 1
    print(counter)
