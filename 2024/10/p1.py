import sys

with open(sys.argv[1])as f:
    g = f.read().splitlines()
R, C = len(g), len(g[0])


def f(r, c):
    if g[r][c] != '.':
        return ''
    rr = set(x for x in g[r] if x != '.')
    cc = set(g[x][c] for x in range(R) if g[x][c] != '.')
    return (rr & cc).pop()


ans = ''.join(f(r, c) for r in range(R) for c in range(C))
print(ans)


def score(s):
    return sum(ix * (ord(c)-64) for ix, c in enumerate(s, start=1))


print(score(ans))

for line in g:
    print(''.join(line))
