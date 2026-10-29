from __future__ import annotations

import collections
import re

reg = re.compile(r'\w+\=\[(\d+),(\w|\!)\]')


class Node:
    rank: int
    value: str
    left: Node
    right: Node

    def __init__(self, rank, value):
        self.id = 0
        self.depth = 0
        self.rank = rank
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f'{self.depth=} {self.rank=} {self.value=}'


def add(tree: list, node):
    if not tree:
        node.depth = 0
        tree.append(node)
        return
    cur = tree[0]
    tree.append(node)
    depth = 1
    while True:
        print(tree)
        if node.rank > cur.rank:
            if cur.right:
                depth += 1
                cur = cur.right
            else:
                node.depth = depth
                cur.right = node
                break
        elif node.rank < cur.rank:
            if cur.left:
                depth += 1
                cur = cur.left
            else:
                node.depth = depth
                cur.left = node
                break


LEFT, RIGHT = [], []
with open('ex2') as f:
    x = reg.findall(f.read())
    for rank, val in x[::2]:
        add(LEFT, Node(int(rank), val))
    for rank, val in x[1::2]:
        add(RIGHT, Node(int(rank), val))
print(LEFT)


seen = set()
D = collections.defaultdict(int)
C = collections.Counter()


def dfs(node):
    if node in seen:
        return
    D[node.depth] += 1
    C[node.depth] += 1
    seen.add(node)
    if node.left and node.left not in seen:
        dfs(node.left)
    if node.right and node.right not in seen:
        dfs(node.right)


dfs(LEFT[0])
dfs(RIGHT[0])
WANT = C.most_common()[0][0]

ANS = []
seen = set()


def dfs(node):
    if node in seen:
        return
    if node.depth == WANT:
        ANS.append(node.value)
        return
    if node.left and node.left not in seen:
        dfs(node.left)
    if node.right and node.right not in seen:
        dfs(node.right)

dfs(LEFT[0])
dfs(RIGHT[0])
print(''.join(ANS))
