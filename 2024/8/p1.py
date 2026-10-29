BLK = 4097688


def p1(b):
    tot = rem = 0
    n = 1
    while b:
        needed = 2*n-1
        if needed > b:
            rem = needed-b
            tot += b
            break
        else:
            b -= needed
            tot += needed
        n += 1

    w = (n-1)*2-1
    if needed-rem == 1:
        w += 1
    else:
        w += 2
    print(rem*w)


p1(BLK)


X = 735


def p2(N):
    mul = 3
    mod = 5
    B = 50
    s = 1
    tot = rem = 0
    for _ in range(mod):
        s = (s*mul) % mod

