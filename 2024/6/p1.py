import collections
import sys

fn = sys.argv[1]
with open(fn) as f:
    G = {
        k: v.split(',')
        for k, v
        in (line.split(':') for line in f.read().splitlines())
    }
    print(G)

ALL = []

def dfs(node, fruit=''):
    if node == "@":
        ALL.append(fruit+'@')
        return
    if node in G:
        for n in G[node]:
            if node in ('BUG', 'ANT'):
                continue
            dfs(n, fruit+node[0])


dfs('RR')
ALL.sort(key=len)
print(ALL)
print([len(x) for x in ALL])
LEN = next(k for k,v in collections.Counter([len(x) for x in ALL]).items()if v==1)
print(next(x for x in ALL if len(x)==LEN))
