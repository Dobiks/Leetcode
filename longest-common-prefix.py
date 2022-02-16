class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix = ""
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            letter = set()
            for word in strs:
                letter.add(word[i])
            if len(letter)==1:
                prefix += word[i]
            else:
                return prefix
        return prefix
                


