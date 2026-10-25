class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums
        heapq.heapify(minHeap)

        for i in range(len(nums) - k):
            heapq.heappop(minHeap)
        
        return minHeap[0]