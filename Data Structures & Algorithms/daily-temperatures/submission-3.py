class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # we're greater than whatever's at the top of the stack
            # that means we can pop it and get a result
            while stack and temperatures[i] > stack[-1][1]:
                index, temp = stack.pop()
                # we put at the index the difference between i and the
                # index because that's how many days it took 
                # to find a hotter day
                res[index] = i - index

            # we then add the index and temp to the stack
            stack.append((i, temperatures[i]))

        return res