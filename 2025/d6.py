import bisect
import collections


def get_input(part):
    with open(f'6-{part}.in') as f:
        G = f.read().strip()
    if part == 3:
        G *= 1000
    D = collections.defaultdict(list)
    for ix, ch in enumerate(G):
        D[ch].append(ix)
    return D


def run(part):
    D = get_input(part)
    ans = 0
    for key in D:
        if part == 1 and key != 'a':
            continue
        if key.islower():
            for ix in D[key]:
                k = key.upper()
                if part == 3:
                    a = bisect.bisect_left(D[k], ix-1000)
                    b = bisect.bisect_right(D[k], ix+1000)
                    ans += b-a
                else:
                    ans += sum(1 for i in D[k] if i < ix)
    return ans


print('A', run(1))
print('B', run(2))
print('C', run(3))
