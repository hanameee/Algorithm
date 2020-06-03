def solution(n):
    q_3 = (n-1)//3
    q_5 = (n-1)//5
    q_15 = (n-1)//15
    answer = 3*((q_3)*(q_3+1))//2 + 5*((q_5)*(q_5+1))//2 - \
        15*((q_15)*(q_15+1))//2
    return answer


print(solution(1000))
