import sys
from heapq import heappop, heappush

with open(sys.argv[1]) as f:
    g = f.read().splitlines()
R, C = len(g), len(g[0])
DD = {
    0: (0, 2, 3),
    1: (1, 2, 3),
    2: (2, 0, 1),
    3: (3, 0, 1),
    None: (0, 1, 2, 3),
}
DX = [(1, 0), (-1, 0), (0, 1), (0, -1)]
DA = {'.': -1, '-': -2, '+': 1, 'S': -1}
ALT = 1000
D = {}
S = [0]*(R*C)
COURSE = {}
for r, row in enumerate(g):
    for c, val in enumerate(row):
        if val == 'S':
            start = (r, c)
        elif val == '#':
            S[r*C+c] = 1
            continue
        if val not in ('-+#.'):
            COURSE[val] = (r, c)
        if val in D:
            D[(r, c)] = DA[val]
        else:
            D[(r, c)] = -1
CC = list(sorted(COURSE.keys()))
print(COURSE, CC)


def mand(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


seen = set()
Q = [(mand(start, COURSE['A']), 0, 'A', ALT, start, None, 0)]
A = 0
while Q:
    # dist, tot, dst, alt, pos, d, minutes = Q.pop(0)

    dist, tot, dst, alt, pos, d, minutes = heappop(Q)

    if pos == COURSE[dst]:
        print(dst)
        if dst == 'S' and alt >= 1000:
            A = min(A, tot)
            continue
        ix = CC.index(dst)+1
        # dst = COURSE[CC[ix]]
        nd = mand(pos, COURSE[CC[ix]])
        Q = [(nd, tot, dst, alt, pos, d, minutes)]
        # Q.append((nd, tot, dst, alt, pos, d, minutes))
        continue

    tot += 1
    minutes += 1
    r, c = pos

    for dx in DD[d]:
        dr, dc = DX[dx]
        np = rr, cc = r+dr, c+dc

        if not (0 <= rr < R and 0 <= cc < C):
            continue
        if S[rr*C+cc]:
            continue

        new_alt = alt + D[(np)]

        if alt <= 0:
            continue

        key = (dst, new_alt, np, dx)
        if key in seen:
            continue
        seen.add(key)

        nd = mand(np, COURSE[dst])

        heappush(Q, (nd, tot, dst, new_alt, np, dx, minutes))
        # Q.append((nd, tot, dst, new_alt, np, dx, minutes))

print(A)
