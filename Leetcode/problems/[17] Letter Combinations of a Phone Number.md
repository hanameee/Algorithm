# [17] Letter Combinations of a Phone Number

## Info

### 결과값

| 항목        | 평가                             |
| ----------- | -------------------------------- |
| 통과        | **AC** WA                        |
| 문제 난이도 | Easy **Medium** Hard             |
| 체감 난이도 | **Easy** Medium Hard             |
| 언어        | C C++ Java **Python** Javascript |

## Solving

기본적인 DFS로 풀었음.

## Source

```python
class Solution(object):
    def letterCombinations(self, digits):
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        answer_arr = []

        if digits == "":
            return answer_arr

        def dfs(v, buf):
            buf += v
            if len(buf) == len(digits):
                answer_arr.append(buf)
                return
            for child in dic[digits[len(buf)]]:
                dfs(child, buf)

        for num in dic[digits[0]]:
            dfs(num, "")
        return answer_arr
```

**[백트래킹]**

백트래킹으로 풀 수도 있다. 문자열 조작과 배열 조작의 시간 차이인지는 모르겠지만...이 방법이 제일 빠르다.

```python
class Solution(object):
    def letterCombinations(self, digits):
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        answer_arr = []

        if digits == "":
            return answer_arr

        def backtrack(idx, path):
            if len(path) == len(digits):
              answer_arr.append(''.join(path))
              return
            adj_letters = dic[digits[idx]]
            for letter in adj_letters:
              path.append(letter)
              backtrack(idx+1, path)
              path.pop

        backtrack(0, [])
        return answer_arr
```



