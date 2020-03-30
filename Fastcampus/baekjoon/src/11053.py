import sys
n = int(sys.stdin.readline())
ascending = [0 for i in range(1001)]
numbers = map(int, sys.stdin.readline().split())

for number in numbers:
    ascending[number] = max(ascending[:number]) + 1

print(max(ascending))
