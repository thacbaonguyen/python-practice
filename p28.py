n = int(input())
while n >0:
    a = int(input())
    rs =0
    if a % 2 == 0:
        for i in range(2, a + 1, 2):
            rs+= 1/i
    else:
        for i in range(1, a + 1, 2):
            rs += 1/i
    n-=1
    print(f"{rs:.6f}")