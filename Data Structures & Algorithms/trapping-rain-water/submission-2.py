class Solution:
    def trap(self, height: List[int]) -> int:
        
        # amount of water at index i is min(left_max, right_max) - height[i]

        result = 0

        # create prefix array
        # at each index, the maximum to the left of that index

        prefix = [0] * len(height)
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i - 1], height[i - 1])
        
        suffix = [0] * len(height)
        for i in range(len(height) - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i + 1])

        #print(prefix)
        #print(suffix)

        for i in range(0, len(height)):
            water = min(prefix[i], suffix[i]) - height[i]
            if water > 0:
                result += water

            #print("prefix[i] is " + str(prefix[i]))
            #print("suffix[i] is " + str(suffix[i]))
            #print("height[i] is " + str(height[i]))
            #print("so we are adding " + str(min(prefix[i], suffix[i]) - height[i]) + "to result") 
            
        return result








