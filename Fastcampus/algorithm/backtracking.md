# 백트래킹 (Backtracking)

## 1. 백트래킹이란?

백트래킹은 알고리즘은 아니고, 일종의 문제를 푸는 기법이다. (분할정복, 탐욕알고리즘과 유사하게 "기법" 임)
**제약 조건 만족 문제** (Constraint Satisfaction Problem) 에서 해를 찾기 위한 전략으로 사용된다.

해를 찾기 위해 후보군들에 대해 제약 조건을 점진적으로 체크하다가, 해당 후보군이 제약 조건을 만족할 수 없다고 판단되는 즉시 backtrack (다시는 이 후보군을 체크하지 않을 것을 표기)하고, 바로 다른 후보군으로 넘어가는 방식으로 최적의 해를 찾는 방법.

실제 구현 시, 고려할 수 있는 모든 경우의 수(**후보군**)를 상태공간**트리** (State Space Tree) 를 통해 표현한다.

각 후보군을 **DFS 방식**으로 확인한다.

상태 공간 트리를 탐색하면서, 제약조건에 맞지 않으면 즉시 해의 후보가 될만한 곳으로 바로 넘어가서 (backtrack) 탐색한다.

- Promising: 해당 루트가 조건에 맞는지를 검사하는 기법
- Pruning (가지치기): 조건에 맞지 않으면 포기하고 다른 루트로 바로 돌아서서, 탐색시간을 절약하는 기법

정리하자면, 백트래킹은 트리 구조를 기반으로 DFS 방식으로 탐색하며, 각 노드가 조건에 부합하는지 체크(Promising)하고, 만약 조건에 맞지않는다면 노드는 더 이상 DFS를 진행하지 않고 가지를 친다 (Pruning). 이러한 방식으로 후보군들 중 제약조건을 만족하는 최적의 해를 찾는다.

## 2. 백트래킹의 대표적 예시 - N Queen 문제

NxN 크기의 체스판에 N개의 퀸을 서로 공격할 수 없도록 배치하는 문제

### Pruning (가지치기) for N Queen

- 한 행에는 하나의 퀸 밖에 위치할 수 없음 (퀸은 수평 이동이 가능하므로)
- 맨 위에 있는 행부터 퀸을 배치하고, 다음 행에 해당 퀸이 이동할 수 없는 위치를 찾아 퀸을 배치
- 만약 앞선 행에 배치한 퀸으로 인해, 다음 행에 해당 퀸들이 이동할 수 없는 위치가 없을 경우에는, 더 이상 퀸을 배치하지 않고, 이전 행의 퀸의 배치를 바꿈
  - 즉, 맨 위의 행부터 전체 행까지 퀸의 배치가 가능한 경우의 수를 상태 공간 트리 형태로 만든 후, 각 경우를 맨 위의 행부터 DFS 방식으로 접근, 해당 경우가 진행이 어려울 경우, 더 이상 진행하지 않고, 다른 경우를 체크

### Promising for N Queen

- 해당 루트가 조건에 맞는지를 검사하는 기법을 활용하여,
- 현재까지 앞선 행에서 배치한 퀸이 이동할 수 없는 위치가 있는지를 다음과 같은 조건으로 확인
  - 한 행에 어차피 하나의 퀸만 배치 가능하므로 수평 체크는 별도로 필요하지 않음

**1) 수직 체크**

current 위치와 queen 위치의 열 값이 같으면 이동할 수 없다. (같은 수직선상에 위치)
current_col - queen_col = 0

**2) 대각선 체크**

current_row - queen_row = abs(current_col - queen_col)
queen row는 항상 맨 윗줄에서 시작하기에 current_row 의 값이 무조건 queen_row 보다 크지만, current_col은 queen col 보다 왼쪽에 있을 수도, 오른쪽에 있을 수도 있기 때문에 절댓값(abs)을 씌워주어야 한다.

 ## 3. N Queen 풀이 코드 작성

Tree 형태로 후보군을 구성하고, DFS를 돌면서 조건을 탐색하고, 조건에 맞지 않으면 가지치기 한다. (실제로 트리를 만드는 것은 아니고, 컨셉 상 그렇다는 것)

```python
def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True  # 기존 candidate 퀸 위치와 조건을 비교했을 때 아무 문제가 없다면 그 위치에 놓ㅇ르 수 있다는 것


def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:  # 배치가 다 끝났다면
        final_result.append(current_candidate[:])  # 얇은 복사
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row+1, current_candidate, final_result)
            current_candidate.pop()  # pruning


def solve_n_queens(N):
    final_result = list()  # 최종 배치도는 리스트 형태로 저장
    DFS(N, 0, [], final_result)  # 초기 값은 아직 아무 퀸도 배치되지 않았으므로
    return final_result


print(solve_n_queens(4))
```

