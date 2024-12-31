inp = []
while True:
    try:
        inp += input().split()
    except Exception:
        break
def check(n):
    if len(n) > 0:
        for i in n:
            if i.isalnum():
                return True
    return False

for i in range(len(inp)):
    inp[i] = inp[i].lower()
ok = ['?', '.', '!']
rs =''
for i in inp:
    if i[-1] in ok:
        tmp = i.split('.')
        tmp = tmp[0].split('?')
        tmp = tmp[0].split('!')
        rs += tmp[0]
        if check(rs):
            print(rs[0].upper() + rs[1:])
        rs = ''
    else:
        rs += i + ' '

