import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums: 
            if len(self.heap) < self.k: 
                # unconditionally add it
                heapq.heappush(self.heap, num)
            else:
                # only do the swap if it's greater than the least elem
                if num > self.heap[0]:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k: 
            # unconditionally add it
            heapq.heappush(self.heap, val)
        else:
            # only do the swap if it's greater than the least elem
            if val > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)

        print(self.heap)
        return self.heap[0]


