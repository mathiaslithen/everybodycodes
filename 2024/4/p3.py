import re

with open('3.in') as f:
    nums = list(sorted(map(int, re.findall(r'\d+', f.read()))))
x = nums[len(nums)//2]
d = len(nums)//2
nums = nums[:d] + nums[d+1:]
s = sum(abs(n-x) for n in nums)
print(s)
