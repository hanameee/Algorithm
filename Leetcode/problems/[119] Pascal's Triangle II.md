# [119] Pascal's Triangle II

## Info

### 결과값

| 항목        | 평가                             |
| ----------- | -------------------------------- |
| 통과        | **AC** WA                        |
| 문제 난이도 | **Easy** Medium Hard             |
| 체감 난이도 | **Easy** Medium Hard             |
| 언어        | C C++ Java **Python** Javascript |

## Solving

첫 idx는 무조건 1, 두번째 idx는 무조건 2, 그리고 row[idx]는 row-1[idx-1] + row-1[idx] 임에 착안해서 그냥 정직하게 풀었음. 그랬더니 엄청 느리고 공간복잡도가 높은 답이 나왔다. 쓸데없이 탑다운으로 풀어서 헷갈리기만 하고...

## Source

```python
class Solution(object):
    def getRow(self, rowIndex):
        dp = [[0]*(rowIndex+1) for _ in range(rowIndex+1)]

        def getValue(row, idx):
            if idx == 0 or idx == row:
                return 1
            elif idx == 1 or row-idx == 1:
                return row
            else:
                if not dp[row][idx]:
                    dp[row][idx] = getValue(
                        row-1, idx-1) + getValue(row-1, idx)
                return dp[row][idx]

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            arr = [1, rowIndex]
            for i in range(2, rowIndex+1):
                if i <= (rowIndex//2):
                    arr.append(getValue(rowIndex-1, i-1) +
                               getValue(rowIndex-1, i))
                else:
                    arr.append(arr[rowIndex-i])
            return arr
```

시간복잡도/공간복잡도 차원에서 더 효율적인 알고리즘들을 정리해둔다.

**[row 0부터 차근차근 만들어나가기]**

그냥 Bottom-up으로 0열부터 정직하게 칸을 채워나가는 이 방법이 오히려 2배 이상 빠르다.

prev, curr 2가지 배열을 둬서 curr에서 prev를 참조해 완성해나가는 식.

```python
class Solution(object):
    def getRow(self, rowIndex):
        prev = []
        for i in range(rowIndex+1):
            curr = [0]*(i+1)
            curr[0] = 1
            curr[-1] = 1
            for j in range(1,i):
                curr[j] = prev[j-1]+prev[j]
            prev = list(curr)
        return curr
```

**[2차원 배열로 관리하기]**

이것도 마찬가지로 Bottom-up으로 1열부터 채워나가는 방식인데 얘는 위와는 다르게 output을 2차원 배열에 저장한다.

왠지 모르겠는데 시간은 이게 제일 짧다.

```python
class Solution(object):
    def getRow(self, rowIndex):
        output = []
        output.append([1])
        for i in range(1, rowIndex + 1): 
            output.append([])
            output[i].append(1)
            for j in range(1, i + 1): 
                if j == i: 
                    output[i].append(1)
                else: 
                    output[i].append(output[i - 1][j - 1] + output[i - 1][j])
        
        return output[rowIndex]
        
```

