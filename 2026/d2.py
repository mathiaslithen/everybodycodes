import re
from functools import cmp_to_key

reg = re.compile(r"(\d+)(<|>)(\d+)")


def run(fn):
    with open(fn) as f:
        G = f.read().splitlines()
    res = []
    for row in G:
        orders = set()
        n = set()
        for x in row.split():
            a, op, b = reg.match(x).groups()
            n.update((a, b))
            orders.add((a, b) if op == "<" else (b, a))

        def f(a, b):
            if (a, b) in orders:
                return 1
            elif (b, a) in orders:
                return -1
            else:
                for x in orders:
                    if x[0] == a:
                        for y in orders:
                            if y[0] == x[1] and y[1] == b:
                                return 1
            return -1

        res.append(int("".join(sorted(n, key=cmp_to_key(f)))))
    return sum(res)


print("A", run("2-1.in"))
print("B", run("2-2.in"))
print("C", run("2-3.in"))
