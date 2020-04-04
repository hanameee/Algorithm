import sys
n = int(sys.stdin.readline())
numbers = list()
for i in range(n):
    numbers.append(int(sys.stdin.readline()))

numbers = sorted(numbers)
gap = 0
for i in range(1, len(numbers)+1):
    gap += abs(numbers[i-1]-i)

print(gap)
