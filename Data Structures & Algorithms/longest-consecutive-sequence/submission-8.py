class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        unique_num = sorted(set(nums))
        start = 0
        end = 0
        cons_len= 0
        while start <= end and end < len(unique_num):
            if (unique_num[end] - unique_num[start]) == (end - start):
                end += 1
            else:
                cons_len = max(cons_len, end - start)
                start = end

        cons_len = max(cons_len, end - start)
        return cons_len

        