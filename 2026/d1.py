import bisect

N = 10**7
def read_input(fn):
    with open(fn) as f:
        return list(map(int, f.read().split(",")))


def part1():
    X = [x**2 for x in range(N)]
    return sum(X[bisect.bisect_left(X, n)] - n for n in read_input('1-1.in'))


def part2():
    X = [2 * x + 2 * (x - 2) for x in range(3, N)]
    return sum(X[bisect.bisect_left(X, n)] - n for n in read_input('1-2.in'))


def part3():
    X = [x**2 - 1 for x in range(3, N) if x % 2 == 1]
    return sum(X[bisect.bisect_left(X, n)] - n for n in read_input('1-3.in'))


print("A", part1())
print("B", part2())
print("C", part3())
