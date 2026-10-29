with open('2.in') as f:
    G, inst = f.read().split('\n\n')
G = G.splitlines()
SLOTS = G[0].count('*')
LR = {'L': -1, 'R': 1}
LL = {-1: 'L', 1: 'R'}
G = [[(0 if x == '.' else 1) for x in row] for row in G]
inst = [[LR[x] for x in row] for row in inst.splitlines()]
R, C = len(G), len(G[0])


def play(line):
    ans = []
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
                    ans.append(max(final_slot*2 - toss_slot, 0))
                    break
                pos = rr, c
    return ans


print(2, sum(max(play(x)) for x in inst))
