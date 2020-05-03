import sys
input = sys.stdin.readline
n = input().strip()

if n == "0":
    print(1)
elif int(n) >= int("1"*len(n)):
    print(len(n))
else:
    print(len(n)-1)
