import itertools
import sys

fn = sys.argv[1]
with open(fn)as f:
    g = [
        (c, itertools.cycle(line.split(',')))
        for c, line
        in (line.split(':') for line in f.read().splitlines())
    ]
ans = []
for c, it in g:
    x = 0
    s = 10
    for _ in range(10):
        match next(it):
            case '+':
                s += 1
            case '-':
                s -= 1
        x += s
    ans.append((x,c))
print(''.join(x[1] for x in sorted(ans, reverse=True)))
