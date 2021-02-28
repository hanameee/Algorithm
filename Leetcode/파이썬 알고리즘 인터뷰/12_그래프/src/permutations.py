def solution(nums):
    answer = []

    def dfs(v, buf):
        if v not in buf:
            buf.append(v)
            if len(buf) == len(nums):
                answer.append(buf[::])
                buf.pop()
                return
            for candidate_num in nums:
                if candidate_num not in buf:
                    dfs(candidate_num, buf)
            buf.pop()
    for num in nums:
        dfs(num, [])
    return answer


print(solution([1, 2, 3]))
