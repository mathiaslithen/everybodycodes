d = 100000+100000j
lim = 1000000


def div(a, b):
    return complex(int(a.real / b.real), int(a.imag / b.imag))


def run(points, n=100, d=d, ret_res=False):
    ans = 0
    for p in points:
        res = 0j
        for _ in range(n):
            res = div(res*res, d) + p
            if any(abs(i) > lim for i in (res.real, res.imag)):
                break
        else:
            ans += 1
    if ret_res:
        return res
    return ans


def part1():
    A = (163, 58)
    points = [complex(*A)]
    res = run(points, n=3, d=10+10j, ret_res=True)
    return f'[{int(res.real)},{int(res.imag)}]'


def part2():
    A = (-4531, 67892)
    points = [
        complex(x, y)
        for y in range(A[1], A[1]+1010, 10)
        for x in range(A[0], A[0]+1010, 10)
    ]
    return run(points)


def part3():
    A = (-4531, 67892)
    points = [
        complex(x, y)
        for y in range(A[1], A[1]+1001)
        for x in range(A[0], A[0]+1001)
    ]
    return run(points)


print('A', part1())
print('B', part2())
print('C', part3())
