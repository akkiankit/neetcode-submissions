class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two Pointer approach:
        nums.sort()
        res = []
    
        for i, a in enumerate(nums):
            a = nums[i]
            if a > 0:
                break
            
            if i > 0  and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

        # nums.sort()
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1

        # res = []
        # for i in range(len(nums)):
        #     count[nums[i]] -= 1
        #     if i and nums[i] == nums[i - 1]:
        #         continue

        #     for j in range(i + 1, len(nums)):
        #         count[nums[j]] -= 1
        #         if j - 1 > i and nums[j] == nums[j - 1]:
        #             continue
        #         target = -(nums[i] + nums[j])
        #         if count[target] > 0:
        #             res.append([nums[i], nums[j], target])

        #     for j in range(i + 1, len(nums)):
        #         count[nums[j]] += 1
        # return res
        # result = set()
        # nums = sorted(nums)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 val = [nums[i], nums[j], nums[k]]
        #                 result.add(tuple(val))
        # return [list(i) for i in result]
                    
        
        