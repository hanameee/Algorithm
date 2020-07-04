def solution(n):
    target = str(bin(n)).count("1")
    while True:
        n += 1
        if str(bin(n)).count("1") == target:
            return n


print(solution(78))
print(solution(15))
