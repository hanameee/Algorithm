from itertools import combinations


def solution(relations):
    answer = 0
    candidate_cols = [i for i in range(len(relations[0]))]
    key_cols = []
    combination_i = 1
    while combination_i <= len(candidate_cols):
        candidate_combinations = combinations(candidate_cols, combination_i)
        for combi in candidate_combinations:
            is_unique = set([])
            for row in relations:
                new_row = ""
                for c in combi:
                    new_row += row[c] + "_"
                is_unique.add(new_row)
            if len(is_unique) == len(relations):
                flag = True
                for key in key_cols:
                    if len(set(key).intersection(set(combi))) == len(key):
                        flag = False
                        break
                if flag:
                    answer += 1
                    key_cols.append([*combi])
        combination_i += 1
    return answer


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["300", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))