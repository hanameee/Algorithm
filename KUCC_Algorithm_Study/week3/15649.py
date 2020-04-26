n, m = list(map(int, input().split()))
visited = [False]*(n+1)  # 1부터 n까지
result = 0
answerStr = []


def visit(num, idx):
    global result, visited, answerStr
    if idx == m-1:
        result += 1
        answerStr.append(str(num))
        for s in answerStr:
            print(s, end=" ")
        print()
        answerStr.pop()
        return 0
    if not visited[num]:
        visited[num] = True
        answerStr.append(str(num))
        for i in range(1, n+1):
            if not visited[i]:
                idx += 1
                visit(i, idx)
                idx -= 1
        visited[num] = False
        answerStr.pop()


for i in range(1, n+1):
    visit(i, 0)
