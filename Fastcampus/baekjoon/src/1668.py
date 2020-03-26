N = int(input())
shelf = list()
for _ in range(N):
    shelf.append(int(input()))

max = 0
left = 0
right = 0
for trophy in shelf:
    if max < trophy:
        left += 1
        max = trophy
print(left)

shelf.reverse()
max = 0

for trophy in shelf:
    if max < trophy:
        right += 1
        max = trophy
print(right)
