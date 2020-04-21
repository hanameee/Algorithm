import sys
input = sys.stdin.readline

n, m = map(int, input().split())
book_position = sorted(list(map(int, input().split())))

positive_position = []
negative_position = []
for book in book_position:
    if book < 0:
        negative_position.append(-book)
    else:
        positive_position.append(book)
negative_position.sort()
steps = 0

if positive_position and negative_position:
    # 가장 멀리 떨어진 곳은 한번만 다녀온다
    if positive_position[-1] > negative_position[-1]:
        steps += positive_position.pop()
        for i in range(m-1):
            if positive_position:
                positive_position.pop()
            else:
                break
    else:
        steps += negative_position.pop()
        for i in range(m-1):
            if negative_position:
                negative_position.pop()
            else:
                break
elif positive_position:
    steps += positive_position.pop()
    for i in range(m-1):
        if positive_position:
            positive_position.pop()
        else:
            break
else:
    steps += negative_position.pop()
    for i in range(m-1):
        if negative_position:
            negative_position.pop()
        else:
            break

while positive_position:
    steps += positive_position.pop()*2
    for i in range(m-1):
        if positive_position:
            positive_position.pop()
        else:
            break


# 그 외의 지점들은 2번씩 돌아야 한다
while negative_position:
    steps += negative_position.pop()*2
    for i in range(m-1):
        if negative_position:
            negative_position.pop()
        else:
            break

print(steps)
