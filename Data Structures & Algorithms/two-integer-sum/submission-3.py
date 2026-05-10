class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # result = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             result.append(i)
        #             result.append(j)

        # return result
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i





        