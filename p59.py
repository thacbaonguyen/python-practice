while True:
    rs = []
    n = int(input())
    if n ==0:
        break
    if n == 1:
        print(1)
    else:
        rs = []
        rs.append(n)
        while n !=1:
            if n % 2 == 0:
                rs.append(n/2)
                n //= 2
            else:
                rs.append(n*3 + 1)
                n = n * 3 +1
        print(len(rs))
