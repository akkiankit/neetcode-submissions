class MedianFinder:

    def __init__(self):
        # Max Heap containing the smaller halp
        self.left = []
        # Min Heap containg the larger half
        self.right = []
        
    def addNum(self, num: int) -> None:
        # step 1: Add the num to left half by defualt
        heapq.heappush(self.left, -1 * num)

        # step 2: Move the largest left value to right
        val =-1 * heapq.heappop(self.left)
        heapq.heappush(self.right, val)

        # Step 3: Keep left equal in size or one larger
        if len(self.right) > len(self.left) :
            min_val = heapq.heappop(self.right)
            heapq.heappush(self.left, -1 * min_val)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return float(-self.left[0])
        
        return (-self.left[0] + self.right[0]) / 2

        