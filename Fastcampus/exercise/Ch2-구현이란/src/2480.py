data = list(map(int, input().split()))
set_data = set(data)
case = len(set_data)
score = 0
if case == 3:
    score = max(data)*100
elif case == 2:
    value = data[0]
    for i in data[1:]:
        if i == value:
            score = 1000+value*100
    if not score:
        score = 1000+data[1]*100
else:
    score = 10000+data[0]*1000
print(score)
