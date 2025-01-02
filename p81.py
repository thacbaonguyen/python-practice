def solve(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count+=2 if i != n/i else 1
    return count
n = int(input())
rs = 0
for i in range(n):
    if solve(i) == 9:
        rs+=1
print(rs)