import re

reg = re.compile(r"ISO2?\-(\d+)\s(\d+)")


def get_input(fn):
    with open(fn) as f:
        return f.read().splitlines()


def adder(x, y):
    while len(x) < len(y):
        x += x
    return sum(
        int(a) * (int(b) ** ix)
        for ix, (b, a) in enumerate(zip(reversed(x), reversed(y)))
    )


def is_valid(s, x, y):
    return not any(s == adder(x, str(y)) for y in range(int(y)))


def part1():
    ans = 0
    for row in get_input("3-1.in"):
        x, y = reg.match(row).groups()
        ans += adder(x, y)
    print("A", ans)


def part2():
    ans = 0
    for row in get_input("3-2.in"):
        x, y = reg.match(row).groups()
        ans += adder(x, y)
    print("B", ans)


def part3():
    ans = 0
    for row in get_input("3-3.in"):
        x, y = reg.match(row).groups()
        s = adder(x, y)
        if is_valid(s, x, y):
            ans += s
    print("C", ans)


part1()
part2()
part3()
