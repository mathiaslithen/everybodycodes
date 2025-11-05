import math

D = (10, 10)
res = (0, 0)
A = (163, 58)


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


for _ in range(3):
    res = mul(res, res)
    res = div(res, D)
    res = add(res, A)

print(f'[{res[0]},{res[1]}]')
