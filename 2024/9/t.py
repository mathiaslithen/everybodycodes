import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10**6)
with open(sys.argv[1]) as f:
    G = list(map(int, f.read().splitlines()))

S = {
    1: (30, 25, 24, 20, 16, 15, 10, 5, 3, 1),
    2: (),
    3: (101, 100, 75, 74, 50, 49, 38, 37,
        30, 25, 24, 20, 16, 15, 10, 5, 3, 1),
}

for k in S:
    if k in sys.argv[1]:
        stamps = S[k]
        break


F = [0]
for i in range(1, 10**6):
    best = 1e7
    for s in stamps:
        if i-s >= 0:
            best = min(best, 1+F[i-s])
    F.append(best)


def g(n):
    mid = (n-1)//2
    best = 1e9
    for x in range(mid-50, mid+1):
        y = n-x
        if abs(x-y) <= 100:
            best = min(best, F[x]+F[y])
        else:
            print(x, y, x-y)
    return best


ans = sum(g(n) for n in G)
print(ans)
