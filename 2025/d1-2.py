import sys

with open(sys.argv[1]) as f:
    words, inst = f.read().split('\n\n')
    words = words.strip().split(',')
    inst = [(1 if x[0] == 'R' else -1, int(x[1:]))
            for x in inst.strip().split(',')]

wl = len(words)
ix = sum(d*n for d, n in inst)
print(words[ix % wl])
