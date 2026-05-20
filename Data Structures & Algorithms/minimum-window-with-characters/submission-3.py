class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        res = [-1, -1]
        min_length = float('infinity')
        countT= {}
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        
        # for i in range(len(s)):
        #     countS = {}
        #     for j in range(i, len(s)):
        #         curC = s[j]
        #         countS[curC] = 1 + countS.get(curC, 0)

        #         flag = True
        #         for c in countT:
        #             if countT[c] > countS.get(c,0):
        #                 flag = False
        #                 break
                
        #         if flag and (j-i+1) < min_length:
        #             min_length = j - i + 1
        #             res = [i,j]
        # l, r = res
        # return s[l:r +1] if min_length != float('infinity') else ""

        need = len(countT)
        have = 0
        l = 0
        windows={}
        for r in range(len(s)):
            c = s[r]
            windows[c] = 1 + windows.get(c,0)
            if c in countT and countT[c] == windows[c]:
                have += 1
            while have == need:
                curlen = r - l + 1
                if min_length > curlen:
                    min_length = curlen
                    res = [l, r]

                windows[s[l]] -= 1
                if s[l] in countT and windows[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        l, r = res
        return s[l : r + 1] if min_length != float("infinity") else ""