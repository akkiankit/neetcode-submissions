class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        for i in range(0, len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum = sum(nums[i:j+1:])
                if current_sum > max_sum:
                    max_sum = current_sum
        return max_sum


        