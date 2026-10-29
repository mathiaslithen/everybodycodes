def get_input(fn):
    with open(fn) as f:
        words, inst = f.read().split('\n\n')
    inst = [(1 if x[0] == 'R' else -1, int(x[1:]))
            for x in inst.strip().split(',')]
    return words.strip().split(','), inst


def part1():
    words, inst = get_input('1-1.in')
    ix = 0
    wl = len(words)-1
    for d, n in inst:
        ix += d*n
        ix = max(0, ix)
        ix = min(wl, ix)
    print('A', words[ix])


def part2():
    words, inst = get_input('1-2.in')
    wl = len(words)
    ix = sum(d*n for d, n in inst)
    print('B', words[ix % wl])


def part3():
    words, inst = get_input('1-3.in')
    wl = len(words)
    for d, n in inst:
        ix = (d*n) % wl
        words[0], words[ix] = words[ix], words[0]
    print('C', words[0])


print('A', part1())
print('B', part2())
print('C', part3())
