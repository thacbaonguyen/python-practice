def Try(i, current, index):
    if len(current) == b:
        tmp.append(' '.join(current))
        return
    for j in range(index, len(rs)):
        Try(i + 1, current + [rs[j]], j + 1)

a, b = map(int, input().split())
rs = [x for x in input().split()]
rs = sorted(set(rs))
tmp = []
Try(1, [], 0)
print('\n'.join(tmp))


# from itertools import combinations, permutations
#
# a, b = map(int, input().split())
# rs = [x for x in input().split()]
# rs = sorted(set(rs))
# print(*list(combinations(rs, 2)))
# print(list(permutations(rs, 2)))