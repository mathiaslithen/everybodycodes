import collections
import itertools


def get_input(part):
    with open(f"4-{part}.in") as f:
        return [
            [int(x.split("=")[-1]) for x in x]
            for x in (x.split() for x in f.read().splitlines())
        ]


def solve(part):
    G = get_input(part)
    if part in (1, 2):
        D = {}
        for i, _, _, t in G:
            if i not in D:
                D[i] = [0, 0]
            D[i][0] -= 1
            D[i][1] += t
        return sum(
            ix * x
            for ix, (_, x) in enumerate(
                sorted(D.values(), key=lambda x: x[-1] if part == 1 else x), start=1
            )
        )
    points = {x[1]: {1: 50, 2: 100, 3: 150} for x in G}
    TOT = collections.defaultdict(int)

    def calc(rows, parts, quest):
        last = None
        count = 0
        for time, _id in rows:
            if last is None:
                last = time
            if time == last:
                count += 1
            elif time > last:
                points[quest][parts] -= count
                count = 1
            TOT[_id] += max(0, points[quest][parts])
            last = time

    for quest, A in itertools.groupby(
        sorted(G, key=lambda x: x[1:]), key=lambda x: x[1]
    ):
        round = {x[0]: 0 for x in G}
        for parts, B in itertools.groupby(A, key=lambda x: x[2]):
            in_round = set()
            for _id, _, _, t in B:
                in_round.add(_id)
                round[_id] += t
            calc(sorted((round[_id], _id) for _id in in_round), parts, quest)

    V = sorted(TOT.values(), reverse=True)
    ans = last = V[0]
    xx = 1
    for ix, val in enumerate(V[1:], start=2):
        if last == val:
            ix = xx
        ans += ix * val
        last, xx = val, ix
    return ans


print("A", solve(1))
print("B", solve(2))
print("C", solve(3))
