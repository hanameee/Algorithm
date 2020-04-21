import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

if k >= n:
    print(0)
else:
    arr = list(map(int, input().split()))
    arr.sort()
    gap_arr = []
    for i in range(1, len(arr)):
        gap_arr.append(arr[i]-arr[i-1])
    gap_arr.sort()
    result = sum(gap_arr[:len(arr)-k], 0)
    print(result)
