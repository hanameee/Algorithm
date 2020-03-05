# 스택

리스트로 stack 구현하기

```python
data_stack = list()

def push(data):
    data_stack.append(data)

def pop():
    data = data_stack[-1] # data_stack의 length를 구할필요 없이 index -1로!
    del data_stack[-1]
    return data

for index in range(1,11):
    push(index)

print(data_stack) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pop()
pop()
print(data_stack) # [1, 2, 3, 4, 5, 6, 7, 8]
```



# 