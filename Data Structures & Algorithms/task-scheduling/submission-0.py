class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = {}
        for t in tasks:
            if t not in freq:
                freq[t] = 0
            freq[t] += 1

        maxHeap = []
        for f in freq: 
            maxHeap.append(-freq[f])
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            if maxHeap:
                top = heapq.heappop(maxHeap)
                top += 1 
                if top != 0:
                    q.append( (top, time + n) )

            if q and q[0][1] == time:
                free = q.popleft()
                heapq.heappush(maxHeap, free[0])
            time += 1
        
        return time