A = (-4531, 67892)
d = 100000+100000j
lim = 1000000
points = [
    complex(x, y)
    for y in range(A[1], A[1]+1001)
    for x in range(A[0], A[0]+1001)
]


def div(a, b):
    return complex(int(a.real / b.real), int(a.imag / b.imag))


ans = 0
for p in points:
    res = 0j
    for _ in range(100):
        res = div(res*res, d) + p
        if any(abs(i) > lim for i in (res.real, res.imag)):
            break
    else:
        ans += 1
print(ans)
