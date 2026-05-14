class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Brute force
        res=[-1, -1]
        resLen = - float('infinity')
        for i in range(len(s)):
            for j in range(len(s)):
                substr = s[i:j+1]
                length = j - i +1
                if substr[::] == substr[::-1]:
                    if length > resLen:
                        resLen = length
                        res=s[i:j+1]
        return res
        