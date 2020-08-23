class Solution:
    def reverseString(self, s: List[str]) -> None:
        for idx in range(len(s)//2):
            s[idx], s[len(s)-idx-1] = s[len(s)-idx-1], s[idx]
