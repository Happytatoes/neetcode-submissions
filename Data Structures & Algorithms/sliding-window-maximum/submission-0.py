import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        heap = [] # stores (-value, index)

        # init with the first k elems
        for i in range(0, k):
            # negative because this is a max heap
            heapq.heappush(heap, (-nums[i], i))

        # add max of 1st window
        res.append(-heap[0][0])

        # now, iterate until end while removing the thing from the sliding window from the heap and adding the next thing
        for r in range(k, len(nums)):
            # add to the right
            heapq.heappush(heap, (-nums[r], r))
            
            l = r - k + 1  # left edge of current window
            while heap[0][1] < l:
                heapq.heappop(heap)

            res.append(-heap[0][0])


        return res



