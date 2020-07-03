# import string


# def solution(name):
#     answer = len(name)-1
#     alphabets = string.ascii_uppercase
#     if len(name) == 1:
#         return min(alphabets.index(name[0]),
#                    len(alphabets)-alphabets.index(name[0]))
#     cum_a = 0
#     if name[1] == "A":
#         cum_a += 1
#         i = 2
#         while True:
#             if i == len(name):
#                 return min(alphabets.index(name[0]),
#                            len(alphabets)-alphabets.index(name[0]))
#             if name[i] != "A":
#                 break
#             cum_a += 1
#             i += 1
#     reverse_cum_a = 0
#     if name[-1] == "A":
#         reverse_cum_a += 1
#         i = -2
#         while True:
#             if -i > len(name):
#                 break
#             if name[i] != "A":
#                 break
#             reverse_cum_a += 1
#             i -= 1
#     answer -= max(reverse_cum_a, cum_a)
#     for alphabet in name:
#         answer += min(alphabets.index(alphabet),
#                       len(alphabets)-alphabets.index(alphabet))
#     return answer


# print(solution("AABAAAAAAAB"))

import string


def calculate_vertical(alphabet):
    alphabets = string.ascii_uppercase
    return min(alphabets.index(alphabet),
               len(alphabets)-alphabets.index(alphabet))


def calculate_horizontal(cur_idx, target_idx, n):
    return min(abs(target_idx-cur_idx), cur_idx+n-target_idx)


def find_next(cur_idx, name, ck, n):
    target_idx = 0
    min_step = len(name)
    done = True
    for i in range(len(name)):
        if ck[i] == False and name[i] != "A":
            done = False
            calculated_step = calculate_horizontal(cur_idx, i, n)
            if calculated_step < min_step:
                target_idx = i
                min_step = calculated_step
    if done:
        return [-1, -1]
    return [target_idx, min_step]


def solution(name):
    ck = [False for i in range(len(name))]
    ck[0] = True
    n = len(name)
    result = calculate_vertical(name[0])
    cur_idx = 0
    while True:
        target_idx, min_step = find_next(cur_idx, name, ck, n)
        if min_step == -1:
            break
        ck[target_idx] = True
        cur_idx = target_idx
        result += min_step + calculate_vertical(name[target_idx])
    return result


# print(solution("CANAAAAANAN"))
print(solution("ABABAAAAAAABA"))
