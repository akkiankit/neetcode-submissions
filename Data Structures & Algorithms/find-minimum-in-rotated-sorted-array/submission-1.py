class Solution:
    def findMin(self, nums: List[int]) -> int:
        # min_number = nums[0]
        # for i in range(0, len(nums)):
        #     if min_number > nums[i]:
        #         min_number = nums[i]
        # return min_number
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]




        