def get_input(part):
    with open(f'7-{part}.in') as f:
        W, inst = f.read().split('\n\n')
    D = {
        k: v.split(',')
        for k, _, v
        in (line.split() for line in inst.splitlines())
    }
    return W.split(','), D


def check(w, D):
    for a, b in zip(w, w[1:]):
        if b not in D[a]:
            return False
    return True


def part3(w, D):
    local = set()
    org = len(w)
    ignore = set()
    q = [w]
    while q:
        w = q.pop()
        if len(w) > 11:
            continue
        if ignore and any(x[org:].startswith(w[org:]) for x in ignore):
            continue
        last = w[-1]
        ap = False
        if last in D:
            for ch in D[last]:
                v = w+ch
                if 7 <= len(v) <= 11:
                    local.add(v)
                ap = True
                q.append(v)
        if not ap:
            ignore.add(w)
    return local


def run(part):
    W, D = get_input(part)
    ans = 0
    s = set()
    for ix, w in enumerate(W, start=1):
        if check(w, D):
            if part == 1:
                return w
            if part == 2:
                ans += ix
            if part == 3:
                s |= part3(w, D)
    if part == 3:
        ans = len(s)
    return ans


print('A', run(1))
print('B', run(2))
print('C', run(3))
