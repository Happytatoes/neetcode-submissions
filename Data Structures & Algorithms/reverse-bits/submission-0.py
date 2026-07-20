class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0

        for i in range(0, 32):
            # if the ith bit of n is 1, this is one
            if (n >> i) & 1:
                # take that bit, reverse it, and or it with the result
                res |= (1 << (31 - i))

        return res