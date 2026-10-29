import re
from functools import cmp_to_key, partial

reg = re.compile(r"(\d+)(<|>)(\d+)")


def get_input(part):
    with open(f"2-{part}.in") as f:
        yield from (x.split() for x in f.read().splitlines())


def get_order(row):
    order = set()
    n = set()
    for x in row:
        a, op, b = reg.match(x).groups()
        n.update((a, b))
        order.add((a, b) if op == "<" else (b, a))
    return order, list(n)


def cmp(a, b, order):
    if (a, b) in order:
        return 1
    elif (b, a) in order:
        return -1
    else:
        for x in order:
            if x[0] == a:
                for y in order:
                    if y[0] == x[1] and y[1] == b:
                        return 1
    return -1


def solve(part):
    return sum(
        int("".join(sorted(n, key=cmp_to_key(partial(cmp, order=order)))))
        for (order, n) in (get_order(x) for x in get_input(part))
    )


print("A", solve(1))
print("B", solve(2))
print("C", solve(3))
