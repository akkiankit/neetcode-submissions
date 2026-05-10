class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_sum = nums[0]
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         current_sum = nums[i] + nums[j]
        #         max_sum = max(max_sum, current_sum)
        # return max_sum
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum




        