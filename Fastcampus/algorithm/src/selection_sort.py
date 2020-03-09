import random
data = random.sample(range(100), 15)
print(data)


def selection_sort(data):
    for i in range(len(data)-1):
        min_index = i
        for j in range(i+1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]


selection_sort(data)
print(data)
