rs = []
def inspect(n):
    if rs.count(n % 42) == 0:
        rs.append(n % 42)
data = []
while len(data) < 10:
    data += list(map(int, input().split()))
for i in range(0, len(data)):
    inspect(data[i])
print(len(rs))