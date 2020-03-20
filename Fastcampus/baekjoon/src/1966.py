test_case = int(input())
result = list()

for i in range(test_case):
    N, M = list(map(int, input().split(" ")))
    data = list(map(int, input().split(" ")))
    target_index = M
    popped = 0
    max_data = max(data)
    while data:
        if data[0] != max(data):
            temp = data[0]
            data.pop(0)
            data.append(temp)
            if target_index == 0:
                target_index = len(data) - 1
            else:
                target_index -= 1
        else:
            if target_index == 0:
                result.append(str(popped+1))
            data.pop(0)
            popped += 1
            target_index -= 1

print("\n".join(result))
