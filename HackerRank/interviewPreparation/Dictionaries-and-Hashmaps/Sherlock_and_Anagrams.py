def sherlockAndAnagrams(s):
    answer = 0
    d = {}
    for i in range(len(s)):
        for j in range(i+1, len(s)+1, 1):
            target = "".join(sorted(list(s[i:j])))
            if target in d:
                d[target] += 1
            else:
                d[target] = 1
    for key in d.keys():
        value = d[key]
        if value >= 2:
            answer += (value)*(value-1)//2
    return answer
