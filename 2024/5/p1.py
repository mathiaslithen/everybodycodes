import itertools

with open('1.in') as f:
    g = [list(map(int, list(line)))for line in f.read().splitlines()]
C = len(g[0])

def t(li):
    return list(map(list, itertools.zip_longest(*li, fillvalue=None)))


for n in range(10):
    g = t(g)
    row = g[n%C]
    x = row[0]
    row = row[1:]
    row.append(None)
    g[(n+1)%C].insert(x-1, x)
    g[n%C] = row
    g = t(g)
    print(f'{n+1}: {g[0]}')
