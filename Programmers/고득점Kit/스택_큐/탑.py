def solution(heights):
    arr = [0 for i in range(len(heights))]
    stack = []
    for i in range(len(heights)-1, -1, -1):
        curr_idx = i
        curr_height = heights[i]
        while stack:
            if stack[-1][0] < curr_height:
                arr[stack[-1][1]] = curr_idx+1
                stack.pop()
            else:
                break
        stack.append([curr_height, curr_idx])
    answer = arr
    return answer


# print(solution([3, 9, 9, 3, 5, 7, 2]))
print(solution([1, 5, 3, 6, 7, 6, 5]))
print(solution([6, 9, 5, 7, 4]))
