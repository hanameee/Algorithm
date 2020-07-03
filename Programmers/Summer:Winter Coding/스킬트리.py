def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        skill_arr = []
        for t in tree:
            if t in skill:
                skill_arr.append(t)
        new_skill = "".join(skill_arr)
        if new_skill == skill[:len(new_skill)]:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
