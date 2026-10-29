#!/usr/bin/python3
import itertools
import sys
from collections import defaultdict, deque
from copy import deepcopy

infile = sys.argv[1] if len(sys.argv) >= 2 else 'B.in'
with open('3.in') as f:
    lr, G = f.read().split('\n\n')
G = [list(line) for line in G.splitlines()]
R, C = len(G), len(G[0])
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


def getPermutation():
    g = [[(r, c) for c in range(C)] for r in range(R)]
    LR = itertools.cycle(lr.strip())
    for r in range(R):
        for c in range(C):
            if r > 0 and r < R-1 and c > 0 and c < C-1:
                OLD = {(dr, dc): G[r+dr][c+dc] for dr, dc in M.keys()}
                swap = next(LR) == 'R'
                for (fr, fc), (sr, sc) in M.items():
                    if swap:
                        fr, fc, sr, sc = sr, sc, fr, fc
                    G[r+fr][c+fc] = OLD[(sr, sc)]
    return {
        (r, c): g[r][c]
        for r in range(R)
        for c in range(C)
    }


def permutationMultiply(P, Q):
    C = {}
    for k in P.keys():
        C[k] = P[Q[k]]
    return C


def permutationPower(P, N):
    if N == 1:
        return P
    elif N % 2 == 0:
        return permutationPower(permutationMultiply(P, P), N//2)
    else:
        return permutationMultiply(P, permutationPower(P, N-1))


P = getPermutation()
N = 1048576000
P2 = permutationPower(P, N)


def applyPermutation(P, G):
    return [
        [G[rr][cc] for rr, cc in
         (P[(r, c)] for c in range(C))]
        for r in range(R)
    ]


G2 = applyPermutation(P2, G)

print('\n'.join(''.join(row) for row in G2))
