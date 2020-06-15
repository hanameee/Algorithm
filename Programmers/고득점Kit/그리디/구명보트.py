# 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
# 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.


def solution(people, limit):
    weight_count = [0 for i in range(241)]
    answer = 0
    n = len(people)
    done = 0
    people.sort()
    for w in people:
        weight_count[w] += 1
    while done < n:
        done += 1
        answer += 1
        cur_weight = people.pop()
        for i in range(limit-cur_weight, 39, -1):
            if weight_count[i] > 0:
                weight_count[i] -= 1
                done += 1
                break
    return answer


print(solution([70, 80, 50], 100))
