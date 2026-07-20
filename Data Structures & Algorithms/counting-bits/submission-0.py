class Solution:

    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(0, 32):
            mask = (1 << i)
            if n & mask == (1 << i):
                res += 1
        return res

    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(0, n+1):
            output.append(self.hammingWeight(i))
        return output