class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return(True if len(nums) > len(list(set(nums))) else False)

            
        