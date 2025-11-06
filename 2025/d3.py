import collections


def get_input(fn):
    with open(fn) as f:
        return list(map(int, f.read().strip().split(',')))


G = get_input('3-1.in')
print('A', sum(set(G)))

G = get_input('3-2.in')
print('B', sum(list(sorted(set(G)))[:20]))

G = get_input('3-3.in')
c = collections.Counter(G)
ans = 0
while any(c.values()):
    s = set(i for i in c if c[i] > 0)
    for n in s:
        c[n] -= 1
    ans += 1
print('C', ans)
