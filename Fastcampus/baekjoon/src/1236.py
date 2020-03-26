x, y = map(int, (input().split()))
guardList = list()

for i in range(x):
    data = list(input())
    for j in range(y):
        if data[j] == "X":
            guardList.append([i, j])

x_guard = set()
y_guard = set()
for guard in guardList:
    x_guard.add(guard[0])
    y_guard.add(guard[1])

left_result = 0
right_result = 0
for i in range(x):
    if i not in x_guard:
        left_result += 1

for j in range(y):
    if j not in y_guard:
        right_result += 1

print(max(left_result, right_result))
