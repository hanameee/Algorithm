import random
data_list = random.sample(range(100), 10)
print(data_list)


def quicksort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = list()
    right = list()
    for index in range(1, len(data)):
        if data[index] < pivot:
            left.append(data[index])
        else:
            right.append(data[index])
    return quicksort(left)+[pivot]+quicksort(right)


print(quicksort(data_list))


# list comprehension을 통해 작성한 조금 더 간결한 퀵소트 코드
def quicksort_s(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [item for item in data[1:] if item < pivot]
    right = [item for item in data[1:] if pivot <= item]
    return quicksort_s(left) + [pivot] + quicksort_s(right)


print(quicksort_s(data_list))
