def solution(s):
    l = 0
    max_len = 1
    while l < len(s)-1:
        r = l+max_len+1
        while r <= len(s):
            if s[l:r] == s[l:r][::-1]:
                max_len = r-l
            r += 1
        l += 1
    return max_len


print(solution("abcdcba"))
print(solution("abacde"))
