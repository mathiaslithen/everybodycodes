import itertools

G = open(0).read().splitlines()
DX = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]
M = itertools.cycle(DX)

for r, row in enumerate(G):
    for c, val in enumerate(row):
        if val == '@':
            start = (r, c)
        elif val == '#':
            stop = (r, c)

pos = (0, 0)
stop = ((stop[0] - start[0]), (stop[1] - start[1]))

fin = {(stop[0]+dr, stop[1]+dc) for (dr, dc) in DX}
print(stop)
print(fin)

seen = {pos}
while True:
    r, c = pos
    dr, dc = next(M)
    np = rr, cc = r+dr, c+dc
    if fin.issubset(seen):
        print(len(seen))
        break
    if np in seen or np == stop:
        continue
    pos = np
    seen.add(pos)
    print(pos)
