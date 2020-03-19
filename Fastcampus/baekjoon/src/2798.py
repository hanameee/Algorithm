N, M = list(map(int, input().split(" ")))
data = list(map(int, input().split(" ")))
combination = list()
for A in range(0, N-2):
    for B in range(A+1, N-1):
        for C in range(B+1, N):
            result = data[A] + data[B] + data[C]
            if result <= M:
                combination.append(result)

print(max(combination))
