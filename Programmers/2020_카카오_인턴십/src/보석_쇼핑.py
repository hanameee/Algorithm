def solution(gems):
    gems_set = set(gems)
    gems_dict = {}
    min_length = float("inf")
    answer_arr = []
    start_idx = 0
    end_idx = 0
    for idx in range(len(gems)):
        if gems[idx] not in gems_dict:
            gems_dict[gems[idx]] = 1
            if len(gems_dict.keys()) == len(gems_set):
                end_idx = idx
                break
        else:
            gems_dict[gems[idx]] += 1
    while end_idx < len(gems):
        while gems_dict[gems[start_idx]] > 1:
            gems_dict[gems[start_idx]] -= 1
            start_idx += 1
        if min_length > end_idx - start_idx:
            answer_arr = [start_idx+1, end_idx+1]
            min_length = end_idx-start_idx
        end_idx += 1
        if end_idx < len(gems):
            gems_dict[gems[end_idx]] += 1
    return answer_arr

# 공식 해설 참고 풀이
# def solution(gems):
#     gems_set = set(gems)
#     gems_dict = {gems[0]: 1}
#     start_idx = 0
#     end_idx = 0
#     min_length = float("inf")
#     answer = [start_idx, end_idx]
#     while end_idx < len(gems):
#         if len(gems_dict) == len(gems_set):
#             while gems_dict[gems[start_idx]] > 1:
#                 gems_dict[gems[start_idx]] -= 1
#                 start_idx += 1
#             if end_idx - start_idx < min_length:
#                 min_length = end_idx - start_idx
#                 answer = [start_idx+1, end_idx+1]
#         end_idx += 1
#         if end_idx < len(gems):
#             if gems[end_idx] not in gems_dict:
#                 gems_dict[gems[end_idx]] = 1
#             else:
#                 gems_dict[gems[end_idx]] += 1
#     return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA",
                "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(	["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution([1, 2, 4, 1, 1, 3, 1, 1, 2, 3, 4, 4, 3, 4, 4, 2, 1]))
