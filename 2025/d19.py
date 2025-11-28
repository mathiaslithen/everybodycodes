import bisect
import collections
from heapq import heappop, heappush


def get_input(part):
    with open(f'19-{part}.in') as f:
        return [tuple(map(int, line.split(','))) for line in f.read().splitlines()]


def run(part):
    G = get_input(part)
    W = collections.defaultdict(list)
    C = []
    for c, r1, r2 in G:
        C.append(c)
        W[c].append(range(r1, r1+r2))
    goal_c = G[-1][0]
    D = {}
    q = [(0, 0, (0, 0))]
    while q:
        _, flaps, pos = heappop(q)
        r, c = pos
        if c == goal_c and any(r in ran for ran in W[goal_c]):
            return flaps
        col = C[bisect.bisect_right(C, c)]
        min_height = min(ran[0] for ran in W[col])+1
        delta = col-c
        if min_height > r+delta:
            continue
        skip_dive = r < (min_height+delta-1)
        for (dr, dc), f in ((1, 1), 1), ((-1, 1), 0):
            if skip_dive and not f:
                continue
            np = rr, cc = r+dr, c+dc
            if rr <= 0:
                continue
            if cc in W and not any(rr in ran for ran in W[cc]):
                continue
            ff = flaps+f
            if np in D and D[np] <= ff:
                continue
            D[np] = ff
            heappush(q, (goal_c-cc, ff, np))


print('A', run(1))
print('B', run(2))
print('C', run(3))  # ~30sec
