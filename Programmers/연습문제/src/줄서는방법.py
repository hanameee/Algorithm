from itertools import permutations
import math

print(math.factorial(20))
# def solution(n, k):
#     answer = []
#     arr = [i for i in range(1, n+1)]
#     k -= 1
#     while arr:
#         div, mod = divmod((k), math.factorial(len(arr)-1))
#         print(div, mod)
#         answer.append(arr[div])
#         arr.pop(div)
#         k = mod
#         if k == 0:
#             answer.extend(arr)
#             return answer
#     return answer


# print(solution(3, 5))
