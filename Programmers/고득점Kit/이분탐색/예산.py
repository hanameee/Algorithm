# def solution(budgets, M):
#     budgets.sort()
#     max_value = max(budgets)
#     if sum(budgets) <= M:
#         return max_value
#     else:
#         # 제일 작은 것도 평균보다 커질 때 까지
#         limit = M//len(budgets)
#         total_value = M
#         idx = 0
#         while budgets[idx] < limit:
#             for i in range(idx, len(budgets)):
#                 if budgets[i] > limit:
#                     break
#                 else:
#                     total_value -= budgets[i]
#                     limit_idx = i
#             idx = limit_idx+1
#             limit = total_value//(len(budgets)-idx)
#     return limit


def solution(budgets, M):
    max_value = max(budgets)
    if sum(budgets) <= M:
        return max_value
    l, r, mid = min(budgets), max(budgets), 0
    answer = 0
    # 이분탐색
    if l > M//len(budgets):
        return M//len(budgets)
    while l <= r:
        mid = (l+r) // 2
        total = 0
        for budget in budgets:
            if budget <= mid:
                total += budget
            else:
                total += mid
        if total > M:
            r = mid - 1
        else:
            if answer <= mid:
                answer = mid
            l = mid + 1
    return answer


print(solution([9, 8, 5, 6, 7], 5))
# print(solution([50, 50, 50, 50, 100, 100, 120, 120, 200, 240], 1000))
