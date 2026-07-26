class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        countS = {}
        l = 0
        r = 0
        res = 0
        while r < len(s):
            if s[r] in countS:
                l = max(l, countS[s[r]] + 1)
            countS[s[r]] = r
            res = max(res, (r-l+1))
            r += 1
        return res

# loop 1 : a - 0, res = 1
# loop 2 : r = 1, l = 0, a-0, b-1, res - 2
# loop 3: r = 2, l = 0, a-0, l = 2,  a-0, b - 2, res = 2
# loop 4: r = 3, l = 2, l = 1