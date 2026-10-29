#!/usr/bin/pypy3
import collections
import sys

with open(sys.argv[1]) as f:
    G = {k: v.split(',')
         for k, v
         in (line.split(':') for line in f.read().splitlines())}


S = []
for key in G:
    D = collections.defaultdict(int)
    D[key] = 1
    for _ in range(20):
        tmp = collections.defaultdict(int)
        for k, v in D.items():
            for x in G[k]:
                tmp[x] += v
        D = tmp
    S.append(sum(D.values()))

print(max(S) - min(S))
