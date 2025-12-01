DX = ((1, 0), (-1, 0), (0, 1), (0, -1))


def get_input(part):
    with open(f'20-{part}.in') as f:
        G = f.read().splitlines()
    R, C = len(G), len(G[0])
    start = stop = None
    for r, row in enumerate(G):
        for c, val in enumerate(row):
            if val == 'S':
                start = (r, c)
            elif val == 'E':
                stop = (r, c)
    return G, R, C, start, stop


def valid_step(pos, np, dr, dc, grid, R, C):
    r, c = pos
    rr, cc = np
    if 0 <= rr < R and 0 <= cc < C:
        if grid[rr][cc] in 'SET':
            if dr == 0 and dc == 0:
                return True
            if dc:
                return True
            if dr == 1 and (c-r) % 2 == 1:
                return True
            if dr == -1 and (c-r) % 2 == 0:
                return True


def part1():
    G, R, C, start, stop = get_input(1)

    def f(p):
        q = [p]
        local = {p}
        pairs = []
        visited = set()
        while q:
            pos = q.pop(0)
            r, c = pos
            local.add(pos)
            for dr, dc in DX:
                np = rr, cc = r+dr, c+dc
                if (pos, np) in visited:
                    continue
                visited.add((pos, np))
                if valid_step(pos, np, dr, dc, G, R, C):
                    q.append(np)
                    pairs.append((pos, np))
        return pairs, local

    ans = 0
    seen = set()
    for r, row in enumerate(G):
        for c, v in enumerate(row):
            if v == 'T':
                p = r, c
                if p in seen:
                    continue
                seen.add(p)
                pairs, points = f(p)
                if pairs:
                    seen |= points
                    ans += len(pairs)
    return ans//2


def part2():
    G, R, C, start, stop = get_input(2)
    q = [(start, [])]
    D = {}
    while q:
        pos, path = q.pop(0)
        if pos == stop:
            break
        r, c = pos
        steps = len(path)+1
        for dr, dc in DX:
            np = rr, cc = r+dr, c+dc
            if valid_step(pos, np, dr, dc, G, R, C):
                if np in D and D[np] <= steps:
                    continue
                D[np] = steps
                q.append((np, path+[np]))
    return len(path)


def part3():
    G, R, C, start, stop = get_input(3)

    def rot(grid):
        g = [['.']*r for r in range(R)]
        dx = ((-1, 0), (0, -1))
        for rr in reversed(range(R)):
            cc = len(''.join(G[rr]).rstrip('.'))-1
            pos = rr, cc
            it = 0
            while True:
                r, c = pos
                if not (0 <= r < R and 0 <= c < C):
                    break
                g[R-1-rr].append(grid[r][c])
                dr, dc = dx[it % 2]
                it += 1
                pos = r+dr, c+dc
        for x in g:
            while len(x) != C:
                x.append('.')
        return g

    GRIDS = [G]
    for _ in range(2):
        GRIDS.append(rot(GRIDS[-1]))

    DX = ((1, 0), (-1, 0), (0, 1), (0, -1), (0, 0))
    q = [(0, start)]
    seen = set()
    while q:
        dist, pos = q.pop(0)
        if pos == stop:
            return dist
        r, c = pos
        dist += 1
        gix = dist % 3
        for dr, dc in DX:
            np = rr, cc = r+dr, c+dc
            if valid_step(pos, np, dr, dc, GRIDS[gix], R, C):
                key = (gix, np)
                if key in seen:
                    continue
                seen.add(key)
                q.append((dist, np))


print('A', part1())
print('B', part2())
print('C', part3())
