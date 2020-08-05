from string import ascii_uppercase


def solution(msg):
    dictionary = {value: idx for idx, value in enumerate(ascii_uppercase, 1)}
    idx = 0
    idx_lst = []
    while idx < len(msg):
        w = msg[idx]
        while w in dictionary and idx+1 < len(msg):
            idx += 1
            w += msg[idx]
        # 더 이상 일치하지 않아서 빠져나온 경우
        if w not in dictionary:
            idx_lst.append(dictionary[w[:-1]])
            dictionary[w] = len(dictionary)+1
            continue
        else:
            idx_lst.append(dictionary[w])
        print(w, msg[idx])
        idx += 1
    answer = idx_lst
    return answer


print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))
