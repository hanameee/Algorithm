def solution(array, commands):
    result = []
    for command in commands:
        i, j, k = command
        data = array[i-1:j]
        data.sort()
        result.append(data[k-1])
    return result
