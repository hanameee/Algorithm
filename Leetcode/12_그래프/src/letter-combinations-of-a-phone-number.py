def solution(digits):
    phone_map = [None, None, "abc", "def", "ghi",
                 "jkl", "mno", "pqrs", "tuv", "wxyz"]
    result = []

    def dfs(v, buf):
        if digits == "":
        buf += v
        if len(buf) == len(digits):
            result.append(buf)
            return
        for child in phone_map[int(digits[len(buf)])]:
            dfs(child, buf)

    for root in phone_map[int(digits[0])]:
        dfs(root, "")
    return result


print(solution("23"))
