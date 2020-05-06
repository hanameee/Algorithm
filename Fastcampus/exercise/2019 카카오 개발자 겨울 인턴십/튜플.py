def solution(s):
    dp = [False for i in range(100001)]
    s = s[1:-1]
    answer = []
    words = []
    word_stack = []
    # 파싱하기
    # 튜플의 원소가 하나인경우
    print(s)
    if "," not in s:
        return [int(s[1:len(s)-1])]
    # 그 외의 경우
    else:
        idx = 0
        words = []
        word_stack = []
        word = ""
        while idx < len(s):
            # 한 그룹 시작
            if s[idx] == "{":
                i = idx+1
                # 한 그룹 끝날 때 까지
                while s[i] != "}":
                    if s[i] != ",":
                        word += s[i]
                        i += 1
                    else:
                        word_stack.append(int(word))
                        word = ""
                        i += 1
                        print(s, i)
                if word:
                    word_stack.append(int(word))
                    word = ""
            # 한 그룹 끝나고 다시 돌아오는 코드
            idx = i+2
            words.append(word_stack)
            word_stack = []
        if word:
            word_stack.append(int(word))
    print(words)
    words.sort(key=lambda x: len(x))
    for word in words:
        for num in word:
            if not dp[num]:
                dp[num] = True
                answer.append(num)
                break
    return answer


# print(solution("{{123}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
