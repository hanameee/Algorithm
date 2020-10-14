def solution(a):
    answer = len(a)
    if len(a) <= 3:
        return len(a)
    left_min, left_arr = float("inf"),  [0 for i in range(len(a))]
    right_min, right_arr = float("inf"), [0 for i in range(len(a))]
    for i in range(len(a)):
        if a[i] < left_min:
            left_arr[i] = a[i]
            left_min = a[i]
        else:
            left_arr[i] = left_min
    for i in range(len(a)-1, -1, -1):
        if a[i] < right_min:
            right_arr[i] = a[i]
            right_min = a[i]
        else:
            right_arr[i] = right_min
    for i in range(1, len(a)-1):
        if a[i] > left_arr[i-1] and a[i] > right_arr[i+1]:
            answer -= 1
    return answer


print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
