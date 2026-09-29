class Solution:

    def climbStairs(self, n: int) -> int:
        
        num_1, num_2 = 1, 1

        for i in range(n - 1):
            temp = num_2
            num_2 = num_1 + num_2
            num_1 = temp
        
        return num_2
