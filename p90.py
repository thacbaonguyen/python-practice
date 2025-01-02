a = input()
ok = True
for i in range(len(a)):
    if a[i] not in ['6','8']:
        ok = False
        break
if not ok:
    print('NO')
else:
    check = True
    for i in range(len(a) - 2):
        if a[i:i+3] == '888':
            check = False
            break
    if check:
        print('YES')
    else:
        print('NO')