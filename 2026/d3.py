import re

reg = re.compile(r"ISO2?\-(\d+)\s(\d+)")


def get_input(fn):
    with open(fn) as f:
        return f.read().splitlines()


def adder(x, y):
    return sum(
        int(a) * (int(b) ** ix)
        for ix, (b, a) in enumerate(zip(reversed(x), reversed(y)))
    )


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
        while len(x) < len(y):
            x += x
        ans += adder(x, y)
    print("B", ans)


def part3():
    ans = 0
    for row in get_input("3-3.in"):
        x, y = reg.match(row).groups()
        while len(x) < len(y):
            x += x
        s = adder(x, y)
        yy = int(y)
        valid = True
        while yy > 0:
            yy -= 1
            if s == adder(x, str(yy)):
                valid = False
                break
        if valid:
            ans += s
    print("C", ans)


part1()
part2()
part3()
