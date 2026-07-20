class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        left = 0
        right = n - 1 

        while left <= right:
            index = (left + right) // 2

            if nums[index] == target:
                return index
            elif nums[index] < target:
                left = index + 1
            else:
                right = index - 1

        return -1