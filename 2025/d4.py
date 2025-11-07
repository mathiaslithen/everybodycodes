def get_input(part):
    with open(f'4-{part}.in') as f:
        if part in (1, 2):
            return list(map(int, f.read().splitlines()))
        N = []
        for line in f:
            N.append(tuple(map(int, line.split('|'))))
        return N


n = get_input(1)
x = 2025
print('A', int(x/(n[-1]/n[0])))

n = get_input(2)
x = 10000000000000
print('B', int(1+x*n[-1]/n[0]))

n = get_input(3)
x = 100
ratio = 1
for a, b in zip(n, n[1:]):
    ratio *= a[-1]/b[0]
print('C', int(x*ratio))
