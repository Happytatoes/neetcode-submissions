class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       
        exp_xor = 0
        act_xor = 0

        for i in range(0, len(nums) + 1):
            exp_xor ^= i

        for num in nums:
            act_xor ^= num

        return exp_xor ^ act_xor
