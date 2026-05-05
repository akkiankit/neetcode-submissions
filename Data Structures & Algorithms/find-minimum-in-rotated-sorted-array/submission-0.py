class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_number = nums[0]
        for i in range(0, len(nums)):
            if min_number > nums[i]:
                min_number = nums[i]
        return min_number

        