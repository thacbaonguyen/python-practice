class student:
    def __init__(self, name, correct, submit):
        self.name = name
        self.correct = correct
        self.submit = submit
rs = []
for i in range(int(input())):
    a = input()
    b, c = map(int, input().split())
    rs.append(student(a, b, c))
rs = sorted(rs, key = lambda x : ((-1)*x.correct, x.submit, x.name))
for item in rs:
    print(item.name, item.correct, item.submit)
