def solve(part):
    with open('%d.in' % part) as f:
        G = f.read().splitlines()
    R, C = len(G), len(G[0])
    DX = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if part == 3:
        DX.extend([(1, 1), (-1, -1), (1, -1), (-1, 1)])
    P = {
        (r, c)
        for r in range(R)
        for c in range(C)
        if G[r][c] == '#'
    }
    ans = len(P)
    while P:
        P = {
            (r, c)
            for r, c in P
            if all((r+dr, c+dc) in P for dr, dc in DX)
        }
        ans += len(P)
    print(f'{part}: {ans}')

solve(1)
solve(2)
solve(3)
