def solution(logs):
    digits = []
    letters = []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


print(solution(["a1 9 2 3 1", "g1 act car",
                "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
