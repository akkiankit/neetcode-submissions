class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # output = []
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             output.append(i)
        #             output.append(j)
        # return output
        seen={}
        for i, num in enumerate(nums): 
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


        