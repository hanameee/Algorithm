# [Distinct](https://app.codility.com/programmers/lessons/6-sorting/distinct/)

```python
def solution(A):
    return len(set(A))
```

set은 배열을 unique하게 만들어버리지!

# [MaxProductOfThree](https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/)

```python
def solution(A):
    A.sort()
    return max((A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3]))
```

핫하 이정도 훼이크론 어림도 없지!

3개의 product이므로 정렬한 뒤에 단순 제일 큰 3개를 곱하는 것이 아니라, 제일 작은 2개*제일큰거 1개의 곱도 생각해줘야 한다. 음수 2개를 곱한것이 더 커질 수도 있으므로.



# [Triangle](https://app.codility.com/programmers/lessons/6-sorting/triangle/)

```python
def is_triangle(a,b,c):
    if a+b <= c:
        return False
    if b+c <= a:
        return False
    if c+a <= b:
        return False
    return True
        
def solution(A):
    A.sort()
    for idx in range(0,len(A)-2):
        if is_triangle(A[idx],A[idx+1],A[idx+2]):
            return 1
    return 0
```

이것도 좀 수학적인 사고력이 필요한 것 같긴 한데...정렬 후 연속적으로 붙어있는 애가 안되면 떨어져 있는 애는 당연히 될 리가 무방한?

그래서 그냥 정렬 후 하나씩 체크해줬다.

