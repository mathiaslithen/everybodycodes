import collections


def get_input(part):
    with open(f"7-{part}.in") as f:
        return {
            int(a): (int(b), tuple(map(int, c.split(","))))
            for (a, b, c) in (
                (y.split("=")[-1] for y in x)
                for x in (x.split(", ") for x in f.read().splitlines())
            )
        }


def solve(part):
    G = get_input(part)
    ans = 0
    ids = {i for i in G}
    starts = G if part == 3 else [
        max(list(G.items()), key=lambda x: len(x[1][-1]))[0]]
    for start in starts:
        tot = collections.defaultdict(int)
        for i, (energy, _) in G.items():
            tot[i] += energy
        impulse = {1: 5, 2: 10, 3: 10}[part]
        exp = 1000000
        dead = set()
        Q = [(start, {impulse: 1})]
        while Q:
            nxt = {i: collections.defaultdict(int) for i in ids}
            dies = set()
            for pos, impulses in Q:
                if pos in dead:
                    continue
                for imp, mul in impulses.items():
                    tot[pos] += imp * mul
                    if part == 3 and tot[pos] >= exp:
                        dies.add(pos)
                    imp -= 1
                    if imp:
                        for n in G[pos][1]:
                            nxt[n][imp] += mul
            for pos in dies:
                for n in G[pos][1]:
                    nxt[n][10] += 1
            dead.update(dies)
            Q = [(k, v) for k, v in nxt.items() if v]
        ans = max(ans, sum(v for k, v in tot.items() if k not in dead))
    return ans


print("A", solve(1))
print("B", solve(2))
print("C", solve(3))
