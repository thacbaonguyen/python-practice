# import csv
# import json
#
# try:
#     with open('example.csv', 'r') as file:
#         csv_reader = csv.reader(file)
#         for row in csv_reader:
#             print(row)
# except Exception as ex:
#     print(ex)
#
# with open('example.json', 'r') as file:
#     data = json.load(file)
#     print(data)
# with open('example.txt', 'r') as file:
#     list_content = file.readlines()
#     for i in list_content:
#         print(i)
from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))
# a.sort()
b = Counter(a).most_common(1)
c = Counter(a)
check = True
for x, y in c.items():
    if y < b[0][1]:
        print(x)
        check = False
        break
if check:
    print('NONE')
