test_list = list(map(int, input().split(" ")))


def solution(test_list):
    if test_list[0] + 1 == test_list[1]:
        for index in range(1, 7):
            if test_list[index] + 1 != test_list[index+1]:
                return "mixed"
        return "ascending"
    if test_list[0] - 1 == test_list[1]:
        for index in range(1, 7):
            if test_list[index] - 1 != test_list[index+1]:
                return "mixed"
        return "descending"
    return "mixed"


print(solution(test_list))
