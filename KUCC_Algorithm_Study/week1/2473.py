import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()
min_combination = []
min_sum = 5e9


def compare(cur_v, old_v):
    if abs(cur_v) < abs(old_v):
        return True
    else:
        return False


for i in range(0, n-2):
    j = i+1
    k = n-1
    while j < k:
        sum_value = data[i]+data[j]+data[k]
        if sum_value != 0:
            if compare(sum_value, min_sum):
                min_sum = sum_value
                min_combination = [data[i], data[j], data[k]]
            if sum_value > 0:
                k -= 1
            else:
                j += 1
        else:
            min_combination = [data[i], data[j], data[k]]
            break

min_combination.sort()
for i in min_combination:
    print(i, end=" ")
