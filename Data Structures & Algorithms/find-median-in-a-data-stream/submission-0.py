import heapq
class MedianFinder:

    def __init__(self):
        self.data = []
        self.sorted_li = []
        
    def addNum(self, num: int) -> None:
        self.data.append(num)
        heap = self.data.copy()
        heapq.heapify(heap)
        self.sorted_li = []
        while heap:
            self.sorted_li.append(heapq.heappop(heap))
        
        print(self.sorted_li)

    def findMedian(self) -> float:
        if len(self.sorted_li) % 2 == 0:
            mid = len(self.sorted_li) // 2
            return (self.sorted_li[mid-1] + self.sorted_li[mid] )/2
        else:
            mid = len(self.sorted_li) // 2
            return self.sorted_li[mid]

        
        