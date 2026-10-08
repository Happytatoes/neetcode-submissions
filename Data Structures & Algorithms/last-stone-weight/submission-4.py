class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = stones
        for i in range(len(heap)):
            heap[i] *= -1
        heapq.heapify(heap)
        
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first > second:
                heapq.heappush(heap, second - first)
        
        if len(heap) == 0:
            return 0 
        return -heap[0] 
        