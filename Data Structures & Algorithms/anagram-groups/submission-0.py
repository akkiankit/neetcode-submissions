class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_sorted = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in group_sorted.keys():
                group_sorted[key].append(word)
            else:
                group_sorted[key] = [word]
        group = []
        for item in group_sorted.values():
            group.append(item)

        return group
