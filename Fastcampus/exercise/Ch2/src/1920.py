import sys
input = sys.stdin.readline

n = int(input())
n_data = list(map(int, input().split()))
n_data.sort()
m = int(input())
m_data = list(map(int, input().split()))

# arr = 대상을 찾는 배열 target = 찾는 숫자


def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] > target:
            high = mid-1
        elif arr[mid] < target:
            low = mid+1
        else:
            return 1
    return 0


for target in m_data:
    print(binary_search(n_data, target))
