import itertools,collections


def t(li):
    return list(map(list, itertools.zip_longest(*li, fillvalue=0)))


with open('3.in') as f:
    g = [list(map(int, list(line.split())))for line in f.read().splitlines()]
    C = len(g[0])
    g = t(g)
print(C)
D = collections.defaultdict(int)
# for n in range(10):
n = 0
M=0
while True:
    x = g[n % C].pop(0)
    r = (n+1) % C
    le = len(g[r])
    p = 0
    left = 1
    for _ in range(x):
        if p and p % le == 0 and left:
            left = 0
        else:
            p += 1*(1 if left else -1)
        if p == 0:
            p = 1
            left = 1
    if left:
        p -= 1
    g[r].insert(p, x)
    i = int(''.join(str(x[0]) for x in g))
    M=max(M,i)
    if n%10000==0:
        print(M)
    n+=1



"""
015
124
233

"""
