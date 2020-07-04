import copy


def solution(land):
    dp = copy.deepcopy(land)
    dp[0] = land[0]
    for row_idx in range(1, len(land)):
        for col_idx in range(4):
            max_prev_value = 0
            for prev_col_idx in range(4):
                if col_idx != prev_col_idx:
                    max_prev_value = max(
                        max_prev_value, dp[row_idx-1][prev_col_idx])
            dp[row_idx][col_idx] += max_prev_value
    return max(dp[-1])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
