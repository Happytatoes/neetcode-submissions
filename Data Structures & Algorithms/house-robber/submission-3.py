class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        ptr_1 = nums[0]
        ptr_2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            new = max(nums[i] + ptr_1, ptr_2)
            temp = ptr_2
            ptr_2 = new
            ptr_1 = temp
        
        return max(ptr_1, ptr_2)
        