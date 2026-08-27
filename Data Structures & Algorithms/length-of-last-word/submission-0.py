class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        listofwords = s.strip().split(" ")
        return len(listofwords[-1])
        