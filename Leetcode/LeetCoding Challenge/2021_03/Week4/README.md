# Week 4

## [Longest Word in Dictionary through Deleting](https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3649/)

이것도 처음에 뭐 알파벳을 키값으로 해서 인덱스를 저장하고 어쩌고... 시간복잡도 줄여보겠다고 한참 이상하게 삽질하고 힌트 슬쩍 보고 다시 풀었다. 😒

일단 Input 조건이 꽤나 빡세다.

```
1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
```

또 문제에서 약간 헷갈리는 부분이 있는데, 여러개 일치할 시 `return the longest word with the smallest lexicographical order ` 에 따라 답을 내야 한다.

[AC 풀이]

```python
s = "abpcplea"
dictionary = ["ale", "apple", "monkey", "plea"]


class Solution:
    def findLongestWord(self, s, dictionary):
        sortedDictionary = sorted(dictionary, key=lambda x: (-len(x), x)) #1
        for word in sortedDictionary:
            s_idx = 0
            flag = True
            for idx, char in enumerate(word):
                if s_idx == len(s):
                    flag = False
                    break
                while s[s_idx] != char:
                    s_idx += 1
                    if s_idx == len(s):
                        flag = False
                        break
                if flag:
                    s_idx += 1
                else:
                    break
            if flag:
                return word
        return ''


solution = Solution()
print(solution.findLongestWord(s, dictionary)
```

1. 주어진 input이 아예 알파벳이든 길이든 랜덤으로 섞여있기 때문에 한번 sorting을 하고 시작했다. 먼저 길이 순으로 정렬 후, 2차로 알파벳 순으로 정렬.
2. 정렬된 word들을 하나씩 돌면서, s와 알파벳 하나씩 비교해본다. 약간 word에 포인터 하나, s에 포인터 하나씩 두고 비교하는 느낌으로다가
   1. s_idx는 현재 word의 문자와 비교하는 대상인 s의 인덱스
   2. flag는 현재 word의 유효성을 체크하는 플래그 > word를 다 돌지 않았는데 s를 다 돌아버리면 s에서 문자를 지워서 w가 될 수 없는 것이므로 해당 word는 유효하지 않음
   3. 1에서 정렬을 해둔 상태이므로 s가 끝나기 전에 word의 char을 성공적으로 다 돌면 (flag=True) 해당 문자열을 바로 return하면 답.

뭔가...코드가 한눈에 안들어오고 좀 지저분하다. 모범 답안 보고 수정 필요.

구글 코딩 질문이었나부다. [요기](https://techdevguide.withgoogle.com/resources/former-interview-question-find-longest-word/)서 다양한 접근법과 해설 볼 수 있다. 🥳 내가 택한 방법은 링크에서의 Greedy Algorithm 정도일 것 같다!