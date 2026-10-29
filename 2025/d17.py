import collections
import sys
from heapq import heappop, heappush


def get_input(part):
    with open(f'17-{part}.in') as f:
        G = f.read().splitlines()
    return G, len(G), len(G[0])


DX = ((1, 0), (-1, 0), (0, 1), (0, -1))


def parse(G):
    nums = []
    for r, row in enumerate(G):
        for c, v in enumerate(row):
            if v == '@':
                volcano = (r, c)
            elif v == 'S':
                start = (r, c)
            nums.append(int(v) if v.isnumeric() else 0)
    return start, volcano, nums


def get_dest(G, start, volcano):
    dest = collections.defaultdict(set)
    dest[3].add(start)
    for r, row in enumerate(G):
        for c, v in enumerate(row):
            p = (r, c)
            if r == volcano[0] and c < volcano[1]:
                dest[0].add(p)
            elif r == volcano[0] and c > volcano[1]:
                dest[2].add(p)
            elif c == volcano[1] and r > volcano[0]:
                dest[1].add(p)
    return dest


def in_range(p, radius, volcano):
    Yv, Xv = volcano
    Yc, Xc = p
    return (Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc) <= (radius * radius)


def get_lava(radius,volcano, G):
    s = {volcano}
    for r, row in enumerate(G):
        for c, v in enumerate(row):
            p = (r, c)
            if in_range(p, radius):
                s.add(p)
    return s


def go(radius):
    time_limit = (radius+1)*30
    lava = get_lava(radius)
    D = {}
    q = [(0, 0, start)]
    while q:
        duration, dix, pos = heappop(q)
        if pos in (dest[dix]-lava):
            if dix == 3:
                return duration
            dix += 1
        r, c = pos
        for dr, dc in DX:
            np = rr, cc = r+dr, c+dc

            if np in lava or not (0 <= rr < R and 0 <= cc < C):
                continue

            nd = duration+nums[rr*C+cc]
            if nd > time_limit:
                continue

            key = (np, dix)
            if key in D and D[key] <= nd:
                continue
            D[key] = nd

            heappush(q, (nd, dix, np))


for i in range(R//4, R//2):
    if ans := go(i):
        print(i*ans)
        break
