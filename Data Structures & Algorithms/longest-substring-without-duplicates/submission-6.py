class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            charset = set()
            for j in range(i, len(s)):
                if s[j] in charset:
                    break
                charset.add(s[j])
            cnt = max(cnt, len(charset))
        return cnt
                
                    
