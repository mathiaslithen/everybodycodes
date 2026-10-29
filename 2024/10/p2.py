#!/usr/bin/pypy3
import sys

with open(sys.argv[1])as f:
    G = f.read().split('\n\n')


def f(g):
    s = ''
    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] != '.':
                continue
            rr = set(x for x in g[r] if x != '.')
            cc = set(g[x][c] for x in range(len(g)) if g[x][c] != '.')
            x = rr & cc
            assert len(x) == 1, print(g, x)
            s += (rr & cc).pop()
    print(s, score(s))
    return score(s)


def T(x):
    return list(map(list, zip(*x)))


def score(s):
    return sum(ix * (ord(c)-64) for ix, c in enumerate(s, start=1))


def parse(G):
    grids = []
    for x in G:
        a = []
        for y in T(x.splitlines()):
            if all(not b.strip() for b in y):
                grids.append(T(a))
                a = []
            else:
                a.append(y)
        grids.append(T(a))
    return grids


ans = sum(f(g) for g in parse(G))
print(ans)
