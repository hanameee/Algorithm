import collections


def solution(strs):
    dic = collections.defaultdict(list)
    for item in strs:
        dic["".join(sorted(list(item)))].append(item)
    return [value for key, value in dic.items()]


print(solution(["eat", "tea", "tan", "ate", "nat", "bat"]))
