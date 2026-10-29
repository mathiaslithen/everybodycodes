def get_input(part):
    with open(f"3-{part}.in") as f:
        yield from (x.split('-')[-1].split() for x in f.read().splitlines())


def adder(x, y):
    return sum(
        int(a) * (int(b) ** ix)
        for ix, (b, a) in enumerate(
            zip(reversed(x * (len(y) // len(x) + 1)), reversed(y))
        )
    )


def is_valid(s, x, y):
    return not any(s == adder(x, str(y)) for y in range(int(y)))


def solve(part):
    return sum(
        s if part in (1, 2) or is_valid(s, *x) else 0
        for (x, s) in ((x, adder(*x)) for x in get_input(part))
    )


print("A", solve(1))
print("B", solve(2))
print("C", solve(3))
