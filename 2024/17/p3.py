import collections
import functools
import heapq
import itertools
import operator
import sys

MAX_DIST = 5

with open(sys.argv[1]) as f:
    stars = {
        (r, c)
        for r, row in enumerate(f.read().splitlines())
        for c, val in enumerate(row)
        if val == '*'
    }


def dist(a, b):
    return (abs(a[0]-b[0])+abs(a[1]-b[1]))


adj = collections.defaultdict(list)
for p1, p2 in itertools.combinations(stars, 2):
    d = dist(p1, p2)
    if d <= MAX_DIST:
        adj[p1].append((d, p2))
        adj[p2].append((d, p1))


def mst(stars):
    seen = set()
    tot = 0
    q = [(0, stars.pop())]
    while q:
        d, p = heapq.heappop(q)
        if p in seen:
            continue
        tot += d
        seen.add(p)
        for nd, n in adj[p]:
            if n not in seen:
                heapq.heappush(q, (nd, n))
    stars -= seen
    return tot+len(seen)


ans = [0]*3
while stars:
    heapq.heappushpop(ans, mst(stars))
s = functools.reduce(operator.mul, ans)
print(s)
