class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Brute force
        res=[-1, -1]
        resLen = - float('infinity')
        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         substr = s[i:j+1]
        #         length = j - i +1
        #         if substr[::] == substr[::-1]:
        #             if length > resLen:
        #                 resLen = length
        #                 res=s[i:j+1]
        # return res
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                winlen = r - l + 1
                if winlen > resLen:
                    resLen = winlen
                    res = s[l:r+1] 
                l -= 1
                r += 1

            l = i
            r = i + 1   
            while l >= 0 and r < len(s) and s[l] == s[r]:
                winlen = r -l + 1
                if winlen > resLen:
                    resLen = winlen
                    res = s[l:r+1] 
                l -= 1
                r += 1
        return res     