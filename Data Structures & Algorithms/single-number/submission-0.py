class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        result = 0

        for elem in nums:
            result ^= elem

        return result 