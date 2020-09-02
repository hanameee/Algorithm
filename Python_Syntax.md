# Python Syntax

코테 볼 때 알고 있으면 유용한 파이썬 문법 🐝

## List comprehension

List comprehension: 기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문으로, map이나 filter에 람다 식을 섞어서 사용하는 것에 비해 가독성이 좋다.

[예시: 홀수인 경우 2를 곱해 출력하는 리스트]

```python
[n * 2 for n in range(1, 10+1) if n % 2 == 1]
# [2, 6, 10, 14, 18]
```

리스트 외에도 Dictionary Comprehension도 가능하다.

```python
original = {"a":1,"b":2,"c":3,"d":4}
a = {key: value for key, value in original.items()}
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

## Generator

Loop의 반복 동작을 제어할 수 있는 루틴 형태.

```python
# 이 함수는 제너레이터를 리턴한다
def get_natural_number():
  n = 0
  while True:
    n += 1
    yield n

g = get_natural_number()
# 1부터 100까지의 값을 생성할 수 있다
for _ in range(0, 100):
  print(next(g))
```

**range**는 대표적으로 제너테리어 방식을 활용하는 함수이다.

1억개의 자연수를 순차적으로 출력해야 할 때, 1억개의 배열을 담아둔 후 출력하는 것과, range로 출력하는 것과는 메모리 점유율이 엄청나게 차이가 많이 난다.

range는 실제로 생성한 값을 담고 있는 것이 아닌, 생성해야 한다는 조건만 가지고 있다. 하지만 미리 생성하지 않은 값일지라도 인덱스로 접근할 시 바로 생성하게 되어 있어, 리스트와 거의 유사하게 사용할 수 있다.

```python
a = range(100000)
len(a) # 100000
a[999] # 999
```

## Enumerate

enumerate는() 함수는 순서가 있는 자료형(list, set, tuple등)을 인덱스를 포함한 enumerate 객체로 리턴하는 함수다.

```python
a = ["a","b","c","d","e"]
enumerate(a) # <enumerate object at 0x10692c640>
list(enumerate(a)) # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
```

enumerate 객체를 list로 변환해 결과를 추출할 수 있는데, 인덱스를 자동으로 부여해주기 때문에 편리하다.

대표적으로 아래와 같은 방식으로 많이 활용한다.

```python
for idx, value in enumerate(a):
  print(idx, value)
```

## divmod

파이썬에서는 나눗셈과 정수형 내림을 한꺼번에 해주는 연산자 `//` 가 있다. 즉, 몫을 구하는 연산자이다.

나머지를 구하는 모듈로 연산자 `%` 도 있다.

이 둘을 합쳐놓은 함수가 divmod이다. 몫과 나머지를 한꺼번에 구할 수 있다.

```python
divmod(5, 3)
# (1, 2)
```

## print

print() 함수는 기본적으로 공백으로 값을 구분해주며, 항상 줄바꿈을 한다.

```python
print('A1', 'B2')
# A1 B2
```

sep 파라미터로 구분자를 변경해줄 수 있다.

```python
print('A1', 'B2', sep=',')
# A1,B2
```

end 파라미터로 줄바꿈을 하지 않게 만들 수도 있다.

```python
print('aa', end=' ')
print('bb')
# aa bb
```

join함수로 리스트를 출력할 수 있다.

```python
a = ['A', 'B']
print(' '.join(a))
# A B
```

format을 활용해 출력할 수도 있다.

```python
idx = 1
fruit = "Apple"
```

```python
print('{0}: {1}'.format(idx +1, fruit))
# 인덱스를 생략할 수도 있다.
print('{}: {}'.format(idx + 1, fruit))
```

파이썬 3,6+ 에서 지원되는 f-string은 가장 간결하다. 템플릿을 사용하듯 인라인으로 삽입할 수 있어 편리하다.

```python
print(f'{idx + 1}: {fruit})
```

위 3가지 방법은 모두 다 동일한 결과 (`2: Apple`) 를 출력한다.

## locals

locals() 는 로컬 심볼 테이블 딕셔너리를 가져오는 메소드로, 로컬에 선언된 모든 변수(클래스 메소드 내부의 모든 로컬 변수)를 조회할 수 있어 디버깅에 많은 도움이 된다.

이때, pprint를 활용하면 보기 좋게 줄바꿈 처리를 해주기 때문에 가독성이 높다.

```python
import pprint
pprint.pprint(locals())
```

## zip()

zip 함수는 여러 시퀀스에서 **동일한 인덱스의 아이템을 순서대로 추출하여 새로운 튜플 시퀀스**를 만들어준다. 튜플은  immutable 객체이기에 값 조작이 불가능하다.

또, zip 함수 실제 리턴 값은 제너레이터이기에, 값을 추출하기 위해서는 list로 한번 더 묶어줘야 한다.

```python
a = [1,2,3,4,5]
b = [2,3,4,5]
c = [3,4,5]

list(zip(a,b)) # [(1,2),(2,3),(3,4),(4,5)]
list(zip(a,b,c)) # [(1,2,3),(2,3,4),(3,4,5)]
```



## *

파이썬에서 `*` 는 sequence unpacking operator로, 시퀀스를 풀어헤치는 연산자를 뜻한다. 주로 튜플이나 리스트를 언패킹하기 위해 사용한다. 

### 1. zip과 함께 사용

참고 - `Leetcode/11_해시테이블/src/top-k-frequent-elements.py`

```python
list(zip(*collections.Counter(nums).most_common(k)))[0]
```

*없이 `[(1,3),(2,2)]` 를 zip 하면 원치 않은 결과가 나옴. *로 튜플을 리스트로 풀어주고 zip을 적용해야 원하는 결과가 나온다.

### 2. 리스트 출력

```python
a = ["a", "b", "c"]
print(*a) # a b c
```

리스트를 공백으로 분리해 출력할때 간단하게 사용할 수 있는 방법

### 3. 변수의 할당

약간 Javascript의 spread 연산자처럼 활용할 수 있는 것 같다.

`*`는 리스트/튜플 언패킹,

```python
a = [1, 2, 3]
b = [4, 5]
c = [*a, *b]
print(c) # [1, 2, 3, 4, 5]
```

 `**` 는 키/값 페어를 언패킹 하는 데에 사용된다

```python
info = {1:"a",2:"b",3:"c"}
new_info = {**info, 3:"d"} 
print(new_info) # {1: 'a', 2: 'b', 3: 'd'}
```



## 중첩함수

DFS, BFS 처럼 함수 끼리 변수를 공유해야 하는 일이 잦을 때 쓰면 유용한 방법.

자식 함수는 부모 함수의 변수를 자유롭게 읽을 수 있다.

```python
def outer_function(s):
  text = s
  def inner_function():
    print(text)
	inner_function()
  
outer_function("Hello!")
# Hello!
```

다만, 주의할 점이 몇가지 있다.

- 중첩 함수에서는 부모 함수의 가변 객체를 조작할 수 있다. (부모 함수에도 그 조작한 결과가 반영된다) 예를 들어, 자식 함수에서 부모 함수의 리스트를 조작하면, 부모 함수에도 반영된다.
- 하지만 **불변 객체는 조작할 수 없다**. 예를 들어 문자열 같은 경우엔 불변 객체이기에 조작할 수 없다. 값을 변경하려면 재할당 할 수밖에 없고, 이렇게 재할당 한 값은 자식 함수 내에서만 사용 가능한 새로운 로컬변수로 선언되며, 이 재할당된 값은 **부모 함수에서는 반영되지 않는다.**

```python
def outer_function(s):
  text = s
  print(text)
  def inner_function1():
    text = "Bye!"
    print(text)
  def inner_function2():
    print(text)
	inner_function1()
  inner_function2()

outer_function("Hello!")
# Hello! > 부모의 불변객체
# Bye! > 문자열은 조작이 불가능하므로 inner_function1은 자기만의 text 지역변수를 가짐
# Hello! > 부모의 text
```

