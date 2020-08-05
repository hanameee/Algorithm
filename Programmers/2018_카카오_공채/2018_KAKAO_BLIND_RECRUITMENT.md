# 2018 KAKAO BLIND RECRUITMENT



## 1. 뉴스 클러스터링

또또또또 한시간이나 삽질했쥬? 문제를 잘못 읽었다.
**중복을 허용하는 다중 집합** 에 확장해서 사용하는건데! 그냥 단순히 셌다. 그라믄 안된다.

```python
# 10:55~
from string import ascii_lowercase
alpha_list = ascii_lowercase


def filter_alpha_lst(lst):
    new_list = []
    for e in lst:
        flag = True
        for char in e:
            if char not in alpha_list:
                flag = False
        if not flag:
            continue
        new_list.append(e)
    return new_list


def get_alpha_lst(a):
    lst = []
    for i in range(len(a)-1):
        lst.append(a[i]+a[i+1])
    return lst


def compare(a_lst, b_lst):
    count = 0
    sum_count = 0
    dup_count = 0
    a_set = set(a_lst)
    len_a = len(a_lst)
    len_b = len(b_lst)
    for e in a_set:
        count_a = a_lst.count(e)
        count_b = b_lst.count(e)
        # 다중 중복요소라면
        if count_a >= 1 and count_b >= 1:
            sum_count += max(count_a, count_b)
            dup_count += min(count_a, count_b)
            len_a -= count_a
            len_b -= count_b
        # 일반 요소라면
    return (dup_count, sum_count + len_a + len_b)

    dup_count += 1
    if e in b_lst:
        count += 1
    return count


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    lst1 = get_alpha_lst(str1)
    lst1 = filter_alpha_lst(lst1)
    lst2 = get_alpha_lst(str2)
    lst2 = filter_alpha_lst(lst2)
    dup_c, sum_c = compare(lst1, lst2)
    if sum_c == 0:
        jkd = 1
    else:
        jkd = dup_c / sum_c
    answer = int(jkd*65536)
    return answer


print(solution("aa1+aa2	", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
```

1) 유효한 원소들로만 필터링
2) 교집합을 구하고, 합집합을 구한다.

Counter을 사용하면 좀 더 편하게 구할 수 있는 것 같다.



## 2. 캐시

재밌는 문제. cache를 어떤걸 써야 하나 고민했는데 cache 사이즈가 컸으면 heapq나 deque를 고민했겠지만 제한이 30으로 작아서 그냥 list 썼다.

```python
def is_in_cache(cache, city):
    for idx in range(len(cache)):
        if cache[idx][1] == city:
            return idx
    else:
        return -1


def solution(cacheSize, cities):
    cache = []
    time = 0
    if not cacheSize:
        return len(cities)*5
    # cities 하나하나 본다
    for city in cities:
        result = is_in_cache(cache, city.lower())
        # 캐시에 있다면
        if result != -1:
            time += 1  # hit
            # 최근 사용 업데이트
            for c in cache:
                c[0] += 1
            cache[result][0] = 0
        # 캐시에 없다면
        else:
            time += 5  # miss
            # 캐시가 비었다면
            if len(cache) < cacheSize:
                for c in cache:
                    c[0] += 1
                # 추가해주기
                cache.append([0, city.lower()])
            # 캐시가 꽉 차있다면 LRU 삭제하고 추가해주기
            else:
                cache.sort(key=lambda x: x[0])
                cache.pop()
                for c in cache:
                    c[0] += 1
                cache.append([0, city.lower()])
    answer = time
    return time


print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                   "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
```



## 3. 프렌즈4블록

dropdown을 하면서 좌표가 바뀌기 때문에 done 좌표를 저장하는 것은 불필요하다. 쓰잘데기 없는 변수 추가해서 1시간 걸림.

주어진대로 구현하면 된다. 뿌요뿌요랑 비슷. 인형뽑기의 조금 더 어려운 버전?
이런 문제는 어떤 상태들을 관리해야 할 지 미리 잘 정의해두고 가면 좋을 것 같다.



---

# [3차]

## 파일명 정렬
`python 코드`

```python
def solution(files):
    file_arr = []
    for file in files:
        result = [file]
        cur_idx = 0
        head_idx = 0
        num_idx = 0
        for idx in range(0, len(file)):
            if 48 <= ord(file[idx]) <= 57:
                cur_idx = idx
                head_idx = idx
                break
        result.append(file[0:cur_idx].lower())
        for idx in range(head_idx, len(file)):
            cur_idx = idx + 1
            if ord(file[idx]) < 48 or ord(file[idx]) > 57:
                cur_idx = idx
                num_idx = idx
                break
            if int(file[head_idx:idx+1]) > 99999:
                cur_idx = idx
                num_idx = idx
                break
        result.append(int(file[head_idx:cur_idx]))
        file_arr.append(result)
    file_arr.sort(key=lambda x: [x[1], x[2]])
    result = []
    for sortedFile in file_arr:
        result.append(sortedFile[0])
    return result
```

프로그래머스 Level2라서 만만하게 봤는데, 생각보다 헷갈렸다.

1. files 문자열에서, 숫자인 문자열과, 문자인 문자열을 구분해내야 한다. 나는 파이썬의 `ord` 를 이용했다. 주의할 점은, 특수부호 (" ", ".", "-") 도 들어오기 때문에 `ord` 의 범위를 신경써서 잡아줘야 한다.
2. TAIL 부분은 사실상 필요하지 않다. HEAD와 NUMBER만 잘 구분해내면 된다.
3. NUMBER에 범위 제약이 있다. (0~99999) 또, 앞쪽에 0도 올 수 있다. 00011, 100000 등의 케이스를 어떻게 처리할지 고민해봐야 한다.
4. 파이썬의 기본 `.sort` 알고리즘은 **안정 정렬 (stable sort)** 이다. 따라서 Lambda 의 key를 sort function으로 정의해서 단순히 비교만 해주면 문제의 조건을 충족할 수 있다.

그 밖에도 대소문자, index 등등 신경써야 할 것이 많았던 문제였다.

내 로직은 아래와 같다.

```pseudocode
file_arr = []
for files의 모든 file:
	result = [file] # [원래파일명, HEAD, NUMBER] 으로 필터링해 담아두기 위한 배열
	for char in file[0부터 끝까지]:
		if char이 숫자라면:
			break
	result.append(HEAD부분)
	for char in file[HEAD이후부터 끝까지]:
		if 숫자가 아니라면:
			break
		if 숫자가 99999 초과라면:
			break
	result.append(NUMBER부분)
	file_arr.append(result) # 필터한 결과를 file_arr에 담기
file_arr.sort(key는 HEAD, NUMBER 순)
result = []
for sortedFile in file_arr:
	result.append(원래파일명)
return result
```

느긋하게 풀었다지만 디버깅까지 포함하면 거의 1시간 동안 잡고 있었다. 이런 문제는 빨리 풀 수 있도록 속도를 늘려야 한다. 힝구