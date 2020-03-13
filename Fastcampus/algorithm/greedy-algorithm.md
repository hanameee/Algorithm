# 탐욕 알고리즘 (Greedy algorithm)

## 1. 탐욕 알고리즘이란?

- 최적의 해에 가까운 값을 구하기 위해 사용됨
- 여러 경우 중 하나를 결정해야할 때마다, (여러 조합을 생각하지 않고) **매순간 최적이라고 생각되는 경우를 선택**하는 방식으로 진행해서, 최종적인 값을 구하는 방식

## 2. 탐욕 알고리즘의 예시

### 1. 동전 문제

>  지불해야 하는 값이 4720원 일 때 1원 50원 100원, 500원 동전으로 동전의 수가 가장 적게 지불하시오.

```python
coin_list = [1, 50, 100, 500]


def min_coin_count(value, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)  # 내림차순으로 정렬
    for coin in coin_list:
        coin_num = value // coin # 가장 큰 동전단위로 몫 계산
        total_coin_count += coin_num  # 몫 만큼 coin count 증가
        value -= coin_num * coin # 지불한 만큼 value 차감
        details.append([coin, coin_num]) # 어떤 종류의 동전이 몇개 쓰였는지 기록
    return total_coin_count, details


print(min_coin_count(4720, coin_list))
```

Q. 이게 왜 탐욕 알고리즘인가?
A. 매 순간 최적이라고 생각되는 경우를 선택하고 (가장 큰 동전 단위) 다른 조합은 고려하지 않았기 때문.

### 2. 부분 배낭 문제 (Fractional Knapsack Problem)

**무게 제한이 k인 배낭에 최대 가치를 가지도록** 물건을 넣는 문제

- 각 물건은 무게(w)와 가치(v)로 표현될 수 있음
- 물건은 쪼갤 수 있으므로 물건의 일부분이 배낭에 넣어질 수 있음, 그래서 Fractional Knapsack Problem 으로 부름
  - Fractional Knapsack Problem 의 반대로 물건을 쪼개서 넣을 수 없는 배낭 문제도 존재함 (0/1 Knapsack Problem 으로 부름)

```python
# 튜플로 표현 (w,v)
data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]
data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]


def get_max_value(data_list, capacity):
    # data_list 를 무게 단위 당 가치로 내림차순 정렬 해서 새로운 리스트로 반환
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    details = list()

    for data in data_list:
        # data의 무게가 capacity를 넘지 않는다면
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        # data의 무게가 capacity를 넘으면
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            # 이미 용량이 다 찼으니 다음 물건이 남았더라도 볼 필요가 없음
            break
    return total_value, details


print(get_max_value(data_list, 27))
```

## 3. 탐욕 알고리즘의 한계

- 탐욕 알고리즘은 반드시 최적의 해를 guarantee 하는 것은 아니기에, **근사치 추정**에 활용한다
- 최적의 해에 가까운 값을 구하는 방법 중의 하나임

## 4. Lesson Learned

Lambda 표현식 익히기 [링크](https://dojang.io/mod/page/view.php?id=2359)

