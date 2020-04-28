import sys
input = sys.stdin.readline

test_case = int(input())


def is_same(arr):
    value = arr[0]
    for item in arr[1:]:
        if item != value:
            return False
    return True


for _ in range(test_case):
    cycle = 0
    n = int(input())
    candies = list(map(int, input().split()))
    for i in range(n):
        if candies[i] % 2 == 1:
            candies[i] += 1
    while True:
        if is_same(candies):
            print(cycle)
            break
        new_candies = [0]*n
        for i in range(n):
            new_candies[i] = (candies[i-1]//2)+(candies[i]//2)
            if new_candies[i] % 2 == 1:
                new_candies[i] += 1
        candies = new_candies
        cycle += 1
