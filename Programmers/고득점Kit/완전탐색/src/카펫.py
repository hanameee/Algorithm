def solution(brown, yellow):
    multiply_value = yellow + brown
    sum_value = (brown+4)/2
    for i in range(1, int(multiply_value**0.5 + 1)):
        if multiply_value % i == 0:
            if i + (multiply_value)//i == sum_value:
                return sorted([i, (multiply_value)//i], key=lambda x: -x)


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
