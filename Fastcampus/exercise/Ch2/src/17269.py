import sys
input = sys.stdin.readline

num = {
    "A": 3,
    "B": 2,
    "C": 1,
    "D": 2,
    "E": 4,
    "F": 3,
    "G": 1,
    "H": 3,
    "I": 1,
    "J": 1,
    "K": 3,
    "L": 1,
    "M": 3,
    "N": 2,
    "O": 1,
    "P": 2,
    "Q": 2,
    "R": 2,
    "S": 1,
    "T": 2,
    "U": 1,
    "V": 1,
    "W": 1,
    "X": 2,
    "Y": 2,
    "Z": 1,
}

n, m = map(int, input().split())
a, b = input().split()
min_len = min(len(a), len(b))
num_arr = [0]*(min_len*2)
for i in range(min_len*2):
    if i % 2 == 0:
        num_arr[i] = num[a[int(i//2)]]
    else:
        num_arr[i] = num[b[int(i//2)]]
if len(a) < len(b):
    for i in range(min_len, len(b)):
        num_arr.append(num[b[i]])
else:
    for i in range(min_len, len(a)):
        num_arr.append(num[a[i]])

while len(num_arr) > 2:
    new_arr = []
    for i in range(0, len(num_arr)-1):
        new_num = (num_arr[i]+num_arr[i+1]) % 10
        new_arr.append(new_num)
    num_arr = new_arr

num_arr = list(map(str, num_arr))
if num_arr[0] == "0":
    print(num_arr[1]+"%")
else:
    print(num_arr[0]+num_arr[1]+"%")
