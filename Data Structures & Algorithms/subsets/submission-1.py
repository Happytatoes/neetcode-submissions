class Solution:

    def helper(self, nums: List[int]):
        if nums == [] or nums == None or nums in self.result:
            return
        
        self.result.append(list(nums))
        
        for index in range(0, len(nums)):
            num = nums[index]
            nums.remove(nums[index])
            self.helper(nums)
            nums.insert(index, num)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = [[]]
        self.helper(nums)
        return self.result
