class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # [3, 7] t = 10

        number_to_index = {} # key: number, value: index

        for index in range(0, len(nums)):
            num = nums[index]
            complement = target - num
            if complement in number_to_index:
                return [number_to_index[complement], index]
            number_to_index[num] = index
        
