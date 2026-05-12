class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        for word in strs:
            wordS = "".join(sorted(word))
            # print(word, wordS)
            if wordS in grp:
                grp[wordS].append(word)
            else:
                grp[wordS] = [word]
        return [list(key) for key in grp.values()]


        