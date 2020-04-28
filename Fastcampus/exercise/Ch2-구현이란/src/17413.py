import sys
input = sys.stdin.readline

s = input()
result = ""
l = 0
r = 0

while len(s):
    # 지금 보고있는 문자열이 태그일때
    if s[0] == "<":
        tag_s = ''.join(s[s.find("<"):s.find(">")+1])
        result += tag_s
        s = s[s.find(">")+1:].strip()
    # 지금 보고있는 문자열이 태그가 아닐 때
    else:
        # 앞으로도 태그가 없을 때
        if s.find("<") == -1:
            reversed_s = list(s.split())
            for i in range(len(reversed_s)):
                reversed_s[i] = ''.join(reversed(reversed_s[i]))
            result += ' '.join(reversed_s)
            s = []
        else:
            cur_s = s[:s.find("<")]
            reversed_s = list(cur_s.split())
            for i in range(len(reversed_s)):
                reversed_s[i] = ''.join(reversed(reversed_s[i]))
            result += ' '.join(reversed_s)
            s = s[s.find("<"):].strip()
print(result)
