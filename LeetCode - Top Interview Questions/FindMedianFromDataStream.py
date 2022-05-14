import heapq

class MedianFinder:
    def __init__(self):
        self.smaller = []
        self.larger = []

    def addNum(self, num: int) -> None:
        min_elem = heapq.heappushpop(self.larger, num)
        heapq.heappush(self.smaller, -min_elem)
        if len(self.smaller) - len(self.larger) == 2:
            heapq.heappush(self.larger, -heapq.heappop(self.smaller))

    def findMedian(self) -> float:
        if (len(self.smaller) + len(self.larger)) % 2 == 0:
            return (-self.smaller[0] + self.larger[0]) / 2
        else:
            return self.larger[0] if len(self.larger) > len(self.smaller) else -self.smaller[0]


# Your MedianFinder object will be instantiated and called as such:
medianFinder = MedianFinder()
medianFinder.addNum(6)
print(
    medianFinder.findMedian()
)
medianFinder.addNum(10)
print(
    medianFinder.findMedian()
)
medianFinder.addNum(2)
print(
    medianFinder.findMedian()
)
medianFinder.addNum(6)
print(
    medianFinder.findMedian()
)
medianFinder.addNum(5)