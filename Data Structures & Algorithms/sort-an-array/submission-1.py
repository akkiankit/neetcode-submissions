class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # return sorted(nums)
        # Bubble sort
        for i in range(len(nums) - 1):
            swapped = False
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums
         

        