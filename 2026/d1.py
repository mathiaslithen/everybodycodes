import bisect


def get_input(part):
    with open(f"1-{part}.in") as f:
        yield from (map(int, f.read().split(",")))


def get_cones(part):
    N = 10**4
    if part == 1:
        return [x**2 for x in range(N)]
    elif part == 2:
        return [2 * x + 2 * (x - 2) for x in range(3, N)]
    return [x**2 - 1 for x in range(3, N) if x % 2 == 1]


def solve(part):
    X = get_cones(part)
    return sum(X[bisect.bisect_left(X, n)] - n for n in get_input(part))


print("A", solve(1))
print("B", solve(2))
print("C", solve(3))
