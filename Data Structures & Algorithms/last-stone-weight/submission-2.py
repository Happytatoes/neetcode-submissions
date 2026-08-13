import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            heaviest_1 = -heapq.heappop(heap)
            heaviest_2 = -heapq.heappop(heap)

            if heaviest_1 == heaviest_2:
                continue
            else:
                new = abs(heaviest_1 - heaviest_2)
                heapq.heappush(heap, -new)
        
        if len(heap) == 0:
            return 0

        return -heap[0]