class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return True if len(nums) > len(set(nums)) else False
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False



        