import collections
import sys

with open(sys.argv[1]) as f:
    G = list(map(int, f.read().strip().split(',')))

print('A', sum(set(G)))
print('B', sum(list(sorted(set(G)))[:20]))


c = collections.Counter(G)
ans = 0
while any(c.values()):
    s = set(i for i in c if c[i] > 0)
    for n in s:
        c[n] -= 1
    ans += 1
print('C', ans)
