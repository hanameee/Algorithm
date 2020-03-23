N = int(input())
data = list()

for i in range(N):
    x, y = input().split()
    data.append((int(x), int(y)))

sorted_data = sorted(data)

for item in sorted_data:
    print(item[0], item[1])
