from collections import defaultdict


def solution(s):
    if not s:
        return 0
    mp = defaultdict(int)
    l = 0
    r = 0
    max_len = -1
    while r < len(s):
        if not mp[s[r]]:
            max_len = max(max_len, r-l+1)
            mp[s[r]] += 1
            r += 1
        else:
            mp[s[l]] -= 1
            l += 1
    return max_len


print(solution("abcabcbb"))
