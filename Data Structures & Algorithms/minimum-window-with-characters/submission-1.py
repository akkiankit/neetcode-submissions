class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if t == "":
        #     return ""
        # countT = {}
        # for c in t:
        #    countT[c] = 1 + countT.get(c,0)

        # res = [-1,-1]
        # resLen = float("infinity")

        # for i in range(len(s)):
        #     countS = {}
        #     for j in range(i, len(s)):
        #         countS[s[j]] = 1 + countS.get(s[j], 0)
        #         flag = True
        #         for c in countT:
        #             if countT[c] > countS.get(c,0):
        #                 flag = False
        #                 break
        #             # if c in s[i:j]:
        #             #     continue
        #             # else:
        #             #     flag = False
                
        #         if flag and (j-i+1) < resLen:
        #             resLen = j -i +1
        #             res= [i,j]
        #         #     length = len(s[i:l])
        #         #     min_length.append(length)
        #         # if min(min_length)
            
        # l,r = res        
        # return s[l : r + 1] if resLen != float("infinity") else ""
        # Sliding Windows
        if t == "": return ""
        countT, windows = {}, {}
        l = 0
        res = [-1, -1]
        resLen = float('infinity')
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have = 0
        need = len(countT)

        for r in range(len(s)):
            c = s[r]
            # updating current windows
            windows[c] = 1 + windows.get(c,0)

            # checking the condition if it is satisfied everthing 
            if c in countT and windows[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r- l + 1 ) < resLen:
                    resLen = r - l + 1
                    res = [l,r]

                # pop from the left of our windows
                windows[s[l]] -= 1
                if s[l] in countT and windows[s[l]] < countT[s[l]]:
                    have -=1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('infinity') else ""

                

                
            







