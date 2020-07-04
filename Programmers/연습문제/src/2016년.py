def solution(a, b):
    days_arr = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_list = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month = 1
    total_days = 0
    while month < a:
        total_days += days_arr[month-1]
        month += 1
    total_days += b
    return days_list[total_days % 7]


print(solution(5, 24))
