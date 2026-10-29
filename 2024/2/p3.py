with open('3.in') as f:
    words, lines = f.read().split('\n\n')
words = words.strip().split(':')[1].split(',')
G = lines.splitlines()
R, C = len(G), len(G[0])
DX = ((1, 0), (-1, 0), (0, 1), (0, -1),)


def search(r, c, w, dx):
    if G[r][c] != w[0]:
        return set()
    dr, dc = dx
    s = {(r, c)}
    for ix, val in enumerate(w[1:], start=1):
        rr = (r + (dr * ix))
        cc = (c + (dc * ix)) % C
        if not (0 <= rr < R) or G[rr][cc] != val:
            break
        s.add((rr, cc))
    else:
        return s
    return set()


ans = set.union(
    *(search(r, c, w, dx)
      for r in range(R)
      for c in range(C)
      for dx in DX
      for w in words)
)
print(len(ans))
