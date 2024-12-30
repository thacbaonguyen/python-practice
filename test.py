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

a = [4]
b = [1, 2, 3, 'a']
a.append(2)
print(a[1])