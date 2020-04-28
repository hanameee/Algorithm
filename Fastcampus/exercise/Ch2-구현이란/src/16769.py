milk_data = []
for i in range(3):
    c, m = map(int, input().split())
    milk_data.append([c, m])


def pour(source, target):
    s_c, s_m = source
    t_c, t_m = target
    # s_m가 t_c-t_m보다 같거나 작다면
    if s_m <= t_c-t_m:
        source[1] = 0
        target[1] = t_m+s_m
    else:
        source[1] -= t_c-t_m
        target[1] = t_c
    return (source, target)


for i in range(100):
    source = milk_data[i % 3]
    target = milk_data[(i+1) % 3]
    pour(source, target)

for data in milk_data:
    print(data[1])
