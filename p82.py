def convert(n, k):
    if k in [2, 8, 16]:
        return bin(n)[2:] if k == 2 else oct(n)[2:] if k ==8 else hex(n)[2:].upper()
    else:
        rs = []
        while n >0:
            rs.append(str(n%k))
            n//=k
        return ''.join(reversed(rs))
with open('DATA.in', 'r') as file:
    t = int(file.readline())
    for i in range(t):
        k = int(file.readline())
        n = int(file.readline(), 2)
        rs = convert(n, k)
        print(rs)