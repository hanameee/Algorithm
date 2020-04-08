n, r, c = map(int, input().split())
step = 0
# 뒤 인덱스부터 도는 것 조심
for i in range(n, -1, -1):
    if r < 2**(i) and c < 2**(i):
        continue
    elif r < 2**(i) and c >= 2**(i):
        step += (2**(i))**2
        c -= 2**(i)
    elif r >= 2**(i) and c < 2**(i):
        step += ((2**(i))**2)*2
        r -= 2**(i)
    else:
        step += ((2**(i))**2)*3
        r -= 2**(i)
        c -= 2**(i)
print(step)
