import collections
import itertools


def get_input(part):
    with open(f'9-{part}.in') as f:
        return {
            int(_id): set(enumerate(dna))
            for _id, dna
            in (line.strip().split(':') for line in f.readlines())
        }


def union_find(part):
    D = {k: ''.join(s for _, s in v) for k, v in get_input(part).items()}

    parent = {x: x for x in D}
    size = {x: 1 for x in D}

    def related(child, p1, p2):
        return all(ch in (D[p1][ix], D[p2][ix]) for ix, ch in enumerate(D[child]))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        xx, yy = find(x), find(y)
        if xx == yy:
            return
        if size[xx] < size[yy]:
            xx, yy = yy, xx
        parent[yy] = xx
        size[xx] += size[yy]

    for a, b, c in itertools.combinations(D, 3):
        if related(a, b, c) or related(b, a, c) or related(c, a, b):
            union(a, b)
            union(a, c)


    g = collections.defaultdict(list)
    for n in D:
        g[find(n)].append(n)

    print(g)

    return sum(max(g.values(), key=len))


def run(part):
    if part == 3:
        return union_find(part)
    D = get_input(part)
    F = []
    parents = set()
    chpa = set()
    ans = 0
    for c in D:
        for p in itertools.combinations(D, 2):
            if c in p:
                continue
            x, y = p
            if (x, y) in chpa or (y, x) in chpa:
                continue
            if (c, x) in parents or (x, c) in parents or (c, y) in parents or (y, c) in parents:
                continue
            if D[c]-(D[x] | D[y]):
                continue

            parents.add(p)
            chpa.add((c, x))
            chpa.add((c, y))

            ans += len(D[x] & D[c]) * len(D[y] & D[c])
            if part == 1:
                return ans
            if part == 3:
                g = {c, x, y}
                if not F:
                    F.append(g)
                else:
                    for f in F:
                        if any(x in f for x in g):
                            f |= g
                            break
                    else:
                        F.append(g)
    if part == 2:
        return ans
    for a, b in itertools.combinations(F, 2):
        if a & b:
            a |= b
            b |= a
    F.sort(key=len)
    return sum(F[-1])


# print('A', run(1))
# print('B', run(2))
print('C', run(3))
