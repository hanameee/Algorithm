import math
import sys
input = sys.stdin.readline

n = int(input())

logged_num = int(math.log2(n))
answer = 3**logged_num
n -= 2**logged_num
while n > 1:
    logged_num = int(math.log2(n))
    cumm = 3**logged_num
    answer += cumm
    n -= 2**logged_num
if n == 0:
    return answer
else:
    return answer + 1

print(solution(n))
