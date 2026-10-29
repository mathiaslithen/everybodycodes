import sys
from heapq import heappop, heappush
from pprint import pprint as pp

with open(sys.argv[1]) as f:
    G = f.read().splitlines()
R, C = len(G), len(G[0])
DX = ((1, 0), (-1, 0), (0, 1), (0, -1))
S = [0]*(R*C)
start = (0, G[0].index('.'))
herbs = {}
for r, row in enumerate(G):
    for c, val in enumerate(row):
        if val in '#~':
            S[r*C+c] = 1
        elif val not in '.#~':
            herbs[(r, c)] = val
TYPE = {h: ix for ix, h in enumerate(set(herbs.values()))}
# TYPE = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
DONE = 2**len(TYPE)-1
print(TYPE, DONE)
HIX = {pos: ix for ix, pos in enumerate(herbs, start=1)}
HIX[start] = 0
OIX = {ix: pos for pos, ix in HIX.items()}
g = {ix: {} for ix in HIX.values()}

for spos, six in HIX.items():
    for epos, eix in HIX.items():
        if spos == epos or eix in g[six]:
            continue
        seen = S[:]
        seen[spos[0]*C+spos[1]] = 1
        Q = [(0, spos)]
        while Q:
            dist, pos = Q.pop(0)
            if pos == epos:
                g[six][eix] = dist
                g[eix][six] = dist
                break
            dist += 1
            r, c = pos
            for dr, dc in DX:
                np = rr, cc = r + dr, c + dc
                if 0 <= rr < R and 0 <= cc < C and not seen[rr*C+cc]:
                    seen[rr*C+cc] = 1
                    Q.append((dist, np))
pp(g[0])
for x in g[0]:
    print('x', x)

M = 10**10
print('XXX\n', g[0], 'XXX\n')


def dfs(dist, bitmask, node):
    global M
    if bitmask == DONE:
        if dist < M:
            print(dist)
        M = min(M, dist)
        return
    for n, dd in sorted(g[node].items(), key=lambda x: x[1]):
        pos = OIX[n]
        if pos == start:
            continue
        b = 1 << TYPE[herbs[pos]]
        if bitmask & b == 0:
            nd = dist+g[node][n]
            if nd > M:
                continue
            dfs(nd, bitmask | b, n)


# dfs(0, 0, 0)
print(M)


print(herbs)
print('p1', min(g[0].values())*2)
le = len(TYPE)
print(TYPE)
# dist, bm, node
X = 10**10
Q = [(le, 0, 0, 0)]
D = {}
while Q:
    y, dist, bm, node = heappop(Q)
    # dist, bm, node = Q.pop(0)
    if bm == DONE:
        x = dist+g[node][0]
        if x < X:
            X = x
            print(X)
        continue
    if bin(bm).count('1') > int(len(TYPE)/0.67):
        if bm in D and D[bm] < dist:
            continue
        D[bm] = dist
    # for p, ix in HIX.items():
    for ix, _ in sorted(g[node].items(), key=lambda x: x[1]):
        p = OIX[ix]
        if p == start:
            continue
        b = 1 << TYPE[herbs[p]]
        if bm & b == 0:
            d = dist + g[node][ix]
            if d > X:
                continue
            nb = bm | b
            y = le - bin(nb).count('1')
            heappush(Q, (y, d, bm | b, ix))
            # Q.append((d, bm | b, ix))
print(X)
