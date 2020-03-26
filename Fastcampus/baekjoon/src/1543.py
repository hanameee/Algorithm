data = input()
target = input()
i = 0
result = 0

while data.find(target) != -1:
    result += 1
    index = data.find(target)
    data = data[index+len(target):]

print(result)
