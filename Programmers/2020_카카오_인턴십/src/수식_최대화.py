from itertools import permutations
from copy import deepcopy


def find_prev_idx(stk, idx):
    for i in range(idx-1, -1, -1):
        if stk[i] != "_":
            return i


def find_next_idx(stk, idx):
    for i in range(idx+1, len(stk)):
        if stk[i] != "_":
            return i


def solution(expression):
    used_operator = []
    # 사용된 연산자 찾기
    for char in expression:
        if char in ["*", "-", "+"] and char not in used_operator:
            used_operator.append(char)
    # 모든 연산자 조합 구하기
    candidate_operation = permutations(used_operator)
    temp = ""
    stk = []
    # 숫자와 연산자로 분리해서 스택에 넣기
    for char in expression:
        if char in used_operator:
            stk.append(temp)
            stk.append(char)
            temp = ""
        else:
            temp += char
    stk.append(temp)
    answer = 0
    for candidate in candidate_operation:
        copied_stk = deepcopy(stk)
        # 우선순위 연산자별로 돌면서 계산해주기
        for operation in candidate:
            result = 0
            for idx in range(len(copied_stk)):
                if copied_stk[idx] == operation:
                    # _가 아닌 전후 인덱스 찾기
                    prev_idx = find_prev_idx(copied_stk, idx)
                    next_idx = find_next_idx(copied_stk, idx)
                    copied_stk[idx] = eval(
                        str(copied_stk[prev_idx])+copied_stk[idx]+str(copied_stk[next_idx]))
                    # 연산 결과를 result에 저장해 최종 값이 자동으로 result 변수에 저장되게 함
                    result = copied_stk[idx]
                    # 사용한 값은 _ 로 변경
                    copied_stk[prev_idx] = "_"
                    copied_stk[next_idx] = "_"
        answer = max(answer, abs(result))
    return answer


print(solution("100-200*300-500+20"))

test = [1, 2, 3]
for i in test:
    i = i*2
test2 = [1, 2, 3]
for i in range(len(test2)):
    test2[i] *= 2

print(test, test2)
