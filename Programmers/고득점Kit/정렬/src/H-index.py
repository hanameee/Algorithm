def solution(citations):
    citations.sort(reverse=True)
    h = citations[0]
    while True:
        check = 0
        for num in citations:
            if h <= num:
                check += 1
                if check >= h:
                    return h
            else:
                break
        h -= 1
    return answer


print(solution([3, 0, 6, 1, 5]))
