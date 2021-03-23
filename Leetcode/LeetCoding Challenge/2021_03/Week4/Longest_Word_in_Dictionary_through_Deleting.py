s = "abpcplea"
dictionary = ["ale", "apple", "monkey", "plea"]


class Solution:
    def findLongestWord(self, s, dictionary):
        sortedDictionary = sorted(dictionary, key=lambda x: (-len(x), x))
        for word in sortedDictionary:
            s_idx = 0
            flag = True
            for idx, char in enumerate(word):
                if s_idx == len(s):
                    flag = False
                    break
                while s[s_idx] != char:
                    s_idx += 1
                    if s_idx == len(s):
                        flag = False
                        break
                if flag:
                    s_idx += 1
                else:
                    break
            if flag:
                return word
        return ''


solution = Solution()
print(solution.findLongestWord(s, dictionary)
