map = {}
count = 0
a = int(input())
check = True
while True:
    if count == a:
        break
    topic = input().strip()
    count+=1
    if count == a:
        break
    rs = []
    while True:
        t = input()
        if t == '':
            count+=1
            break
        rs.append(t)
        count+=1
        if count == a:
            break
    map[topic] = len(rs)
for i in map:
    print(i + ": " + str(map[i]))