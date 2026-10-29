import collections
import re
import sys
import networkx as nx
with open(sys.argv[1]) as f:
    X = f.read().split('\n\n\n')
    G = X[0].split('\n\n')
    activations = [list(map(int, line.split())) for line in X[1].splitlines()]

D = {}
F = []
CON = collections.defaultdict(list)

X = nx.DiGraph()
eee = []
for g in G:
    g = g.splitlines()
    plant, thickness = map(int, re.findall(r'-?\d+', g[0]))
    D[plant] = thickness
    for line in g[1:]:
        if 'free' in line:
            F.append((plant, int(line.split()[-1])))
        elif 'Plant' in line:
            to_plant, thick = map(int, re.findall(r'-?\d+', line))
            CON[to_plant].append((plant, thick))
            eee.append((to_plant, plant, thick))
X.add_weighted_edges_from(eee)


def f(act):
    energy = collections.defaultdict(list)
    for plant, e in enumerate(act, start=1):
        energy[plant].append((1, e))
    # for p, t in F:
    #     energy[p].append((t, 1))
    q = [p for p, _ in F]
    seen = set()
    while q:
        plant = q.pop(0)
        if plant in seen:
            continue
        seen.add(plant)
        e = sum((x[0]*x[1]) for x in energy[plant])
        if e < D[plant]:
            continue
        edges = CON.get(plant)
        if not edges:
            continue
        for nxt, thi in edges:
            energy[nxt].append((thi, e))
            q.append(nxt)
    m = max(D)
    res = sum(a*b for a, b in energy[m])
    if res >= D[m]:
        return res
    return 0


print(sum(f(act) for act in activations))
ix = []
for i in range(len(activations[0])):
    if all(x[i]==0 for x in activations):
        ix.append(i)
print('ix',ix)
    
# a = [0]*len(F)
# print(a)
# baseline = f(a)
# print(baseline)
# hmm=[]
# for i in range(len(F)):
#     for j in range(len(F)):
#         b=a[:]
#         b[i]=1
#         b[j]=1
#         res = f(b)
#         if res:
#             print(res)
#             hmm.append(i)
# print(hmm)

