class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = {}
        for c in t:
           countT[c] = 1 + countT.get(c,0)

        res = [-1,-1]
        resLen = float("infinity")

        for i in range(len(s)):
            countS = {}
            for j in range(i, len(s)):
                countS[s[j]] = 1 + countS.get(s[j], 0)
                flag = True
                for c in countT:
                    if countT[c] > countS.get(c,0):
                        flag = False
                        break
                    # if c in s[i:j]:
                    #     continue
                    # else:
                    #     flag = False
                
                if flag and (j-i+1) < resLen:
                    resLen = j -i +1
                    res= [i,j]
                #     length = len(s[i:l])
                #     min_length.append(length)
                # if min(min_length)
            
        l,r = res        
        return s[l : r + 1] if resLen != float("infinity") else ""
        