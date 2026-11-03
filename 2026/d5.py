DX = (
    (1, 0),
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
)
DDX = (
    (-2, -1),
    (-2, 0),
    (-2, 1),
    (-1, -2),
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (-1, 2),
    (0, -2),
    (0, -1),
    (0, 1),
    (0, 2),
    (1, -2),
    (1, -1),
    (1, 0),
    (1, 1),
    (1, 2),
    (2, -1),
    (2, 0),
    (2, 1),
)


def get_input(part):
    with open(f"5-{part}.in") as f:
        G = f.read().splitlines()
    return (
        {(r, c) for r, row in enumerate(G)
         for c, val in enumerate(row) if val == "1"},
        len(G),
        len(G[0]),
    )


def get_land(G, R, C):
    LAND = {(R // 2, C // 2)}
    changes = LAND.copy()
    seen = set()
    while changes:
        changes = set()
        for pos in LAND:
            if pos in seen:
                continue
            seen.add(pos)
            r, c = pos
            if all((r + dr, c + dc) in LAND for dr, dc in DX):
                seen.add(pos)
            for dr, dc in DX:
                np = rr, cc = r + dr, c + dc
                if np in changes:
                    continue
                if (
                    0 <= rr < R
                    and 0 <= cc < C
                    and sum(
                        pp in G or pp in LAND
                        for pp in ((rr + dr, cc + dc) for dr, dc in DX)
                    )
                    >= 5
                ):
                    changes.add(np)
        LAND.update(changes)
    return LAND


def get_sand(LAND):
    def is_sand(pos):
        r, c = pos
        if any(pp not in LAND for pp in ((r + dr, c + dc) for dr, dc in DX)):
            return True

    SAND = {p for p in LAND if is_sand(p)}
    changes = SAND.copy()
    seen = set()
    while changes:
        changes = set()
        for pos in SAND:
            if pos in seen:
                continue
            seen.add(pos)
            r, c = pos
            for dr, dc in DX:
                np = rr, cc = r + dr, c + dc
                if (
                    np in LAND
                    and sum(
                        pp in SAND or pp not in LAND
                        for pp in ((rr + dr, cc + dc) for dr, dc in DX)
                    )
                    >= 5
                ):
                    changes.add(np)
        SAND.update(changes)
    return SAND


def get_tree(R, C, LAND, SAND):
    def is_tree(pos, X):
        r, c = pos
        return all(p in X for p in ((r + dr, c + dc) for dr, dc in DDX))

    TREE = set()
    for _ in range(2):
        X = LAND - (SAND | TREE)
        changes = {p for p in LAND if is_tree(p, X)}
        TREE.update(changes)
        org = TREE.copy()
        n = 0
        while changes:
            seen = SAND | {(r + dr, c + dc) for r, c in SAND for dr, dc in DX}
            n += 1
            if n == 2:
                break
            changes = set()
            for pos in org | {(r + dr, c + dc) for r, c in org for dr, dc in DX}:
                r, c = pos
                if 2 <= r < R - 2 and 2 <= c < C - 2:
                    if pos in seen or pos in TREE:
                        continue
                    seen.add(pos)
                    if any((r + dr, c + dc) in SAND for dr, dc in DX):
                        continue
                    if sum((r + dr, c + dc) in TREE for dr, dc in DX) >= 4:
                        changes.add(pos)
            TREE.update(changes)
    return TREE


def solve(part):
    G, R, C = get_input(part)
    land = get_land(G, R, C)
    if part == 1:
        return len(land)
    sand = get_sand(land)
    if part == 2:
        return len(sand)
    tree = get_tree(R, C, land, sand)
    return len(tree)


print("A", solve(1))
print("B", solve(2))
print("C", solve(3))
