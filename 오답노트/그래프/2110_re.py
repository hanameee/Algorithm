import sys
n, m = map(int, sys.stdin.readline().split())
home = []
for i in range(n):
    home.append(int(input()))
home.sort()

min_width = home[1]-home[0]
max_width = home[-1]-home[0]
answer = 0

while min_width <= max_width:
    current_width = (min_width+max_width)//2
    start_home = home[0]
    count = 1
    for home_place in home[1:]:
        if home_place - start_home >= current_width:
            count += 1
            start_home = home_place
            if count > m:
                break
    # 꼭 count == m 이어야 하는게 아님. 주의!
    if count >= m:
        answer = max(current_width, answer)
        min_width = current_width + 1
    else:
        max_width = current_width - 1

print(answer)
