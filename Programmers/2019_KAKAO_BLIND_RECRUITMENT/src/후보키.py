# 12:45~
from itertools import combinations


def solution(relation):
    keys = set([col for col in range(len(relation[0]))])
    original_rows = len(relation)
    valid_key = []
    i = 1
    while i <= len(keys):
        set_rows = set([])
        candidate_keys = combinations(keys, i)
        for candidate_key in candidate_keys:
            toContinue = False
            # 기존 v_keys 중 하나라도 candidate_key에 포함되어 있으면
            # print(valid_key, candidate_key)
            for v_keys in valid_key:
                chk = True
                for v in v_keys:
                    if v not in candidate_key:
                        chk = False
                        break
                # 지금 보는 combination이 이번 v_key를 포함한다는 뜻
                if chk:
                    # print(chk, toContinue, "!")
                    toContinue = True
                    break
            if toContinue:
                continue
            # print(valid_key, candidate_key)
            for row in relation:
                value = ""
                for key in candidate_key:
                    value += ","+row[key]
                set_rows.add(value)
            if original_rows == len(set_rows):
                valid_key.append(candidate_key)
                # if i == 1:
                #     for key in candidate_key:
                #         if key in keys:
                #             keys.remove(key)
            set_rows = set([])
        i += 1
    answer = valid_key
    return len(answer)


# print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
#       "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
print(solution([["1", "1", "1", "2"],
                ["2", "1", "2", "3"],
                ["3", "2", "1", "2"]]))
