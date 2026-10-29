R, C = 0, 0
def getPermutation(): pass


def permutationMultiply(P, Q):
    C = {}
    for k in P:
        C[k] = P[Q[k]]
    return C


def permutationPower(P, N):
    if N == 1:
        return P
    if N % 2 == 0:
        return permutationPower(permutationMultiply(P, P), N//2)
    return permutationMultiply(P, permutationPower(P, N-1))


P = getPermutation()
N = 1048576000


def applyPermutation(P):
    g = [['' for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            rr, cc = P[(r, c)]
            g[r][c] = G[rr][cc]
    return g
