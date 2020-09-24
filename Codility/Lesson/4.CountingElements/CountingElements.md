# FrogRiverOne

```python
def solution(X, A):
    s = set([])
    for i in range(len(A)):
        s.add(A[i])
        if len(s) == X:
            return i
    return -1
```

set을 쓰면 되겠다 싶었다.

배열 A에 있는 값들이 X의 범위 안에 있다는 제한 조건이 있으므로, set에 있는 unique한 원소들의 갯수가 X개가 되면 이는 X까지의 숫자가 다 나왔다는것.

단, 마지막까지 리턴이 안된다면 이는 불가능하다는 얘기이므로 -1을 리턴해줘야 한다.

불가능한 인풋이 주어지는지, 그렇다면 뭘로 예외처리를 해야하는지 문제를 잘 읽자.

# [MaxCounters](https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/)
```python
def solution(N, A):
    arr = [0]*N
    max_num = 0
    base_limit = 0
    for i in A:
      	#(1)
        if i == N+1:
            base_limit = max_num
        else:
          	#(2)
            if arr[i-1] < base_limit:
                arr[i-1] = base_limit
            #(3)
            arr[i-1] += 1
            #(4)
            if arr[i-1] > max_num:
                max_num = arr[i-1]
    for i in range(len(arr)):
        if arr[i] < base_limit:
            arr[i] = base_limit
    return arr
```
으으으 한 단계 더 어려운 문제라고 효율성 되게 빡빡하다.
계속 마지막 테케에서 timeout이 나서 결국 해설 찾아봤다.
### 타임아웃 난 코드
```python
def solution(N, A):
    arr = [0]*N
    max_num = 0
    add_num = 0
    for i in A:
        if i == N+1:
            add_num += max_num
            max_num = 0
            arr = [0]*N # 실수한 부분
        else:
            arr[i-1] += 1
            if arr[i-1] > max_num:
                max_num = arr[i-1]
    return [i+add_num for i in arr]
```
A[x] = N+1 일때 모든 배열이 최댓값으로 업데이트 해야한다. input이 100,000까지 들어오기 때문에 당연히 모든 배열을 실제로 업데이트하면 타임아웃이다.
N+1일때마다 배열의 최댓값을 트래킹해야하고, 이를 위해서는 O(n)으로 돌면서 max_num 변수만 관리해주면 된다.
내가 실수한 부분은, N+1일때마다 arr을 초기화해주는 부분이었던 것 같다. 채점 시 ac받는 코드와 동일한 시간복잡도인 O(N+M) 이 나오긴 하지만, 마지막 테케에서 timeout 되는 것을 보면 배열을 새롭게 할당해주는 것이 오버헤드가 있나보다.
배열을 초기화해주는 것이 아니라, 앞서 말한 로직대로 max_num을 계속 쌓아가되 (1) N+1을 만나면 최저값(base_limit)을 max_num으로 업데이트 해준다.
N+1이 아닌 transaction을 만났을 때는 (2)현재 값이 최저값보다 작은지를 체크한 후 작다면 최저값으로 설정해준다. 그리고 나서 (3)1을 더하고, (4)max_num보다 큰 지 확인한 후 업데이트 해준다.
조심할 부분은 2가지 정도가 있다
1. base_limit과 max_num은 다르다. 따라서 (4)번에서 반드시 max_num보다 큰지 확인하는 과정이 필요하다. base_limit은 마지막으로 N+1이 나왔을 시점의 max_num이고, max_num은 그 이후에도 쭉쭉 높아질 수 있다.
2. 마지막에도 한바퀴 loop를 돌아야 한다. 마지막으로 N+1이 나온 이후에 등장하지 않은 값들은 base_num으로 업데이트 될 기회가 없었기 때문이다. 최저값 이하의 애들을 다 최저값까지 끌어올려주는 과정이 필요하다.

# MissingInteger

```python
def solution(A):
    A.sort()
    try:
        start_idx = A.index(1)
    except ValueError:
        return 1
    for i in range(start_idx+1, len(A)):
        if A[i] > A[i-1]+1:
            return A[i-1]+1
    return A[-1]+1
```

음? 쉽다?

Detected time complexity: O(N) or O(N * log(N)) 로 나왔다.

처음에는 set에 넣을까...했는데 set은 index가 안되더라. 그냥 쭉 돌면서 확인해주면 됨.

순서대로 정렬 후, 어떤 원소가 이전 원소+1보다 크다면 한칸 건너뛴것. 따라서 그 건너뛴 값을 리턴.

마지막까지 리턴되지 않았다면 건너뛴 원소가 없는 것. 따라서 끝값+1 리턴.

주의할 점) set은 인덱스로 접근도 안되고, sort도 안된다. list로 변환하고 하기.


# PermCheck

```pythonㄷ
def solution(A):
    A = sorted(list(set(A)))
    if A[-1]-A[0] == len(A)-1:
        return 1
    else:
        return 0
```

음? 실수 많이 했다?

솔직히 문제가 좀 헷갈린다... :)


