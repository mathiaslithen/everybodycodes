import itertools


def get_input(part):
    with open(f'8-{part}.in') as f:
        x = tuple(map(int, f.read().strip().split(',')))
        return tuple(zip(x, x[1:]))


def intersect(a, b, x, y):
    if a == x or a == y or b == x or b == y:
        return 0
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
        ans = 0
        X = []
        for a in G:
            ans += sum(intersect(*a, *b) for b in X)
            X.append(a)
        return ans
    return max(
        sum(intersect(*a, *b) for b in G)
        for a in itertools.combinations(range(1, 256+1), 2)
    )


print('A', run(1))
print('B', run(2))
print('C', run(3))
