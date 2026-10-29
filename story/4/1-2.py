def count(row):
    seen = set()
    x = 0
    for n in list(map(int, row.split(","))):
        t = x - n
        if t > 0 and t not in seen:
            x = t
        else:
            t = x + n
            while True:
                if t not in seen:
                    x = t
                    break
                else:
                    t += 1
        seen.add(x)
    return x


with open(0) as f:
    print(sum(map(count, f.read().splitlines())))
