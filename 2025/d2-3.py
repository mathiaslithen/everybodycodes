import math

D = (100000, 100000)
A = [-4531, 67892]

points = [
    (x, y)
    for y in range(A[1], A[1]+1001)
    for x in range(A[0], A[0]+1001)
]


def add(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1+x2, y1+y2)


def mul(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1*x2-y1*y2, x1*y2+y1*x2)


def div(a, b):
    x1, y1 = a
    x2, y2 = b
    _, x = math.modf(x1/x2)
    _, y = math.modf(y1/y2)
    return (int(x), int(y))


S = set()

for p in points:
    res = (0, 0)
    for _ in range(100):
        res = mul(res, res)
        res = div(res, D)
        res = add(res, p)
        if not (-1000000 <= res[0] <= 1000000 and -1000000 <= res[1] <= 1000000):
            break
    else:
        S.add(p)

print(len(S))
