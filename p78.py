import re

rs = []
map = {}
for i in range(int(input())):
    rs.extend(re.split(r'[^a-zA-Z0-9]', input()))
rs = [x for x in rs if x]

for i in range(len(rs)):
    rs[i] = rs[i].lower()
rs.sort()
result = []
for i in rs:
    if i not in map:
        map[i] = 1
    else:
        map[i] += 1
for i in map:
    result.append([i, map[i]])
result = sorted(result, key=lambda x: (-x[1]))
for i in result:
    print(i[0], i[1])