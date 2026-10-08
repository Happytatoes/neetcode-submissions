class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = stones
        for i in range(len(max_heap)):
            max_heap[i] *= -1
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            
            if first == second:
                continue
            
            new = abs(first - second)
            heapq.heappush(max_heap, -new)
        
        if len(max_heap) == 0:
            return 0 
        return -max_heap[0] 
        