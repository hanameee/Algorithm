import sys
input = sys.stdin.readline

s = input().strip()
a = 0
b = 0
toggled = False
ans = 0


if len(s) <= 1:
    print(0)
else:
    for idx in range(1, len(s)):
        if s[idx] != s[idx-1]:
            toggled = not(toggled)
            if toggled == False:
                ans += 1
        if idx == len(s) - 1:
            if toggled == True:
                ans += 1
    print(ans)
