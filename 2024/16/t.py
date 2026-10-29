import collections
import functools
import math
import sys

with open(sys.argv[1]) as f:
    inst, data = f.read().split('\n\n')
inst = list(map(int, inst.strip().split(',')))
data = data.strip().splitlines()
groups = data[0].strip().count(' ') + 1


def make_wheels(data, part=1):
    G = [[] for _ in range(groups)]
    for r in range(len(data)):
        row = data[r]
        for i in range(groups):
            ix = i*3+i
            if x := row[ix:ix+3].strip():
                G[i].append(x)
    return G


def get_line(i, wheels):
    return ' '.join(wheel[i % len(wheel)][::2] for wheel in wheels)


def score(line):
    return sum(v-2 for v in collections.Counter(line.replace(' ', '')).values() if v > 2)


wheels = make_wheels(data, part=2)
N = 202420242024
lcm = math.lcm(*(len(w) for w in wheels))
loops, rem = divmod(N, lcm)
A = B = 0
for i in range(1, lcm+1):
    A += score(get_line(i, wheels))
    if i == rem:
        B = A
print(loops*A+B)
