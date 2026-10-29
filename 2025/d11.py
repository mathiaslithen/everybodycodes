import math
import re
import sys


def chk(n):
    return sum(ix*i for ix, i in enumerate(n))


with open(sys.argv[1]) as f:
    n = list(map(int, re.findall(r'\d+', f.read())))
m = sum(n)//len(n)

baseline = chk([m for _ in range(len(n))])
cur = chk(n)
print(math.gcd(baseline, cur))
