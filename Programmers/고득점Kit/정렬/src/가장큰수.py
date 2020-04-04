def compare(a, b):
    # 자릿수가 같으면 a와 b 비교, 자릿수가 다르면 a+b, b+a 비교 (앞뒤로 붙인 것)
    return a <= b if len(a) == len(b) else a+b <= b+a
    # compare이 양수면 a<=b, 음수면 a>b


def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [element for element in arr[1:] if not compare(element, pivot)]
        right = [element for element in arr[1:] if compare(element, pivot)]
        return quick_sort(left) + [pivot] + quick_sort(right)


def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers = quick_sort(str_numbers)
    answer = ''.join(str_numbers)
    return answer if str_numbers[0] != "0" else "0"


print(solution([3, 30, 34, 5, 9]))
