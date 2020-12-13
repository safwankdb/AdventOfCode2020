def check2sum(N, summ=2020):
    S = set()
    for n in N:
        if summ-n in S:
            return(n, summ-n)
        S.add(n)
    return


def check3sum(N, summ=2020):
    N = sorted(N)
    for i, n in enumerate(N):
        ans = check2sum(N[i:], summ-n)
        if ans:
            return n, ans[0], ans[1]
    return


if __name__ == "__main__":
    with open('1.in') as f:
        N = [int(n) for n in f.readlines()]
    a, b = check2sum(N)
    print(a,b,a*b)
    a, b, c = check3sum(N)
    print(a,b,c,a*b*c)
