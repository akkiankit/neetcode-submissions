class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        leng = max(len(word1), len(word2))
        l = 0
        r = 0
        ans = ""
        while l < leng or r < leng:
            if l < len(word1):
                ans += word1[l]
            if r < len(word2):
                ans += word2[r]

            l += 1
            r += 1
        return ans



        