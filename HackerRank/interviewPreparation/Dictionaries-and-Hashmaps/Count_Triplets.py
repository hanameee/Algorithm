def countTriplets(arr, r):
    d = {}
    count = {}
    answer = 0
    for num in arr:
        if num % r == 0 and num//r in count:
            answer += count[num//r]
        if num % r == 0 and num//r in d:
            value = d[num//r]
            if num in count:
                count[num] += value
            else:
                count[num] = value
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    return answer


nr = input().rstrip().split()

n = int(nr[0])

r = int(nr[1])

arr = list(map(int, input().rstrip().split()))

ans = countTriplets(arr, r)
print(ans)
