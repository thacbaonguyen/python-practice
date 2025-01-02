t = int(input())
rs = []
while len(rs) < t:
    rs.extend(list(map(int, input().split())))
le = []
chan = []
for i in range(len(rs)):
    if rs[i] % 2 == 0:
        chan.append(rs[i])
    else:
        le.append(rs[i])
chan.sort()
le.sort(reverse=True)
ic, il = 0, 0
for i in range(len(rs)):
    if rs[i] % 2 ==0:
        rs[i] = chan[ic]
        ic+=1
    else:
        rs[i] = le[il]
        il+=1
print(*rs)