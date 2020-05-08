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



## 4. 비밀지도

15분컷 ^ㅅ^ 차근차근. 정리해서 풀면 된다.

```python
# 7:49~
def solution(n, arr1, arr2):
    lst1 = []
    lst2 = []
    for i in arr1:
        print(i)
        coded = format(i, "b")
        if len(coded) < n:
            coded = '0'*(n-len(coded)) + coded
        lst1.append(coded)
    for i in arr2:
        coded = format(i, "b")
        if len(coded) < n:
            coded = '0'*(n-len(coded)) + coded
        lst2.append(coded)
    answer = []
    for i in range(n):
        row_str = ""
        for j in range(n):
            if lst1[i][j] == "1" or lst2[i][j] == "1":
                row_str += "#"
            else:
                row_str += " "
        answer.append(row_str)
    return answer


solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
```

앗! **비트 연산**으로 푸는 문제였다고 한다.
둘 중 하나가 1일 경우에 `#` 이 생기므로, OR로 처리하면 간단히 풀 수 있다.

## 방금 그곡

으으... T_T
잘못 생각했다. sliding window에서 걸리지 않으면 (시작 idx + 문자열길이만큼이 parsed_m이랑 같지 않으면) 

```python
def parse_melody(m):
    idx = 0
    lst = []
    acc = ""
    while idx < len(m):
        # 그냥 음이면
        if m[idx] != "#":
            # 전 음이 있었다면
            if acc:
                lst.append(acc)
                acc = ""
        acc += m[idx]
        idx += 1
    if acc:
        lst.append(acc)
    return lst


def solution(m, musicinfos):
    parsed_m = parse_melody(m)
    m_info = []
    # m과 musicinfo를 음단위로 파싱해서 리스트에 넣기
    for info in musicinfos:
        info = info.split(",")
        s_time = int(info[0][:2])*60 + int(info[0][3:])
        e_time = int(info[1][:2])*60 + int(info[1][3:])
        playtime = e_time - s_time
        melody = parse_melody(info[-1])
        m_info.append([playtime, info[2], melody])
    # 음악별로 시간을 이용해 라디오에서 재생된 멜로디 전체를 구성하기
    for info in range(len(m_info)):
        new_melody = []
        for i in range(m_info[info][0]):
            if i >= len(m_info[info][-1]):
                new_melody.append(m_info[info][-1][i % len(m_info[info][-1])])
            else:
                new_melody.append(m_info[info][-1][i])
        m_info[info][-1] = new_melody
    # m과 멜로디들을 비교하기
    ans_lst = []
    for info in range(len(m_info)):
        flag = False
        idx = 0
        while idx+len(parsed_m) <= len(m_info[info][-1]):
            if m_info[info][-1][idx] == parsed_m[0]:
                if m_info[info][-1][idx:idx+len(parsed_m)] == parsed_m:
                    flag = True
                    break
            idx += 1
        if flag:
            ans_lst.append(m_info[info])
    # 일치하면 일치하는 시간을 찾고, 시간도 일치하면 먼저 입력된애를 반환
    if len(ans_lst) == 1:
        return(ans_lst[0][1])
    elif len(ans_lst) == 0:
        return "(None)"
    else:
        ans_lst.sort(key=lambda x: -x[0])

        return(ans_lst[0][1])
```

\#을 소문자로 치환해주는 방법도 있다고! 치환을 생각하자. 나는 배열에 저장했는데, 두 글자로 된 “C#”, “D#”, “F#” 등을 악보에서 사용되지 않는 문자인 “c”, “d”, “e” 등으로 치환하는 방법도 있다고.

이러면 확실히 부분문자열을 발견하기가 더 편할 것 같다. 나처럼 배열에서 부분문자열을 찾아내는 과정에서 idx로 할 필요 없이 바로 in연산을 수행하면 되니까! 흑흑...

1글자 이상의 문자열을 다룰 때 꼭 치환을 생각하기. 3글자짜리를 안쓰는 문자열로 바꾼다던가!