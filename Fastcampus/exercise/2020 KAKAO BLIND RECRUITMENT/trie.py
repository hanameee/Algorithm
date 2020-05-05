class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 문자열 삽입 메서드
    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        # 현재 curr_node 는 마지막 글자 - 노드의 data 필드에 저장하려는 문자열 전체를 저장
        curr_node.data = string

    # 문자열 검색 메서드
    def search(self, string):
        curr_node = self.head
        # 글자들에 대해
        for char in string:
            # 계속해서 자식을 타고 내려간다
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        if (curr_node.data != None):
            return True

    # 주어진 prefix로 시작하는 단어들을 찾아 리스트 형태로 반환하는 메서드
    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None
        # trie에서 prefix를 찾는다
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None
        # dfs로 prefix subtrie를 순회하며 data가 있는 노드들을 찾는다
        queue = list(subtrie.children.values())  # 노드들의 리스트
        while queue:
            curr = queue.pop()
            if curr.data != None:
                result.append(curr.data)
            queue += list(curr.children.values())
        return result


def solution(words, queries):
    t = Trie()
    for word in words:
        t.insert(word)
    print(t)


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
         ["fro??", "????o", "fr???", "fro???", "pro?"])
