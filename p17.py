def print_solve(n):
    count = 1
    result = ''
    for i in range(1, len(n)):
        if n[i] == n[i -1]: count+=1
        else:
            result += str(count) + n[i -1]
            count = 1
    result+= str(count) + n[len(n) - 1]
    return result
t = int(input())
while t > 0:
    s = input()
    print(print_solve(s))
    t-=1

