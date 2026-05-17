class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # res = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             res += 1
        # return res
        res = 0
        currSum = 0
        prefixsum = {0:1}
        for num in nums:
            currSum += num
            diff = currSum - k
            res += prefixsum.get(diff, 0)
            prefixsum[currSum] = 1 + prefixsum.get(currSum, 0)
        return res



            
        