for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    stack = []
    rs = []
    for i in range(len(a)):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        if not stack:
            count = i + 1
        else:
            count = i - stack[-1]
        stack.append(i)
        rs.append(count)
    for i in rs:
        print(i, end= ' ')
    print()
