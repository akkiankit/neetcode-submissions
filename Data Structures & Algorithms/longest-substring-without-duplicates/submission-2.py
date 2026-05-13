class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # hashmap = set()
        # maxcounter = 0
        # for c in s:
        #     if c in hashmap:
        #         if maxcounter < len(hashmap):
        #             maxcounter = len(hashmap)
        #         hashmap.remove
        #         hashmap.add(c)
        #     else:
        #         hashmap.add(c)
        # return maxcounter
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res




        