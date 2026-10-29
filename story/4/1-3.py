def count(row):
    seen = set()
    x = 0
    for n in list(map(int, row.split(","))):
        t = x - n
        if t > 0 and t not in seen and not any(a in seen for a in range(t, x)):
            x = t
        else:
            t = x + n
            while True:
                if any(a in seen for a in range(x,t)):
                    t+=1
                else:
                    x=t
                    break
        seen.add(x)
    return x


with open(0) as f:
    print(sum(map(count, f.read().splitlines())))
