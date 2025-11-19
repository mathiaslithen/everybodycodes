DX = ((1, 0), (-1, 0), (0, 1), (0, -1))


def get_input(part):
    with open(f'12-{part}.in') as f:
        G = [list(map(int, list(line))) for line in f.read().splitlines()]
    return G, len(G), len(G[0])


def run(part):
    G, R, C = get_input(part)
    if part == 1:
        return len(bfs([(0, 0)], G, R, C))
    if part == 2:
        return len(bfs([(0, 0), (R-1, C-1)], G, R, C))
    ignore = set()
    for _ in range(3):
        best = {}
        for r in range(R):
            for c in range(C):
                if (r, c) in ignore:
                    continue
                x = bfs([(r, c)], G, R, C, ignore=ignore)
                if len(x) > len(best):
                    best = x
        ignore |= best
    return len(ignore)


def bfs(q, G, R, C, ignore=set()):
    seen = set(q)
    while q:
        r, c = q.pop(0)
        v = G[r][c]
        for dr, dc in DX:
            np = rr, cc = r+dr, c+dc
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] <= v and np not in ignore:
                if np in seen:
                    continue
                seen.add(np)
                q.append(np)
    return seen


print('A', run(1))
print('B', run(2))
print('C', run(3))
