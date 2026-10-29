import collections
import functools
import heapq
import itertools
import operator
import sys

with open(sys.argv[1]) as f:
    P = {
        (r, c)
        for r, row in enumerate(f.read().splitlines())
        for c, val in enumerate(row)
        if val == '*'
    }


adj = collections.defaultdict(list)
for p1, p2 in itertools.combinations(P, 2):
    if (d := abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])) and d <= 5:
        adj[p1].append((d, p2))
        adj[p2].append((d, p1))


def mst(P):
    seen = set()
    tot = 0
    q = [(0, P.pop())]
    while q:
        d, p = heapq.heappop(q)
        if p in seen:
            continue
        tot += d
        seen.add(p)
        for nd, n in adj[p]:
            if n not in seen:
                heapq.heappush(q, (nd, n))
    P -= seen
    return tot+len(seen)


ans = [0]*3
while P:
    heapq.heappushpop(ans, mst(P))
s = functools.reduce(operator.mul, ans)
print(s)
