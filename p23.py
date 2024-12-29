s = input()
tmp = ''.join(reversed(s))
rs = ''
cnt =0
for i in tmp:
    if cnt == 3:
        rs += ','
        cnt =0
    rs += i
    cnt+= 1
print(''.join(reversed(rs)))
