import sys
input = sys.stdin.readline
s = input().strip()
answer = len(s)
for i in range(1, (len(s)//2)+1):
    chk_str = ""
    st_idx = 0
    end_idx = i
    count = 0
    length = len(s)
    while end_idx <= len(s):
        chk_str = s[st_idx:end_idx]
        # 같으면
        while chk_str == s[st_idx+i:end_idx+i]:
            count += 1
            if end_idx + i <= len(s):
                st_idx += i
                end_idx += i
            else:
                break
        # 누적된 압축 문자열이 있으면
        if count:
            print(i, chk_str, count, "!")
            length = length - ((count+1)*i)+len(str(count+1))+i
        # 없으면 그냥 탐색 범위를 1 증가한다
        count = 0
        st_idx += i
        end_idx += i
    print(i, length)
    answer = min(answer, length)
print(answer)
