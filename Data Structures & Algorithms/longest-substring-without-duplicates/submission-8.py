class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # cnt = 0
        # for i in range(len(s)):
        #     charset = set()
        #     for j in range(i, len(s)):
        #         if s[j] in charset:
        #             break
        #         charset.add(s[j])
        #     cnt = max(cnt, len(charset))
        # return cnt

        # l = 0
        # cnt = 0
        # charSet = set()
        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     cnt = max(cnt, r-l+1)
        # return cnt

        ## Sliding windows
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]]+1, l)
            mp[s[r]] = r
            res = max(res, r-l +1)
        return res


            

                
                    
