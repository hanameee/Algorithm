# 자료구조

## 1. 배열

파이썬에서는 **리스트 타입**이 배열 기능을 제공

- 배열의 장점:
  - 빠른 접근 가능

- 배열의 단점 :
  - 추가/삭제가 쉽지 않음
  - 미리 최대 길이를 지정해야 함 

## 2. 파이썬과 C언어의 배열 예제

`C`

```c
#include <stdio.h>

int main(int argc, char * argv[])
{
    char country[3] = "US";
    printf("%c%c\n", country[0], country[1]);
    printf("%s\n", country);
    return 0;
}
```

`python`

```python
country = 'US'
print(country)

country = country + 'A'
print(country)
```

