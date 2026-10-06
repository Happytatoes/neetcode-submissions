class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            mid_idx = (l + r) // 2
            mid = nums[mid_idx]
            if target == mid:
                return mid_idx
            elif target > mid:
                l = mid_idx + 1
            else:
                r = mid_idx - 1
        
        return -1
            