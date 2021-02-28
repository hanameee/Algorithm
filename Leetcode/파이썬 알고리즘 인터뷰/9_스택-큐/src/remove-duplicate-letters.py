from collections import Counter
# 재귀 사용 풀이


def solution(s):
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        if set(s) == set(suffix):
            return char + solution(suffix.replace(char, ""))
    return ''

# 스택 사용 풀이


def stackSolution(s):
    counter, seen, stk = Counter(s), set(), []
    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        while stk and char < stk[-1] and counter[stk[-1]] > 0:
            seen.remove(stk.pop())
        stk.append(char)
        seen.add(char)
    return ''.join(stk)


print(solution("cbacdcbc"))
