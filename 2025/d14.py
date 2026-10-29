import sys

with open(sys.argv[1]) as f:
    G = f.read().splitlines()
    R, C = len(G), len(G[0])
DX = ((1, 0), (0, 1), (-1, 0), (0, -1))
A = [
    1 if val == '#' else 0
    for r, row in enumerate(G)
    for c, val in enumerate(row)
]
LA = len(A)

ans = 0
for _ in range(1):
    local = []
    for ix, val in enumerate(A):
        sr, sc = divmod(ix, C)
        s = sum(
            A[r*C+c]
            for r, c
            in ((sr+dr, sc+dc) for dr, dc in DX)
            if 0 <= r < R and 0 <= c < C
        ) % 2
        local.append(int(val == s))
    ans += sum(local)
    A = local
print(ans)
