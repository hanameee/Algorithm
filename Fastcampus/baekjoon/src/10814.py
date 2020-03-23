N = int(input())
data = list()
for i in range(N):
    age, name = input().split()
    data.append((int(age), name, i))

data.sort(key=lambda x: (x[0], x[2]))
for item in data:
    print(item[0], item[1])
