class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triples = []
        nums.sort()

        for i in range(0, len(nums)):
            
            left = 0
            right = len(nums) - 1
            
            while left < right:
                
                if left == i:
                    left += 1
                    continue
                if right == i:
                    right -= 1
                    continue

                current = nums[left] + nums[right] + nums[i]
                if current == 0:
                    # found valid 3sum
                    triple = sorted([nums[left], nums[right], nums[i]])
                    if triple not in triples: 
                        triples.append(triple)
                    left += 1
                    right -= 1
                elif current > 0:
                    right -= 1
                else:
                    left += 1

        return triples
                    












