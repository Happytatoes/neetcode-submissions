class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        
        def recurse(index, current_arr):
            if index == len(nums):
                res.append(current_arr.copy())
                return

            # decision to add
            current_arr.append(nums[index])
            recurse(index + 1, current_arr)

            # decision to not add (whatever's at this index)
            current_arr.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            recurse(index + 1, current_arr)

        recurse(0, [])
        return res