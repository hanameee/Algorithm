def solution(answers):
    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans_arr = [0, 0, 0]
    for idx in range(len(answers)):
        if answers[idx] == std1[idx % (len(std1))]:
            ans_arr[0] += 1
        if answers[idx] == std2[idx % (len(std2))]:
            ans_arr[1] += 1
        if answers[idx] == std3[idx % (len(std3))]:
            ans_arr[2] += 1
    max_ans = max(ans_arr)
    answer = []
    for idx in range(3):
        if ans_arr[idx] == max_ans:
            answer.append(idx+1)
    return answer
