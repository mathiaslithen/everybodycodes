#!/usr/bin/python3
import itertools
import sys

# permutations

with open(sys.argv[1]) as f:
    lr, grid = f.read().split('\n\n')
G = [list(line) for line in grid.splitlines()]
R, C = len(G), len(G[0])
G_START = [[G[r][c] for c in range(C)] for r in range(R)]
M = {
    (-1, -1): (-1, 0),
    (-1, 0): (-1, 1),
    (-1, 1): (0, 1),
    (0, 1): (1, 1),
    (1, 1): (1, 0),
    (1, 0): (1, -1),
    (1, -1): (0, -1),
    (0, -1): (-1, -1),
}
RP = [
    (r, c)
    for r in range(R)
    for c in range(C)
    if r > 0 and r < R-1 and c > 0 and c < C-1
]


def getPermutation():
    g = [[(r, c) for c in range(C)] for r in range(R)]
    LR = itertools.cycle(lr.strip())
    for r, c in RP:
        OLD = {(dr, dc): g[r+dr][c+dc] for dr, dc in M.keys()}
        if next(LR) == 'L':
            for (fr, fc), (sr, sc) in M.items():
                g[r+fr][c+fc] = OLD[(sr, sc)]
        else:
            for (sr, sc), (fr, fc) in M.items():
                g[r+fr][c+fc] = OLD[(sr, sc)]
    return {
        (r, c): g[r][c]
        for r in range(R)
        for c in range(C)
    }


def permutationMultiply(P, Q):
    return {k: P[Q[k]] for k in P}


def permutationPower(P, N):
    if N == 1:
        return P
    if N % 2 == 0:
        return permutationPower(permutationMultiply(P, P), N//2)
    return permutationMultiply(P, permutationPower(P, N-1))


P = getPermutation()
N = int(sys.argv[2]) if len(sys.argv) > 2 else 1048576000
P2 = permutationPower(P, N)


def applyPermutation(P, G):
    return [
        [
            G[rr][cc]
            for rr, cc
            in (P[(r, c)] for c in range(C))
        ]
        for r in range(R)
    ]


G2 = applyPermutation(P2, G)

print('\n'.join(''.join(row) for row in G2))
