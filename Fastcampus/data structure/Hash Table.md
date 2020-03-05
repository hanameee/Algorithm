# Hash Table

### Hash Table: 키(Key)에 데이터(Value)를 저장하는 데이터 구조

- 파이썬 **딕셔너리(Dictionary) 타입**이 해쉬 테이블의 예: Key를 가지고 바로 데이터(Value)를 꺼냄

### Chaining 기법 (list 활용)으로 충돌 문제를 해결한 Hash Table 구현
```python
# list comprehension 문법
hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

# data와 value를 넣으면, 해당 data에 대한 key를 찾아서 해당 key에 대응하는 해쉬주소에 value를 저장하는 예시
# list를 이용한 chaining 기법으로 충돌 문제 해결하기
def store_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        # 해당 해쉬 주소에 기존에 존재하던 list 탐색
        for index in range(len(hash_table[hash_address])):
            # index_key 값과 일치하는 슬롯이 존재한다면
            if hash_table[hash_address][index][0] == index_key:
                # value 값을 업데이트 해주기
                hash_table[hash_address][index][1] = value
                return
        # 기존 존재하던 list에 index_key 값과 일치하는 슬롯이 없다면 append로 새로운 슬롯을 만들어주기
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None

store_data("hannah",'01040743188')
store_data("jeongho",'01077994427')
store_data("john", "01012341234")
read_data("john")
print(hash_table)

```

### Linear probing 기법으로 충돌 문제를 해결한 Hash Table 구현

```python
hash_table = list([0 for index in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key%8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    # 해당 주소에 데이터가 있다면
    if hash_table[hash_address] != 0:
        # 해당 주소부터 순회하며 다음 슬롯들을 탐색한다
        for index in range(hash_address, len(hash_table)):
            # 슬롯에 저장된 값이 없다면 저장
            if hash_table[index] == 0:
                hash_table[index] == [index_key, value]
                return
            # 슬롯에 저장된 데이터의 키가 현재 추가할 키와 동일하면 값만 업데이트
            elif hash_table[index][0] == index_key:
                hash_table[index][1] == value
                return
    else:
        hash_table[hash_address] = [index_key,value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index][0] == index_key:
                return hash_table[index][1]
            # 빈 공간이 있다는 것은 해당 data가 저장된 적이 없다는 뜻
            elif hash_table[index] == 0:
                return None
    else:
        return
```

### 해쉬 함수 사용하기

```python
import hashlib

hash_object = hashlib.sha256()
hash_object.update(b'test')
hex_dig = hash_object.hexdigest()
print(hex_dig)
```

### 해쉬 함수 사용해서 Linear probing 기법의 Hash Table 구현하기

(get_key 를 제외하면 나머지 함수는 동일)

```python
import hashlib


hash_table = list([0 for index in range(8)])

def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    # 해당 주소에 데이터가 있다면
    if hash_table[hash_address] != 0:
        # 해당 주소부터 순회하며 다음 슬롯들을 탐색한다
        for index in range(hash_address, len(hash_table)):
            # 슬롯에 저장된 값이 없다면 저장
            if hash_table[index] == 0:
                hash_table[index] == [index_key, value]
                return
            # 슬롯에 저장된 데이터의 키가 현재 추가할 키와 동일하면 값만 업데이트
            elif hash_table[index][0] == index_key:
                hash_table[index][1] == value
                return
    else:
        hash_table[hash_address] = [index_key,value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index][0] == index_key:
                return hash_table[index][1]
            # 빈 공간이 있다는 것은 해당 data가 저장된 적이 없다는 뜻
            elif hash_table[index] == 0:
                return None
    else:
        return

# 테스트
save_data('aa','123')
save_data('ab','456')
save_data('ac','789')
print(read_data('aa'))
print(read_data('ab'))
print(read_data('ac'))
```

