def solution(clothes):
    kinds = {}
    for name, kind in clothes:
        if kind not in kinds:
            kinds[kind] = 2
        else:
            kinds[kind] += 1
    answer = 1
    print(kinds)
    for value in kinds.values():
        answer *= value
    return answer-1


print(solution([["yellow_hat", "headgear"], [
      "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
