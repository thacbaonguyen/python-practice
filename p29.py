# t = int(input())
# while t >0:
#     n = int(input())
#
def count_x(n):
    rs =0
    for i in range(1, n + 1):
        if n % i ==0: rs+=1
    return rs
for i in range(1, 10000000+1):
    for j in range