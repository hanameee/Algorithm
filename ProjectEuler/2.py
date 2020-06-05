arr = [1, 2]
result = 0


def fibo(n):
    global arr, result
    while True:
        print(arr)
        if arr[1] > n:
            break
        else:
            if arr[1] % 2 == 0:
                result += arr[1]
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] += temp
    return result


print(fibo(4000000))
