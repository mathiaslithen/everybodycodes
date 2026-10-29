def get_input(part):
    with open(f'11-{part}.in') as f:
        return {
            k: v.split(',')
            for k, v
            in (line.split(':') for line in f.read().splitlines())
        }


def run(start, n, G):
    D = {}
    D[start] = 1
    for _ in range(n):
        tmp = {}
        for k, v in D.items():
            for x in G[k]:
                tmp[x] = tmp.get(x, 0)+v
        D = tmp
    return sum(D.values())


print('A', run('A', 4, get_input(1)))
print('B', run('Z', 10, get_input(2)))

G = get_input(3)
S = sorted(run(start, 20, G) for start in G)
print('C', S[-1]-S[0])
