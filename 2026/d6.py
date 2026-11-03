def get_input(part):
    with open(f"6-{part}.in") as f:
        return {
            k: v.split(",") for k, v in (x.split(":") for x in f.read().splitlines())
        }


def solve(part):
    G = get_input(part)
    if part == 1:

        def dive(node, seen):
            if node in seen:
                return
            seen.add(node)
            for n in G.get(node, []):
                dive(n, seen)
            return seen

        return len(dive("NULL", set())) - 1
    elif part == 2:

        def dive(node, seen):
            if node in seen:
                return
            seen.add(node)
            for k, v in G.items():
                if node in v:
                    dive(k, seen)

        seen = set()
        for k, v in G.items():
            if "NULL" in v:
                dive(k, seen)
        return len(seen)

    def dive(node, seen, result):
        seen.add(node)
        for n in G.get(node, []):
            if n in seen:
                continue
            seen.add(n)
            if n.startswith("NULL"):
                result.add(n)
            else:
                dive(n, seen, result)
        return result

    return sum(len(dive(node, set(), set())) >= 2 for node in G)


print("A", solve(1))
print("B", solve(2))
print("C", solve(3))
