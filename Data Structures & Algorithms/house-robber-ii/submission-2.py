class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_line(nums[1:]), self.rob_line(nums[0:len(nums)-1]))

    def rob_line(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]

        ptr_1 = arr[0]
        ptr_2 = max(arr[0], arr[1])

        for i in range(2, len(arr)):
            new = max(arr[i] + ptr_1, ptr_2)
            temp = ptr_2
            ptr_2 = new
            ptr_1 = temp
        
        return max(ptr_1, ptr_2)
        