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
import math

rs = []
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
for i in range(2, 10000):
    if is_prime(i):
        rs.append(i)
print(rs)