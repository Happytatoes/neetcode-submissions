class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        res = [0] * len(temperatures)
        stack = []

        for i in range(0, n):

            # -1 means top of stack, so this is while the current temp is higher than the top of stack
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()

            # then we add the new thing 
            stack.append((temperatures[i], i))

            #print(stack)
        
            
        return res
