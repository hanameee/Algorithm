import sys
input = sys.stdin.readline

n = int(input())
data = [0]*n
set_data = [0]*n
score = [0]*n
for i in range(n):
    data[i] = sorted(list(map(int, (input().split()))))
    set_data[i] = list(set(data[i]))

for i in range(n):
    # 같은 눈 4개
    if len(set_data[i]) == 1:
        score[i] = 50000+set_data[i][0]*5000
    # 같은 눈 3개 혹은 같은 눈 2개
    elif len(set_data[i]) == 2:
        isThree = False
        three_num = 0
        for num in set_data[i]:
            count = 0
            for num2 in data[i]:
                if num2 == num:
                    count += 1
            if count == 3:
                isThree = True
                three_num = num
        if isThree:
            score[i] = 10000+three_num*1000
        else:
            score[i] = 2000+(data[i][0]+data[i][2])*500
    # 같은 눈 1개
    elif len(set_data[i]) == 3:
        duplicate_num = 0
        for num in set_data[i]:
            count = 0
            for num2 in data[i]:
                if num2 == num:
                    count += 1
            if count == 2:
                duplicate_num = num
                break
        score[i] = 1000+(duplicate_num)*100
    # 같은 눈 없을 때
    else:
        score[i] = data[i][-1]*100

print(max(score))
