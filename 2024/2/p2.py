with open('2.in')as f:
    words, lines = f.read().split('\n\n')
    words = words.strip().split(':')[1].split(',')
    lines = lines.splitlines()


def occ(string, sub, r=False):
    print('string', string)
    o = 0
    l_sub = len(sub)
    start = string.find(sub, o)
    if start < 0:
        return
    while start >= 0:
        for i in range(l_sub):
            x = start+i
            if r:
                print(f'{start=},{i=}, {x=}, {l_sub-x=}')
                xx = x
                x = l_sub-x
                print(f'{r=}', x, xx)
            yield x
        o += l_sub
        start = string.find(sub, o)


# ans = 0
# for line in lines:
#     print(line)
#     for w in words:
#         x = set(occ(line, w))
#         y = set(occ(line[::-1], w, r=1))
#         print(x)
#         print(y)
#         ans += len(x | y)

# print(ans)


def f(string, sub):
    _s = string
    s = set()
    ix = 0
    start = string.find(sub, ix)
    while start >= 0:
        for i in range(len(sub)):
            s.add(start+i)
        ix += 1
        start = string.find(sub, ix)
    string = string[::-1]
    ix = 0
    start = string.find(sub, ix)
    while start >= 0:
        for i in range(len(sub)):
            s.add(len(string)-1-start-i)
        ix += 1
        start = string.find(sub, ix)
    return s


ans = 0
for line in lines:
    s = set()
    for w in words:
        s |= f(line, w)
    ans += len(s)
print(ans)
