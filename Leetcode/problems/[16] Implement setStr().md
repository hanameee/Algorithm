# [28] Implement setStr()

## Info

### 결과값

| 항목        | 평가                                                         |
| ----------- | ------------------------------------------------------------ |
| 통과        | **AC** WA                                                    |
| 문제 난이도 | **Easy** Medium Hard                                         |
| 체감 난이도 | **Easy** Medium Hard                                         |
| 언어        | C C++ Java **Python** Javascript                             |
| 해결 시간   | 약 15분                                                      |
| 시간복잡도  | O(N*M) - N은 텍스트(haystack)의 길이, M은 패턴(needle)의 길이 |

## Result

<img src="image-20210411175628344.png" alt="image-20210411175628344" style="zoom:50%;" />

## Solving

- needle이 0이거나 haystack == needle인 경우 `0`
- haystack이 0이거나, haystack보다 needle이 길 경우 `-1`
- 그 외에는 haystack을 앞에서부터 돌면서 needle의 첫글자와 일치할 경우 needle을 포함하는지 체크. 포함하면 early return
- 못찾으면 `-1`

## Source

```python
class Solution(object):
    def strStr(self, haystack, needle):
        Lhaystack = len(haystack)
        Lneedle = len(needle)
        if Lneedle == 0 or haystack == needle:
            return 0
        if Lhaystack == 0 or Lhaystack < Lneedle:
            return -1
        for idx in range(Lhaystack-Lneedle+1):
            if haystack[idx] == needle[0]:
                if haystack[idx:idx+Lneedle] == needle:
                    return idx
        return -1
```

풀고 나서 보니 궂이 필요 없는 예외처리가 들어간 것 같다.

## 다른 풀이들

### 예외 처리 필요 없는 풀이

```python
class Solution(object):
    def strStr(self, haystack, needle):
        N = len(needle)
        for i in range(len(haystack) - N+1):
            if haystack[i:i+N] == needle:
                return i
        return -1
```

needle의 첫글자와 일치하는 경우를 체크하지 않고, 바로 체크할 경우 예외처리가 필요 없어짐. (`needle[0]` 에 접근할  필요가 없어서) 속도도 20 -> 8ms로 빨라짐.

length를 미리 저장해놓고 재사용하는 것도 시간복잡도 줄이는 것에 도움이 됨.

### KMP 알고리즘

KMP 알고리즘은 O(NM)보다 빠른 O(N+M)의 시간복잡도를 가진다.

KMP 알고리즘은 찾고자 하는 문자열 패턴을 전처리해 (PI배열 또는 lps배열) 빠른 검색을 가능하게 한 알고리즘이다.

```python
class KMP:
    # PI 배열 구하는 함수 (pattern 전처리)
    def computePI(self, pattern):
        pi = [0]
        for i in range(1, len(pattern)):
            j = pi[i-1]
            while j > 0 and pattern[j] != pattern[i]:
                j = pi[j-1]
            pi.append(j + 1 if pattern[j] == pattern[i] else j)
        return pi
    # PI 배열을 사용해 T에서 P가 등장하는 idx를 모두 구하는 함수
    def search(self, T, P):
        pi, ans, j = self.computePI(P), [], 0
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = pi[j-1]
            if T[i] == P[j]:
                if (j == len(P)-1):
                    ans.append(i-(len(P)-1))
                    j = pi[j]
                else:
                    j += 1
        return ans


kmp = KMP()
print(kmp.search("ABCABCABC", "ABC"))
```



