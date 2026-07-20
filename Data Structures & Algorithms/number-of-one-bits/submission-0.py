class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0

        for i in range(0, 32):
            mask = (1 << i)
            if n & mask == (1 << i):
                res += 1
        
        return res