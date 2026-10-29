import itertools


def get_input(part):
    with open(f'8-{part}.in') as f:
        x = tuple(map(int, f.read().strip().split(',')))
        return tuple(zip(x, x[1:]))


def intersect(a, b, x, y):
    a, b, x, y = min(a, b), max(a, b), min(x, y), max(x, y)
    if (
        (a > x and a < y and b > y)
        or
        (a < x and b > x and (y > b or y < a))
    ):
        return 1
    return 0


def run(part):
    G = get_input(part)
    if part == 1:
        return sum(abs(a-b) == 16 for a, b in G)
    if part == 2:
        return sum(intersect(*a, *b) for ix, a in enumerate(G) for b in G[:ix])
    return max(
        sum(intersect(*a, *b) for b in G)
        for a in itertools.combinations(range(1, 256+1), 2)
    )


print('A', run(1))
print('B', run(2))
print('C', run(3))
