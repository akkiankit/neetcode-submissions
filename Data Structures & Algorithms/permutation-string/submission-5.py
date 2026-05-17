class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 = sorted(s1)
        # if len(s1) > len(s2): return False
        # for i in range(len(s2)):
        #     for j in range(i,len(s2)):
        #         substr = s2[i:j+1]
        #         substr = sorted(substr)
        #         if substr == s1:
        #             return True
        # return False
        if len(s1) > len(s2):
            return False

        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        need = len(count1)

        for i in range(len(s2)):
            count2 = {}
            cur = 0

            for j in range(i, len(s2)):
                char = s2[j]
                count2[char] = 1 + count2.get(char, 0)

                if count1.get(char, 0) < count2[char]:
                    break

                if count1.get(char, 0) == count2[char]:
                    cur += 1

                if cur == need:
                    return True

        return False

        