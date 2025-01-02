t = int(input())
a = list(map(int, input().split()))

min_steps = float('inf')
chosen_value = a[0]

for target in set(a):
    steps = sum(abs(x - target) for x in a)
    if steps < min_steps or (steps == min_steps and a.index(target) < a.index(chosen_value)):
        min_steps = steps
        chosen_value = target

print(min_steps, chosen_value)
