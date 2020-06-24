##  Sherlock and Anagrams

문제를 잘 읽자! ^^
Palindrome 으로 생각하고 풀었는데, 그게 아니라 Anagrams 였다. 훨씬 쉬운 문제를 혼자서 복잡하게 풀었죠?
#### Palindrome 으로 생각하고 푼 풀이
```python
def sherlockAndAnagrams(s):
    answer = 0
    d = {}
    for i in range(len(s)):
        for j in range(i+1, len(s)+1, 1):
            target = s[i:j]
            if target in d:
                d[target] += 1
            else:
                d[target] = 1
    for key in d.keys():
        if key == 0:
            continue
        counter_key = key[::-1]
        dkey = d[key]
        if counter_key == key:
            if dkey >= 2:
                answer += dkey*(dkey-1)//2
                continue
            continue
        if counter_key in d:
            ckey = d[counter_key]
            answer += dkey*ckey
            d[counter_key] = 0
    return answer

```

#### 정답풀이

```python
def sherlockAndAnagrams(s):
    answer = 0
    d = {}
    for i in range(len(s)):
        for j in range(i+1, len(s)+1, 1):
            target = "".join(sorted(list(s[i:j])))
            if target in d:
                d[target] += 1
            else:
                d[target] = 1
    for key in d.keys():
        value = d[key]
        if value >= 2:
            answer += (value)*(value-1)//2
    return answer
```

## Count Triplets

처음에는 "증가하는 수열이여야한다." 는 조건을 제대로 못봐서 그냥 단순히 숫자들을 count 하고, dictionary.keys() 로 하나씩 돌면서 num\*r, num\*r\*r 이 있나 보고, 공비 1일때만 따로 edge case 로 처리해서 풀었다.

그런데 자꾸 틀리는 것임... 그래서 봤더니 세상에 증가하는 수열이여야하지뭐람!

생각을 반대로 해서, loop를 한번만 돌고 num을 볼 때 아래 세 작업을 실시한다.

1. num이 triplet의 마지막 수가 될 수 있는지 본다. count dict에는 중간 수의 가능성이 있는 애들을 저장해두므로 num//r 이 count에 있다면 num은 triplet을 이룰 수 있는 것.
2. num이 triplet의 중간 수가 될 수 있는지를 본다. num/r 이 이전에 나온 적이 있다면 (dict에 존재하고) num이 중간 수가 될 가능성이 있다는 것이므로 num을 count에 추가한다.
3. num을 d에 추가한다.

```python
def countTriplets(arr, r):
    d = {}
    count = {}
    answer = 0
    for num in arr:
        if num % r == 0 and num//r in count:
            answer += count[num//r]
        if num % r == 0 and num//r in d:
            value = d[num//r]
            if num in count:
                count[num] += value
            else:
                count[num] = value
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    return answer
```

이렇게 d와 count 2개의 dict를 관리하면 1을 edge case로 처리할 필요도 없고, 1번의 loop만 돌면 된다. 해커랭크엔 신기한 문제가 많네...

