a = input()
if len(a) == 1:
    print(1)
else:
    cnt = 0
    while len(a) !=1:
        rs = 0
        for i in range(len(a)):
          rs += ord(a[i]) - ord('0')
        a = str(rs)
        cnt+=1
    print(cnt)