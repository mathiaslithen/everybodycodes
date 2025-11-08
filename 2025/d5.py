import re


def get_input(part):
    with open(f'5-{part}.in') as f:
        return [list(map(int, re.findall(r'\-?\d+', line)))
                for line in f.read().splitlines()]


def run(part):
    G = get_input(part)
    qual = []
    C = []
    for sword in G:
        F = [[None, sword[1], None]]
        q = sword[2:]
        while q:
            v = q.pop(0)
            for b in F:
                if v < b[1] and b[0] is None:
                    b[0] = v
                    break
                elif v > b[1] and b[2] is None:
                    b[2] = v
                    break
            else:
                F.append([None, v, None])
        q = int(''.join(str(x[1]) for x in F))
        qual.append(q)
        qq = tuple(int(''.join(str(i) for i in f if i)) for f in F)
        C.append((q, qq, sword[0]))
    if part == 1:
        return qual[0]
    elif part == 2:
        return max(qual)-min(qual)
    else:
        C.sort(reverse=1)
        ans = 0
        for a, b in enumerate(C, start=1):
            ans += a*b[-1]
        return ans


print('A', run(1))
print('B', run(2))
print('C', run(3))
