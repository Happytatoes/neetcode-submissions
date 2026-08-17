class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current_subset = []
        self.helper(0, nums, current_subset, result)
        return result

    def helper(self, index, nums: List[int], current_subset: List[int], result: List[List[int]]):

        # base case: we've made a decision for every element
        if index == len(nums):
            result.append(current_subset[:])
            return
        
        # run the helper with the number appended
        current_subset.append(nums[index])
        self.helper(index + 1, nums, current_subset, result)
    
        # run the helper with the number not appended
        current_subset.pop()
        self.helper(index + 1, nums, current_subset, result)
