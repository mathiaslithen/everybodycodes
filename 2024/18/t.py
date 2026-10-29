import sys

with open(sys.argv[1]) as f:
    G = f.read().splitlines()
R, C = len(G), len(G[0])
DX = ((1, 0), (-1, 0), (0, 1), (0, -1))
S = [0]*(R*C)
starta = (1, 0)
startb = (R-2, C-1)
P = set()

for r, row in enumerate(G):
    for c, val in enumerate(row):
        if val == '#':
            S[r*C+c] = 1
        elif val == 'P':
            P.add((r, c))


def f(r, c):
    s = 0
    for rr, cc in X:
        s += abs(r-rr)+abs(c-cc)
    return s


X = [(r, c) for r in range(R) for c in range(C) if G[r][c] == '.']
X = [(f(r, c), (r, c)) for r, c in X]
X.sort()
print(X[0],X[-1])
exit()

def f(start, S, P):
    S = list(S)
    P = set(P)
    Q = [(0, start)]
    TT = 0
    while Q:
        dist, (r, c) = Q.pop(0)
        dist += 1
        if TT > best:
            continue
        for dr, dc in DX:
            np = rr, cc = r+dr, c+dc
            if 0 <= rr < R and 0 <= cc < C and not S[rr*C+cc]:
                if np in P:
                    TT += dist
                P.discard(np)
                if not P:
                    return TT
                S[rr*C+cc] = 1
                Q.append((dist, np))
    return 10**6


best = 10**6
for p in X:
    v = f(p[1], tuple(S), tuple(P))
    if v < best:
        print(v)
        best = v
print(best)

X = [
    f((r, c), tuple(S), tuple(P))
    for r in range(R)
    for c in range(C)
    if not S[r*C+c]
]
print(X)
print(min(X))

print(best)
