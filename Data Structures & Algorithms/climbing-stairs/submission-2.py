class Solution:

    def climbStairs(self, n: int) -> int:

        if n == 1 or n == 0:
            return n

        #index = step number
        cache = [0] * (n + 1)
        cache[1] = 1
        cache[2] = 2

        for i in range(3, n + 1):
            
            one_step_back = cache[i - 1]
            two_steps_back = cache[i - 2]
           
            # how many ways to get here? 
            # THERE ARE ONLY TWO WAYS TO GET TO i, EITHER FROM i - 1 or from i - 2. SO JUST # ways to get to either of those. 

            cache[i] = cache[i - 1] + cache[i - 2]

        print(cache)
        return cache[n]