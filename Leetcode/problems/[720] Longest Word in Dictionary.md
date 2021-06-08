# [720] Longest Word in Dictionary

## Info

### 결과값

| 항목        | 평가                             |
| ----------- | -------------------------------- |
| 통과        | **AC** WA                        |
| 문제 난이도 | **Easy** Medium Hard             |
| 체감 난이도 | Easy **Medium** Hard             |
| 언어        | C C++ Java **Python** Javascript |
| 해결 시간   | 약 30분                          |
| 시간복잡도  | ?                                |

## Result

![720](720.png)

## Solving

Trie 문제란걸 알고 있어서, Trie 구현 방법을 찾아보면서 풀었다.

맞긴 맞았는데, 지금은 알파벳 순 + 순서 순으로 정렬을 해서 넣어줘야지만 답이 올바르게 나온다. 시간복잡도랑 공간복잡도가 많이 높은걸 봐서 이게 뭔가 잘못 푼 포인트인것 같다.

다른 답안들도 찾아봐야겠다.

## Source

```python
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)
        self.longest = ""

    def insert(self, string):
        current_node = self.head
        for i, char in enumerate(string):
            if char not in current_node.children:
                if i != len(string) - 1:
                    return
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string
        if len(self.longest) < len(string):
            self.longest = string


class Solution(object):
    def longestWord(self, words):
        sortedWords = sorted(words, key=lambda word: (len(word), word))
        trie = Trie()
        for word in sortedWords:
            trie.insert(word)
        return trie.longest
```