class Solution:
    def countSubstrings(self, s: str) -> int:
        # Brute Force
        # cnt = 0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         substr = s[i:j+1]
        #         if substr[::] == substr[::-1]:
        #             cnt += 1
        # return cnt
        res = 0
        for i in range(len(s)):
            l = r = i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res




