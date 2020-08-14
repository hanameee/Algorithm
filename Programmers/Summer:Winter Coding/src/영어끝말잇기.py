def solution(n, words):
    word_set = [words[0]]
    for idx in range(1, len(words)):
        if words[idx] in word_set:
            return [(idx % n)+1, (idx)//n+1]
        else:
            word_set.append(words[idx])
        if words[idx][0] != words[idx-1][-1]:
            return [(idx % n)+1, (idx)//n+1]
    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel", "land",
                   "dream", "mother", "robot", "tank"]))
