class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brute force
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if i != j:
        #             if numbers[i] + numbers[j] == target:
        #                 return [i+1, j+1]

        # # since array is sorted, we can think of two pointer
        # l = 0
        # r = len(numbers) - 1
        # while l < r:
        #     current_sum = numbers[l] + numbers[r]
        #     if current_sum < target:
        #         l += 1
        #     elif current_sum > target:
        #         r -= 1
        #     else:
        #         return [l+1, r+1]

        # Binary Search O(nlogn)
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l)//2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []



        

        