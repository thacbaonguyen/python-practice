t = int(input())
while t > 0:
    n = int(input())
    check = True;
    while n > 0:
        k = n % 10;
        if k !=4 and k != 7:
            check = False;
        n//=10;
    if check == True:
        print('YES')
    else:
        print('NO')
    t-=1;