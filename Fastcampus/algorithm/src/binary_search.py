import random
data_list = random.sample(range(15), 10)
# 이진탐색은 정렬이 되어 있어야 함
data_list = sorted(data_list)

# 내가 작성한 코드


def b_search(data, target):
    if len(data) > 1:
        medium = int(len(data)/2)
        left_list = data[:medium]
        right_list = data[medium:]
        if data[medium] == target:
            return True
        elif data[medium] < target:
            return b_search(right_list, target)
        else:
            return b_search(left_list, target)
        return False
    elif len(data) == 1:
        if data[0] == target:
            return True
        else:
            return False
    else:
        return False

# 강의 모범 답안 코드


def binary_search(data, search):
    print(data, search)
    if len(data) == 1 and data[0] == search:
        return True
    if len(data) == 1 and data[0] != search:
        return False
    if len(data) == 0:
        return False

    medium = len(data) // 2
    if search == data[medium]:
        return True
    else:
        if search < data[medium]:
            return binary_search(data[:medium], search)
        else:
            return binary_search(data[medium:], search)


print(binary_search(data_list, 1))
