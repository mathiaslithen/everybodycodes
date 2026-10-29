import re

with open('1.in') as f:
    nums = list(sorted(map(int, re.findall(r'\d+', f.read()))))
s = sum(n-nums[0] for n in nums[1:])
print(s)
