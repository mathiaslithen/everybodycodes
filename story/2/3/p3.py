import collections
import re

DX = ((1, 0), (-1, 0), (0, 1), (0, -1), (0, 0))
with open('3.in') as f:
    dices, grid = f.read().split('\n\n')
G = grid.splitlines()
R, C = len(G), len(G[0])
DICE = [
    [sides, len(sides), int(seed), int(seed), 0, 1]
    for _, *sides, seed
    in (re.findall(r'\d+', line) for line in dices.splitlines())
]
D = collections.defaultdict(set)
for r, row in enumerate(G):
    for c, val in enumerate(row):
        D[val].add((r, c))


def roll(dice):
    sides, side_len, seed, pulse, last_roll, roll_number = dice
    spin = roll_number * pulse
    pulse += spin
    pulse %= seed
    pulse += 1 + roll_number + seed
    roll = (last_roll + spin) % side_len
    dice[-3] = pulse
    dice[-2] = roll
    dice[-1] += 1
    return sides[roll]


def explore(dice):
    local = set()
    v = roll(dice)
    current = set(D[v])
    while current:
        local |= current
        v = roll(dice)
        current = {
            p for p
            in ((r+dr, c+dc) for r, c in current for dr, dc in DX)
            if p in D[v]
        }
    return local


ALL_POS = set.union(*(explore(dice) for dice in DICE))
print('ans:', len(ALL_POS))
