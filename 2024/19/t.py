import itertools
import sys

DX = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
)
LL = (1, 2, 4, 0, 7, 3, 5, 6)
RR = (3, 0, 1, 5, 2, 6, 7, 4)


with open(sys.argv[1]) as f:
    lr, grid = f.read().split('\n\n')
G = [list(line) for line in grid.splitlines()]
R, C = len(G), len(G[0])
RP = [
    (r, c)
    for r in range(R)
    for c in range(C)
    if not (r == 0 or r == R-1 or c == 0 or c == C-1)
]

LR = itertools.cycle(lr.strip())


def rot(r, c):
    P = [(r+dr, c+dc) for dr, dc in DX]
    d = [G[r][c] for r, c in P]
    d = [d[i] for i in (LL if next(LR) == 'L' else RR)]
    for (r, c), v in zip(P, d):
        G[r][c] = v


# for ix in range(100):
#     LR = itertools.cycle(lr.strip())
#     for p in RP:
#         rot(*p)


def getPermutation():


def permutationMultiply(P, Q):
    C = {}
    for k in P:
        C[k] = P[Q[k]]
    return C


def permutationPower(P, N):
    if N == 1:
        return P
    if N % 2 == 0:
        return permutationPower(permutationMultiply(P, P), N//2)
    return permutationMultiply(P, permutationPower(P, N-1))


P = getPermutation()
N = 1048576000


def applyPermutation(P):
    g = [['' for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            rr, cc = P[(r, c)]
            g[r][c] = G[rr][cc]
    return g


print('\n'.join(''.join(line) for line in G))
