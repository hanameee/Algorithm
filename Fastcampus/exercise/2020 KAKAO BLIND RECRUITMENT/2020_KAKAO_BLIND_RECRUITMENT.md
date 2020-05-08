# 2020_KAKAO_BLIND RECRUITMENT

## 1. 문자열 압축

푸는데 2시간 조금 안되게 걸렸고, 마지막에 계속 실패한 테스트케이스의 원인을 못찾아서 결국 질문 찾아서 해결했다.

### 문제를 잘 읽자. 제바류...

s가 최대 1000밖에 되지 않으므로, 완전탐색 문제.
접근 방법은 30분 정도 만에 알아냈는데, 구현 과정에서 계속 실수했고 무엇보다 **문제를 잘못 읽었다**. 앞에서부터 순서대로 자른다고 했는데, 압축 불가능한경우에는 idx가 1씩 밀린다고 생각해서 그냥 스스로 복잡도를 높여서 잘못 풀었다.

### 다 정리되고 풀이를 시작해라... 제바류...

수도코드로 정리되고 나서 코드 쓰기.
디버깅 하는 시간이 훨씬 오래 걸린다.



## 2. 괄호 변환

한시간 정도 걸렸다. 

### 재귀는 차근차근 생각하자

재귀를 어려워하는데, 재귀 문제가 나왔네.
다행히 문자열이라서 참조에 대해 생각하지 않아도 되어서 좋았다.

말 그대로 주어진 알고리즘을 그대로 구현하면 되었다. 복잡하게 생각하지 말고 쫄지 말고 구현했으면 좋았을 것 같다.

자잘자잘한 디버깅이 있었는데, 대부분 **변수 명과 인덱스를** 헷갈려서 생긴 실수였다.
이렇게 함수가 길어지는 경우 함수명과 변수명도 조심해서 작성하는 것이 좋겠다.



## 3. 자물쇠와 열쇠

1시간 40분 정도 걸렸다.

- key의 사이즈를 m, lock의 사이즈를 n이라고 할 때 n+2m-2 사이즈의 배열 mp 을 만든 뒤, (m-1,m-1) 을 시작점으로 두고 lock을 입력한다.
- 그리고 일단 key를 4방향으로 회전시키고, 그 모든 key를 가지고 process 함수를 돌린다.
- process 함수는 mp에서 n+m-1미만의 모든 지점에 대해 (n+m-1 부터는 자물쇠에 영향을 주지 않으므로) key를 더한 뒤 is_solved를 체크한다.
- key를 더할 때는 해당 지점이 key의 (0,0) 이 되도록 한 뒤 더한다.
- is_solved는 graph가 있는 부분(m-1, m-1+n)에 대해 모든 지점이 1인지를 체크하고, 아니면 false를 리턴한다.
- key들 중 하나라도 true를 리턴한다면 답은 true, 아니면 false.

키가 상하좌우 이동이 가능하고, 회전도 가능했기에 경우의 수가 너무 많아보였다. 그런데 사실, **key를 회전만 시키고 상하좌우 여백이 있는 graph의 모든 지점을 기준으로 key를 겹치면** 모든 경우에 대해 상하좌우 이동을 한 것과 같은 효과가 난다.

### 2차원 배열 회전시키기

처음에 약간의 삽질을 했는데, 2차원 배열을 회전시키는 코드를 숙지하고 있으면 편할 것 같다.
3번 돌리면 상,하,좌,우 모든 결과를 얻을 수 있으므로

`내 코드 `

```python
def rotate(key):
    new_key = [[0]*len(key[0]) for _ in range(len(key[0]))]
    for i in range(len(key)):
        for j in range(len(key)):
            new_key[j][len(key)-i-1] = key[i][j]
    return new_key
```

[참고 링크](https://shoark7.github.io/programming/algorithm/rotate-2d-array)

### 주어진 그래프보다 더 큰 그래프 만들기

키가 맘대로 움직일 수 있고, 잘려도 상관 없으므로 mp를 원래 lock 사이즈보다 크게 잡으면 된다.



## 4. 가사 검색

1시간 정도 걸렸고, 효율성 테스트 중에 3개 못맞았당.
효율성 테스트를 위해

- length 별로 word를 저장하고
- 접두사/접미사를 이용해보려 했으나 실패.

Trie 자료구조를 사용해야 한다고...😐 쉬익...

#### Trie 자료구조

문자열 검색에 좋은 알고리즘. Trie는 Prefix tree로, 영어사전을 생각해보면 된다.
"hannah"를 찾을 때, "s" 를 찾고, 그 다음 "a"를 찾고...이런 식으로! 자동완성 기능을 구현하려면 리스트로는 택도 없고, 이런 효율적인 자료구조인 Trie가 필요하다.

Trie에서 어떤 문자열을 검색할때의 시간복잡도는 **O(m)** 이며, 문자열 검색에 특화된 자료구조이다.

#### 파이썬에서의 Trie 구현

1. Node 구현
   key는 단어의 글자 하나 하나를 담는 필드
   data는 원래는 마지막 글자를 나타내주는 flag (boolean) 혹은 마지막글자인 경우 단어 전체를 저장 (마지막글자 아니면 null). 이 예제에서는 후자. 왜? starts_with 메서드를 구현하기 위해!

```python
class Node(object):
  def __init__(self, key, data=None):
    self.key = key
    self.data = data
    self.children = {}
```

2. Trie 구현
   - insert(string) : 트라이에 문자열 삽입
   - search(string) : 주어진 단어 string이 트라이에 존재하는지 여부 반환
   - starts_with(prefix) : 주어진 prefix로 시작하는 단어들을 BFS로 트라이에서 찾아 리스트 형태로 반환

```python
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 문자열 삽입 메서드
    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        # 현재 curr_node 는 마지막 글자 - 노드의 data 필드에 저장하려는 문자열 전체를 저장
        curr_node.data = string

    # 문자열 검색 메서드
    def search(self, string):
        curr_node = self.head
        # 글자들에 대해
        for char in string:
            # 계속해서 자식을 타고 내려간다
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        if (curr_node.data != None):
            return True

    # 주어진 prefix로 시작하는 단어들을 찾아 리스트 형태로 반환하는 메서드
    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None
        # trie에서 prefix를 찾는다
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None
        # dfs로 prefix subtrie를 순회하며 data가 있는 노드들을 찾는다
        queue = list(subtrie.children.values())  # 노드들의 리스트
        while queue:
            curr = queue.pop()
            if curr.data != None:
                result.append(curr.data)
            queue += list(curr.children.values())
        return result


def solution(words, queries):
    t = Trie()
    for word in words:
        t.insert(word)
    print(t)


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
         ["fro??", "????o", "fr???", "fro???", "pro?"])
```



## 기둥과 보 설치

나는 map을 만들어두고, 그 map을 build frame을 하나씩 돌면서 완성해나가는 방식으로 했는데 그럴 필요가 없었다.

그냥 result 자체를 list (혹은 set) 로 관리하면 되었다. 구현을 할 때 반드시 N에 맞춰 모든 것을 맞출 필요는 없다는걸 알게 됨. query에 따라 포함시키고, 그 query를 다 돌면서 확인하는 것도 하나의 방법.

```python
from copy import deepcopy


def check_valid(x, y, a, b, bt):
    # 삭제하기
    if b == 0:
        temp_bt = deepcopy(bt)
        temp_bt.pop(bt.index([x, y, a]))
        for x_, y_, a_ in bt:
            if x_ == x and y_ == y and a == a_:
                continue
            if not check_valid(x_, y_, a_, 1, temp_bt):
                return False
            else:
                temp_bt.append([x_, y_, a_])
        return True
    # 설치하기
    else:
        # 보 설치
        if a:
            if [x, y-1, 0] in bt or [x+1, y-1, 0] in bt or ([x-1, y, 1] in bt and [x+1, y, 1] in bt):
                return True
        # 기둥 설치
        else:
            if y == 0 or [x-1, y, 1] in bt or [x, y, 1] in bt or [x, y-1, 0] in bt:
                return True
    return False


def solution(n, build_frame):
    built_frame = []
    # x가 열, y가 행
    for order in build_frame:
        x, y, a, b = order
        if check_valid(x, y, a, b, built_frame):
            if b == 1:
                built_frame.append([x, y, a])
            else:
                built_frame.pop(built_frame.index([x, y, a]))
    answer = built_frame
    answer.sort()
    return answer
```

실수가 잦았는데, 대표적인 실수 포인트는 삭제에서 나왔다. 삭제는 한개를 삭제해본 뒤 나머지 애들이 다 설치 가능한지를 보면 되는데, 순서대로만 체크했던것이 실수 포인트. 삭제는 해당 건물을 짓기 전 명령까지 모두 다 설치한 후, 삭제하는것이기에 순서대로 보면 안되고 모든 칸들을 다 보는 것이 맞다. 

물론 왼/오 보, 아래 기둥 이런 식으로 체크해도 되지만 그럼 경우의수가 너무 많아지니 그냥 지금까지 세운 애들을 다 도는 것이 편하다.

set은 정렬이 안되는 것도 기억.

