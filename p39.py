def Try(l, s, count_a, count_b, count_c):
    if len(s) == l:
        if count_c >= count_b >= count_a > 0:
            print(s)
        return
    Try(l, s + 'A', count_a +1, count_b, count_c)
    Try(l, s + 'B', count_a, count_b + 1, count_c)
    Try(l, s + 'C', count_a, count_b, count_c +1)
t = int(input())
for i in range(3, t +1):
    Try(i, '', 0, 0, 0)