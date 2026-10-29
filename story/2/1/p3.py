import itertools

with open('3.in') as f:
    G, inst = f.read().split('\n\n')
G = G.splitlines()
SLOTS = G[0].count('*')
G = [[(0 if x == '.' else 1) for x in row] for row in G]
inst = [[-1 if x == 'L'else 1 for x in row] for row in inst.splitlines()]
R, C = len(G), len(G[0])


def play(line):
    ans = {}
    for toss_slot, slot_ix in zip(range(1, SLOTS+1), range(0, 100, 2)):
        pos = (-1, slot_ix)
        ix = 0
        while True:
            r, c = pos
            if 0 <= r+1 < R and G[r+1][c] == 1:
                dx = line[ix]
                ix += 1
                cc = c+dx
                if not (0 <= cc < C):
                    cc = c+(dx*-1)
                pos = r+1, cc
            else:
                rr = r+1
                if rr >= R:
                    final_slot = c//2+1
                    ans[toss_slot-1] = max(final_slot*2 - toss_slot, 0)
                    break
                pos = rr, c
    return ans


D = {}
for ix, i in enumerate(inst):
    D[ix] = play(i)
print(D)
mi = 1000000
ma = 0
for x in itertools.combinations(range(10), 6):
    for y in itertools.permutations(x):
        s = 0
        for i, k in enumerate(y):
            s += D[i][k]
        mi = min(s, mi)
for x in itertools.combinations(range(10, 20), 6):
    for y in itertools.permutations(x):
        s = 0
        for i, k in enumerate(y):
            s += D[i][k]
        ma = max(ma, s)
print(mi, ma)
