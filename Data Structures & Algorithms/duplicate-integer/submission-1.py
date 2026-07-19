class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # cooler solution
        return len(set(nums)) < len(nums)

        # old solution

        #my_set = set()

        #for num in nums:
        #    if num in my_set:
        #        return True
        #    my_set.add(num)

        #return False
