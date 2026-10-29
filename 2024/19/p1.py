import itertools
import sys

fn = sys.argv[1]
N = int(sys.argv[2]) if len(sys.argv) > 2 else 1
with open(fn) as f:
    lr, grid = f.read().split('\n\n')
    G = [list(line) for line in grid.splitlines()]
R, C = len(G), len(G[0])
DX = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
RP = [
    (r, c)
    for r in range(R)
    for c in range(C)
    if r > 0 and r < R-1 and c > 0 and c < C-1
]
LL = (1, 2, 4, 0, 7, 3, 5, 6)
RR = (3, 0, 1, 5, 2, 6, 7, 4)


def rot(r, c):
    P = [(r+dr, c+dc) for dr, dc in DX]
    d = [G[r][c] for r, c in P]
    d = [d[i] for i in (LL if next(LR) == 'L' else RR)]
    for (r, c), v in zip(P, d):
        G[r][c] = v


for _ in range(N):
    LR = itertools.cycle(lr.strip())
    for p in RP:
        rot(*p)

print('\n'.join(''.join(line) for line in G))
