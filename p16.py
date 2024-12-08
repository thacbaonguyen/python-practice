def print_solve(c, n):
    for i in range(1, n + 1):
        print(c, end='')
t = int(input())
while t > 0:
    s = input()
    for i in range(0, len(s), 2):
        print_solve(s[i], int(s[i + 1]))
    print()
    t-=1