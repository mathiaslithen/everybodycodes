import collections


def get_input(fn):
    with open(fn) as f:
        return list(map(int, f.read().strip().split(',')))


G = get_input('3-1.in')
print('A', sum(set(G)))

G = get_input('3-2.in')
print('B', sum(list(sorted(set(G)))[:20]))

G = get_input('3-3.in')
print('C', max(collections.Counter(G).values()))
