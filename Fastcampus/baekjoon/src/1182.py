n, s = map(int, input().split())
data = list(map(int, input().split()))
count = 0
k = 1 << n


def get_sum(num):
    global n, s, count
    result = 0
    for i in range(n):
        if (num & (1 << i)):
            result += data[i]
    if result == s:
        count += 1


for num in range(1, k):
    get_sum(num)


print(count)
