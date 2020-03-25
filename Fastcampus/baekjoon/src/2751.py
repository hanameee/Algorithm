import sys


def merge(left, right):
    result = list()
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            result.append(right[right_index])
            right_index += 1
        else:
            result.append(left[left_index])
            left_index += 1
    while left_index < len(left):
        result.extend(left[left_index:])
        break
    while right_index < len(right):
        result.extend(right[right_index:])
        break
    return result


def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data)/2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left, right)


N = int(sys.stdin.readline())
data = list()

for _ in range(N):
    data.append(int(sys.stdin.readline()))

result = mergesplit(data)
print(*result, sep="\n")
