#!/usr/bin/pypy3
import collections
import sys

with open(sys.argv[1]) as f:
    G = {
        k: v.split(',')
        for k, v
        in (line.split(':') for line in f.read().splitlines())
    }

D = collections.defaultdict(int)
D['Z'] = 1

for _ in range(10):
    tmp = collections.defaultdict(int)
    for k, v in D.items():
        for x in G[k]:
            tmp[x] += v
    D = tmp

print(sum(D.values()))
