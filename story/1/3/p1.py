import re

reg = re.compile(r'\d+')


def man(s):
    x, y = s
    return 1+abs(x-1)+abs(y-1)


def move(s, n=100):
    x, y = s
    x += n-1
    x %= man(s)
    y = x % man(s)
    x += 1
    return x, y


def score(s):
    x, y = s
    return x + (100 * y)


with open('1.in') as f:
    S = sum(
        x+(100*y)
        for x, y in
        (move(s)
         for s
         in (map(int, reg.findall(line)) for line in f))
        )
print(S)

ans = sum(score(move(s))for s in S)
ans = sum(score(move(s))for s in S)
ans = sum(x+(100*y) for (x, y) in (move(s) for s in S))
print(ans)
ans = 0
for s in S:
    s = move(s)
    ans += score(s)
print(ans)
"""
x=1 y=2
x=2 y=3
x=3 y=4
x=4 y=4

123456789
23456789
3456789
456789
56789
6789
789
89
9
"""
