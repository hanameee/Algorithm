class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n != 0:
            div, mod = divmod(n, 2)
            answer += mod
            n = div
        return answer
