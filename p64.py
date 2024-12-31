t = int(input())
a = list(map(float, input().split()))
a  = [i for i in a if (i != min(a) and i != max(a))]
print(f"{sum(a)/len(a):.3}")