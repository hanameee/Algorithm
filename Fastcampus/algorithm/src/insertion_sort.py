import random
data = random.sample(range(100), 15)
print(data)


def insertion_sort(data):
    for i in range(len(data)-1):
        for j in range(i+1, 0, -1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
            else:
                break
    return data


insertion_sort(data)
print(data)
