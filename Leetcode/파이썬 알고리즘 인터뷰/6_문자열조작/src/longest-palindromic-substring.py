def solution(s):
    l = 0
    max_len = 1
    max_l = 0
    while l < len(s)-1:
        r = l+max_len
        while r < len(s):
            target = s[l:r+1]
            if target == target[::-1]:
                max_len = r-l+1
                max_l = l
            r += 1
        l += 1
    print(s[max_l:max_l+max_len])


solution("babad")
