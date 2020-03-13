import random
data_list = random.sample(range(100), 21)
print(data_list)


def merge(left, right):
    result = list()
    left_index = 0
    right_index = 0
    while len(left) > left_index and len(right) > right_index:
        if left[left_index] > right[right_index]:
            result.append(right[right_index])
            right_index += 1
        else:
            result.append(left[left_index])
            left_index += 1
    while len(left) > left_index:
        result.extend(left[left_index:])
        break
    while len(right) > right_index:
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


print(mergesplit(data_list))
