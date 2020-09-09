def solution(dartResult):
    # 주어진 dartResult를 파싱하기
    lst = []
    num = 0
    for dr in range(len(dartResult)):
        if dartResult[dr] in ["S", "D", "T"]:
            if dartResult[dr] == "D":
                num = num**2
            elif dartResult[dr] == "T":
                num = num**3
            if dr + 1 == len(dartResult) or dartResult[dr+1] not in ["*", "#"]:
                lst.append(num)
                num = 0
        elif dartResult[dr] in ["*", "#"]:
            if dartResult[dr] == "*":
                num *= 2
                if lst:
                    lst[-1] *= 2
            else:
                num *= -1
            lst.append(num)
            num = 0
        else:
            if dartResult[dr] == "0" and num == 1:
                num = 10
            else:
                num = int(dartResult[dr])
    answer = sum(lst)
    return answer


print(solution("1D2S#10S"))
