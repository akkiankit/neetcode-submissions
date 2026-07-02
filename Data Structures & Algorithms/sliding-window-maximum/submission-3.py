class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # res = []
        # for i in range(len(nums) - k + 1):
        #     res.append(max(nums[i:i+k]))
        # return res

        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output

        