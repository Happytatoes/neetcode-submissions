class Solution:
    def trap(self, height: List[int]) -> int:
        
        result = 0
        n = len(height)

        # step 1:
        # create an array of tuples where the index corresponds to 
        # (maximum left elem), (maximum right elem)
        
        prefix = [0] * n
        suffix = [0] * n

        # build the prefix arr

        prefix[0] = height[0]
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i])
        
        # build the suffix arr

        suffix[n-1] = height[n-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i])

        # step 2: 
        # at any particular index position, the amount trapped is 
        # min ( biggest l * biggest r ) - height at that index

        for i in range(0, n):
            result += min(prefix[i], suffix[i]) - height[i]
        
        return result
            
       