import sys
input = sys.stdin.readline
n, l, k = map(int, input().split())
prob = []
score = 0
for _ in range(n):
    easy, hard = map(int, input().split())
    prob.append((easy, hard))
prob.sort(key=lambda x: x[1])
solved_prob = [0]*n
for i in range(n):
    if k:
        # 어려운 문제 해결 가능하면
        if l >= prob[i][1]:
            score += 140
            solved_prob[i] = 1
            k -= 1

for i in range(n):
    if k:
        # 안푼 쉬운 문제 해결 가능하면
        if l >= prob[i][0] and solved_prob[i] == 0:
            score += 100
            k -= 1

print(score)
