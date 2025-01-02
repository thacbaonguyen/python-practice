n, m = map(int, input().split())
a = list(map(int, input().split()))
map = {}
maxx = 0
for i in a:
    if i in map:
        map[i] +=1
    else:
        map[i] = 1
    maxx = max(map[i], maxx)
tmp = 0
rs = 0
for i in range(m + 1):
    if i in map and map[i] != maxx and map[i] > tmp:
      rs = i
      tmp = map[i]
if rs == 0:
    print('NONE')
else:
    print(rs)