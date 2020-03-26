from collections import defaultdict

dict = defaultdict(int)
N = int(input())

for _ in range(N):
    data = input()
    dict[data] += 1

max = max(dict.values())
maxBookList = []

for name, number in dict.items():
    if number == max:
        maxBookList.append(name)
maxBookList.sort()

print(maxBookList[0])
