import sys

with open(sys.argv[1]) as f:
    words, inst = f.read().split('\n\n')
    words = words.strip().split(',')
    inst = [(1 if x[0] == 'R' else -1, int(x[1:]))
            for x in inst.strip().split(',')]

ix = 0
wl = len(words)-1
for d, n in inst:
    ix += d*n
    ix = max(0, ix)
    ix = min(wl, ix)
print(words[ix])
