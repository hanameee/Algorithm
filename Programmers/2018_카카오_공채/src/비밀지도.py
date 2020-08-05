# 7:49~


def solution(n, arr1, arr2):
    lst1 = []
    lst2 = []
    for i in arr1:
        print(i)
        coded = format(i, "b")
        if len(coded) < n:
            coded = '0'*(n-len(coded)) + coded
        lst1.append(coded)
    for i in arr2:
        coded = format(i, "b")
        if len(coded) < n:
            coded = '0'*(n-len(coded)) + coded
        lst2.append(coded)
    answer = []
    for i in range(n):
        row_str = ""
        for j in range(n):
            if lst1[i][j] == "1" or lst2[i][j] == "1":
                row_str += "#"
            else:
                row_str += " "
        answer.append(row_str)
    return answer


solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
