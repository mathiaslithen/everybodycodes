import re

FN = 'ex'

print("""
123456789
23456789
3456789
456789
56789
6789
789
89
9
""")

with open(FN) as f:
    S = [
        list(map(int, re.findall(r'\d+', line)))
        for line
        in f.read().splitlines()
    ]

print(S)


def score(s):
    x, y = s
    return (x+1) + (100 * (y+1))


def move(s):
    x, y = s
    x -= 1
    y -= 1
    d = abs(x) + abs(y)
    xx = (x + 100) % d
    yy = d - xx
    print(f'[x={x} y={y}] @ {d} --> {xx},{yy}')
    return score((xx, yy))


ans = sum(move(s) for s in S)
print(ans)
