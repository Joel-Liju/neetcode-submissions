import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for n in nums:
            heapq.heappush(self.heap, n)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        tempvals = heapq.nlargest(self.k, self.heap)
        return tempvals[len(tempvals) - 1]
