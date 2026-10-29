LR = {'L': -1, 'R': 1}
LL = {-1: 'L', 1: 'R'}


def get_input(part):
    with open(f'{part}.in') as f:
        G, inst = f.read().split('\n\n')
    G = [[(0 if x == '.' else 1) for x in row] for row in G.splitlines()]
    inst = [[LR[x] for x in row] for row in inst.splitlines()]
    return G, inst


def run(part):
    G, inst = get_input(part)
    R, C = len(G), len(G[0])
    ans = []
    for line in inst:
        s = 0
        for toss_slot, slot_ix in zip(range(1, sum(G[0])+1), range(0, 100, 2)):
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
                        s += max(final_slot*2-toss_slot, 0)
                        break
                    pos = rr, c
        ans.append(s)
    return ans


print('A', run(1))
print('B', run(2))
