import sys
N, C = map(int, sys.stdin.readline().split())
homes = list()
for _ in range(N):
    homes.append(int(sys.stdin.readline()))
homes.sort()

min_gap = 1
max_gap = homes[-1] - homes[0]

while min_gap != max_gap:
    target = set()
    i, j = 0, 1
    mid_gap = (max_gap + min_gap)//2
    if max_gap - min_gap == 1:
        mid_gap += 1
    while j < N:
        if homes[j]-homes[i] >= mid_gap:
            target.add(i)
            target.add(j)
            i, j = j, j+1
        else:
            j += 1
    if len(target) >= C:
        min_gap = mid_gap
    elif len(target) < C:
        max_gap = mid_gap-1

print(min_gap)
