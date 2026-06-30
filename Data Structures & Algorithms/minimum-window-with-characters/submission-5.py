class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        if t == "": return ""

        countT = {}
        for c in t:
            countT[c] = countT.get(c,0) + 1
        
        res, resLen = [-1,-1], float('infinity')
        has, need = 0, len(countT)
        windowsT = {}
        left = 0
        for right in range(len(s)):
            ch = s[right]
            windowsT[ch] = windowsT.get(ch,0) + 1
            if ch in countT and countT[ch] == windowsT[ch]:
                has += 1
            while has == need:
                if (right - left + 1) < resLen:
                    resLen = right - left + 1
                    res = [left, right]
                
                # update left
                windowsT[s[left]] -= 1
                if s[left] in countT and windowsT[s[left]] < countT[s[left]]:
                    has -= 1
                left += 1

        # for i in range(len(s)):
        #     countS= {}
        #     for j in range(i,len(s)):
        #         countS[s[j]] = 1 + countS.get(s[j], 0)
        #         flag = True
        #         for c in countT:
        #             if countT[c] > countS.get(c,0):
        #                 flag = False
        #                 break
        #         if flag and (j-i+1) < resLen:
        #             resLen = j - i + 1
        #             res = [i,j]
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""
        