import re


def get_input(part):
    with open(f'13-{part}.in') as f:
        return list(map(int, re.findall(r'\d+', f.read())))


def part1(part):
    n = get_input(part)
    R = []
    L = []
    for ix, i in enumerate(n):
        if ix % 2 == 0:
            R.append(i)
        else:
            L.append(i)
    x = [1] + R + L[::-1]
    return x[2025 % len(x)]


def part23(part):
    n = get_input(part)
    m = 202520252025 if part == 3 else 20252025
    R = []
    L = []
    for ix, (a, b) in enumerate(zip(n[::2], n[1::2])):
        ra = range(a, b+1)
        if ix % 2 == 0:
            R.extend(list(ra))
        else:
            L.extend(list(ra))
    x = [1] + R + L[::-1]
    return x[m % len(x)]


print('A', part1(1))
print('B', part23(2))
print('C', part23(3))
