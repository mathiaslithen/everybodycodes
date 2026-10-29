import heapq
import sys

with open(sys.argv[1]) as f:
    P = [
        (r, c)
        for r, row in enumerate(f.read().splitlines())
        for c, val in enumerate(row)
        if val == '*'
    ]


def dist(a, b):
    return (abs(a[0]-b[0])+abs(a[1]-b[1]))


def mst(P):
    seen = set()
    tot = 0
    q = [(0, P[0])]
    while q:
        d, p = heapq.heappop(q)
        if p in seen:
            continue
        tot += d
        seen.add(p)
        for n in P:
            if n not in seen:
                heapq.heappush(q, (dist(n, p), n))
        print(seen, q)
    return tot+len(seen)


print(mst(P))
