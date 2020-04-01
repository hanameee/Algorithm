import sys
x = sys.stdin.readline().strip()
y = sys.stdin.readline().strip()
lcs = [[0]*(len(y)+1) for _ in range(len(x)+1)]

for i in range(1, len(x)+1):
    none = True
    for j in range(1, len(y)+1):
        if x[i-1] == y[j-1]:
            lcs[i][j] = max(lcs[i-1][:j]) + 1
            none = False
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    if none:
        lcs[i] = lcs[i-1]

print(max(lcs[-1]))
