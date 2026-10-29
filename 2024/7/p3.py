import itertools

with open('trackp3') as f:
    g = f.read().splitlines()
R, C = len(g), len(g[0])
DX = ((1, 0), (-1, 0), (0, 1), (0, -1))

T = []
node = ((0, 0), None)
first = True
while True:
    pos, last = node
    r, c = pos
    if first:
        rr, cc = 0, 1
        first = False
        T.append(g[0][1])
        node = ((rr, cc), pos)
    else:
        for dr, dc in DX:
            np = rr, cc = r + dr, c + dc
            if 0 <= rr < R and 0 <= cc < C and g[rr][cc] != ' ' and np != last:
                T.append(g[rr][cc])
                node = (np, pos)
                break
    if T and T[-1] == 'S':
        break
print(T)
print(len(T))


d = ['+', '+', '+', '+', '+', '-', '-', '-', '=', '=', '=']
with open('3.in') as f:
    opp = list(f.read().strip().split(':')[1])
print(opp)


def f(plan):
    it = itertools.cycle(plan)
    score = 0
    s = 10
    for _ in range(11):
        for op in T:
            own = next(it)
            if op in ('=', 'S'):
                op = own
            match op:
                case '+':
                    s += 1
                case '-':
                    s -= 1
            score += s
    return score


ans = 0
baseline = f(opp)
print('baseline', baseline)
for plan in itertools.permutations(d):
    if f(plan) > baseline:
        ans += 1
        print(ans)
print(ans)
