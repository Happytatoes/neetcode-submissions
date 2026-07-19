class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        my_dict = {}
        idx = 0

        for num in nums:
            
            complement = target - num
            if complement in my_dict:
                return [my_dict[complement], idx]
                
            my_dict[num] = idx
            idx += 1

           